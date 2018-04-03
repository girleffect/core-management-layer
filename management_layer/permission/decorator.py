"""
The permission module exposes a decorator that can be used to protect
function calls by specifying the permissions required to execute the function.
"""
import asyncio
import json
import logging
import typing
import uuid
from functools import wraps

from aiohttp.web_exceptions import HTTPForbidden

from management_layer.constants import TECH_ADMIN_ROLE_ID
from management_layer.permission.utils import Operator, ResourcePermissions, \
    user_has_permissions, get_user_roles_for_domain, get_user_roles_for_site
from management_layer.mappings import Mappings

logger = logging.getLogger(__name__)


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
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Extract the request from the function arguments
            request = get_value_from_args_or_kwargs(request_field, args, kwargs)

            user_id, site_id = get_user_and_site(request)

            allowed = await user_has_permissions(
                request, user_id, operator, resource_permissions,
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


def requester_has_role(
        nocache: bool = False,
        request_field: typing.Union[int, str] = 0,
        body_field: typing.Union[int, str] = None,
        target_user_id_field: typing.Union[int, str] = None,
        role_id_field: typing.Union[int, str] = None,
        domain_id_field: typing.Union[int, str] = None,
        site_id_field: typing.Union[int, str] = None
) -> typing.Callable:
    """
    This function is used as a decorator to protect functions that add and remove roles on
    domains and sites to users, e.g.
    ```
    @requester_has_role()
    def usersiterole_create(request, body, **kwargs):
        pass
    ```
    The body must contain the user_id of the recipient, the role_id of the role that must be
    assigned and the site_id of the site for which the user will must get the role.
    ```
    @requester_has_role()
    def usersiterole_delete(request, user_id, site_id, role_id, **kwargs):
        pass
    ```
    The user making the request is inferred from the token passed with the request.

    IMPORTANT: This decorator can be applied to both coroutines and normal functions AND it
    always changes the decorated function into a coroutine, meaning it must be called using `await`:
    ```
    @requester_has_role()
    def doSomething(request, body):
        pass

    # Call the function
    result = await doSomething(request, body)  # Decorator change function to coroutine
    ```

    :param nocache: Bypass the cache if True
    :param request_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the request parameter.
    :param body_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the body parameter. The
        body parameter is a dictionary that can contain a user_id, role_id and either a
        site_id or domain_id, depending in the call.
    :param target_user_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the user_id field of the target user,
        i.e. the user for which a role must be set or removed.
    :param role_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the role_id field.
    :param domain_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the domain_id field.
    :param site_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the site_id field.
    :raises: Forbidden if the user does not have the role that is being invoked or revoked.
    """

    def wrap(f):
        @wraps(f)
        async def wrapped_f(*args, **kwargs):
            """
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Extract the request from the function arguments
            request = get_value_from_args_or_kwargs(request_field, args, kwargs)

            user_id, site_id = get_user_and_site(request)

            # Extract the user_id for which a role must be a assigned/revoked
            target_user_id = get_value_from_args_or_kwargs(target_user_id_field, args, kwargs)

            if body_field is not None:
                body = get_value_from_args_or_kwargs(body_field, args, kwargs)

                # When the body is specified, the xxx_field arguments must be the names of the
                # fields in the body dictionary.
                role_id = body[role_id_field or "role_id"]
                # We expect either a domain_id or a site_id to be provided
                domain_id = body.get(domain_id_field or "domain_id")
                site_id = body.get(site_id_field or "site_id")
                if domain_id is None and site_id is None or \
                        domain_id is not None and site_id is not None:
                    raise RuntimeError("Either a domain_id or site_id needs to exist in the body")
            else:
                # If a body is not specified, the rest of the arguments are considered to be
                # positional arguments.
                role_id = get_value_from_args_or_kwargs(role_id_field, args, kwargs)
                if domain_id_field is None and site_id_field is None or \
                        domain_id_field is not None and site_id_field is not None:
                    raise RuntimeError("Either a domain_id_field or site_id_field needs to defined")

                if domain_id_field:
                    domain_id = get_value_from_args_or_kwargs(domain_id_field, args, kwargs)
                else:
                    site_id = get_value_from_args_or_kwargs(site_id_field, args, kwargs)

            if domain_id:
                user_roles = await get_user_roles_for_domain(request, user_id, domain_id, nocache)
            else:  # Use site_id
                user_roles = await get_user_roles_for_site(request, user_id, site_id, nocache)

            # If the user roles contains the one we want to assign or Tech Admin, we allow
            # the call to proceed.
            if user_roles.intersection([role_id, TECH_ADMIN_ROLE_ID]):
                if asyncio.iscoroutinefunction(f):
                    return await f(*args, **kwargs)
                else:
                    return f(*args, **kwargs)

            raise HTTPForbidden(body=json.dumps({
                "message": "Forbidden"
            }))

        return wrapped_f

    return wrap


def get_value_from_args_or_kwargs(
        argument_identifier: typing.Union[int, str],
        args: typing.Tuple[typing.Any, ...], kwargs: dict
):
    """

    :param argument_identifier: The index or name of a function argument
    :param args: A list of positional arguments
    :param kwargs: A dictionary of named arguments
    :return: The value of the argument.
    """
    argument_identifier_type = type(argument_identifier)
    if argument_identifier_type is int:
        return args[argument_identifier]

    if argument_identifier_type is str:
        return kwargs[argument_identifier]

    raise RuntimeError("Invalid value for argument identifier")


def get_user_and_site(request):
    """
    A request contains the JWT token payload from which we get
    * the user id from the "sub" (subscriber) field
    * the client id from the "aud" (audience) field
    :param request: An HttpRequest
    :return: A (user_id, site_id) tuple.
    :raises: HTTPForbidden if the token's client id does not map to a site id.
    """
    # Extract the user's UUID from the request
    user_id = uuid.UUID(request["token"]["sub"])
    # Extract the client id from the request
    client_id = request["token"]["aud"]
    if client_id not in Mappings.site_client_id_to_id_map:
        raise HTTPForbidden(body=json.dumps({
            "message": f"No site linked to the client '{client_id}'"
        }))

    site_id = Mappings.site_client_id_to_id_map[client_id]
    return user_id, site_id
