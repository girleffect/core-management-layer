"""
The permission module exposes a decorator that can be used to protect
function calls by specifying the permissions required to execute the function.
"""
import asyncio
import json
import typing
import uuid
from functools import wraps

from aiohttp.web_exceptions import HTTPForbidden

from management_layer.permission.utils import Operator, ResourcePermissions, \
    user_has_permissions
from management_layer.mappings import SITE_CLIENT_ID_TO_ID_MAP


def require_permissions(
    operator: Operator,
    resource_permissions: ResourcePermissions,
    nocache: bool = False,
    request_field: typing.Union[int, str] = 0
) -> typing.Callable:
    """
    This function is used as a decorator to protect functions by specifying
    the permissions that a user requires to perform the action, e.g.
    ```
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    @require_permissions(any, [("urn:ge:test:foo", "read"),
                               ("urn:ge:test:bar", "read"])
    def doSomething(request, arg1, arg2):
        pass
    ```
    As can be seen from the example above, the decorator can be stacked.
    Note, however, that for performance reasons the least amount of
    decorators is preferred.
    ```
    # Logically correct, but suboptimal performance
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    @require_permissions(all, [("urn:ge:test:bar", "write")])
    @require_permissions(all, [("urn:ge:test:baz", "write")])
    def badExample(request, arg1, arg2):
        pass

    # Logically equivalent to the decorators of example above and more efficient
    @require_permissions(all, [("urn:ge:test:foo", "write"),
                               ("urn:ge:test:bar", "write"),
                               ("urn:ge:test:baz", "write")])
    def goodExample(request, arg1, arg2):
        pass
    ```
    This function requires the the user who made the request as well as the
    site from which the request originated in order to look up roles
    associated with the user. The user and site UUID values are read from
    the request field passed to the decorated function. By default we use the first
    argument as the request field. This can be changed in the decorator, e.g.
    ```
    @require_permissions(all, [("urn:ge:test:baz", "write")],
                         request_field=2)
    def example1(arg1, arg2, request):
        pass

    @require_permissions(all, [("urn:ge:test:baz", "write")],
                         request_field="request")  # "request" in kwargs
    def example2(arg1, **kwargs):
        pass
    ```

    IMPORTANT: This decorator can be applied to both coroutines and normal functions AND it
    always changes the decorated function into a coroutine, meaning it must be called using `await`:
    ```
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    def doSomething(request):
        pass

    # Call the function
    result = await doSomething(request)  # Decorator change function to coroutine
    ```

    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param nocache: Bypass the cache if True
    :param request_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the request parameter.
    :raises: Forbidden if the user does not have the required permissions.
    """
    if operator not in [any, all]:
        raise RuntimeError("The operator must be any or all")

    def wrap(f):
        @wraps(f)
        async def wrapped_f(*args, **kwargs):
            """
            The purpose of the wrapper is to get the
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Extract the request from the function arguments
            request_field_type = type(request_field)
            if request_field_type is int:
                request = args[request_field]
            elif request_field_type is str:
                request = kwargs[request_field]
            else:
                raise RuntimeError("Invalid value for request_field")

            # The request contains the JWT token payload from which we get
            # * the user id from the "sub" (subscriber) field
            # * the client id from the "aud" (audience) field

            # Extract the user's UUID from the request
            user = uuid.UUID(request["token"]["sub"])
            # Extract the client id from the request
            client_id = request["token"]["aud"]
            if client_id not in SITE_CLIENT_ID_TO_ID_MAP:
                raise HTTPForbidden(body=json.dumps({
                    "message": f"No site linked to the client '{client_id}'"
                }))

            site_id = SITE_CLIENT_ID_TO_ID_MAP[client_id]

            allowed = await user_has_permissions(
                request, user, operator, resource_permissions,
                site=site_id, nocache=nocache,
            )
            if allowed:
                if asyncio.iscoroutinefunction(f):
                    return await f(*args, **kwargs)
                else:
                    return f(*args, **kwargs)

            raise HTTPForbidden(body=json.dumps({
                "message": "Forbidden"
            }))

        return wrapped_f

    return wrap
