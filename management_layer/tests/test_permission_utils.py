from unittest import TestCase
from unittest.mock import patch
from uuid import uuid1

from datetime import datetime

import management_layer.constants
import management_layer.permission
from access_control import RoleResourcePermission
from management_layer.permission import utils, require_permissions

# Test dictionaries commonly used by tests
TEST_ROLE_LABEL_TO_ID_MAP = {"role{}".format(i): i for i in range(1, 11)}
TEST_PERMISSION_NAME_TO_ID_MAP = {"permission{}".format(i): i for i in range(1, 11)}
TEST_RESOURCE_URN_TO_ID_MAP = {"urn:resource{}".format(i): i for i in range(1, 11)}
TEST_SITES = {1: {"client_id": "test_client"}}
TEST_SITE_CLIENT_ID_TO_ID_MAP = {
    detail["client_id"]: id_ for id_, detail in TEST_SITES.items()
}


class TestRequirePermissionsDecorator(TestCase):
    """
    These tests exercise the functionality provided by the @require_permissions
    decorator.
    """
    def setUp(self):
        self.user = uuid1()
        self.site_id = 1
        self.client_id = TEST_SITES[self.site_id]["client_id"]
        self.dummy_request = {
            "token": {
                "sub": self.user.hex,
                "aud": self.client_id
            }
        }

    def test_name_and_docstring(self):
        """
        The name attribute and docstring of a decorated function should stay
        the same when the decorator is implemented properly.
        """
        @require_permissions(all, [("urn:ge:test:foo", "read")])
        def simple(_request, **_kwargs):
            """This docstring is checked."""
            pass

        self.assertEqual(simple.__name__, "simple")
        self.assertEqual(simple.__doc__, "This docstring is checked.")

    @patch.dict("management_layer.mappings.SITE_CLIENT_ID_TO_ID_MAP",
                TEST_SITE_CLIENT_ID_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_empty_resource_permissions_lists(self, mocked_function):
        """
        Check the expected behaviour when an empty resource permission list
        is used with the any or all operation.
        We mock a response for the get_user_roles_for_site() function in
        order to test the case where the specified required resource
        permission list is empty.
        """
        # require_permissions(all, []) always succeeds, regardless of which
        # roles the user has.
        @require_permissions(all, [])
        def empty_all(_request):
            return True

        # require_permissions(any, []) always fails, regardless of which roles
        # the user has.
        @require_permissions(any, [])
        def empty_any(_request):
            raise RuntimeError("This should never get executed")

        mocked_function.return_value = ["some_role"]

        # Always gets allowed, regardless of the user's roles
        self.assertTrue(empty_all(self.dummy_request))

        # Never gets allowed, regardless of the user's roles
        with self.assertRaises(utils.Forbidden):
            empty_any(self.dummy_request)

    @patch.dict("management_layer.mappings.SITE_CLIENT_ID_TO_ID_MAP",
                TEST_SITE_CLIENT_ID_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_positional_args(self, mocked_function):
        """
        Check that positional argument lookups of the request works.
        We mock a response for the get_user_roles_for_site() function in
        order to check that it was called with the appropriate values.
        """
        @require_permissions(all, [], request_field=1)
        def positional_args(_arg1, _request):
            return True

        # Call the test function...
        positional_args("some_value", self.dummy_request)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(self.user, self.site_id, False)

    @patch.dict("management_layer.mappings.SITE_CLIENT_ID_TO_ID_MAP",
                TEST_SITE_CLIENT_ID_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_keyword_args(self, mocked_function):
        """
        Check that keyword-based lookups of the user and site information works.
        We mock a response for the get_user_roles_for_site() function in
        order to check that it was called with the appropriate values.
        """
        @require_permissions(all, [], request_field="i_am_a_request")
        def keyword_args(**kwargs):
            return True

        # Call the test function...
        keyword_args(arg=123, i_am_a_request=self.dummy_request)
        # ...and verify that the mocked function was called with the right
        # arguments.
        mocked_function.assert_called_with(self.user, self.site_id, False)

    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_stacked_decorators(self, mocked_function):
        """
        We mock a response for the get_user_roles_for_site() function in
        order to test the case where the specified required resource
        permission list is empty.
        """
        @require_permissions(all, [])
        @require_permissions(any, [])
        def stack(_request):
            raise RuntimeError("This should never get executed")

        @require_permissions(any, [])
        @require_permissions(all, [])
        def reverse_stack(_request):
            raise RuntimeError("This should never get executed")

        mocked_function.return_value = ["some_role"]

        with self.assertRaises(utils.Forbidden):
            stack(self.dummy_request)

        with self.assertRaises(utils.Forbidden):
            reverse_stack(self.dummy_request)

    @patch.dict("management_layer.mappings.SITE_CLIENT_ID_TO_ID_MAP",
                TEST_SITE_CLIENT_ID_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.ROLE_LABEL_TO_ID_MAP",
                TEST_ROLE_LABEL_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.PERMISSION_NAME_TO_ID_MAP",
                TEST_PERMISSION_NAME_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.RESOURCE_URN_TO_ID_MAP",
                TEST_RESOURCE_URN_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_all(self, mocked_get_user_roles_for_site,
                 mocked_get_role_resource_permissions):
        """
        A test of the 'all' operator by mocking roles, resources and
        permissions.
        """
        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            responses = {
                ("role1", "urn:resource1"): [1],
                ("role2", "urn:resource2"): [2],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @require_permissions(all, [("urn:resource1", "permission1")])
        def single_requirement(_request):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.return_value = []
        with self.assertRaises(utils.Forbidden):
            single_requirement(self.dummy_request)

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role2"]
        with self.assertRaises(utils.Forbidden):
            single_requirement(self.dummy_request)

        # If the user has a role with the necessary permission,
        # then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        self.assertTrue(single_requirement(self.dummy_request))

        @require_permissions(all, [("urn:resource1", "permission1"),
                                   ("urn:resource2", "permission2")])
        def multiple_requirements(_request):
            return True

        # If the user has only one of the permissions, then access is
        # denied.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        with self.assertRaises(utils.Forbidden):
            multiple_requirements(self.dummy_request)

        # If the user has all the permissions, then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1", "role2"]
        self.assertTrue(multiple_requirements(self.dummy_request))

    @patch.dict("management_layer.mappings.SITE_CLIENT_ID_TO_ID_MAP",
                TEST_SITE_CLIENT_ID_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.ROLE_LABEL_TO_ID_MAP",
                TEST_ROLE_LABEL_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.PERMISSION_NAME_TO_ID_MAP",
                TEST_PERMISSION_NAME_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.RESOURCE_URN_TO_ID_MAP",
                TEST_RESOURCE_URN_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_any(self, mocked_get_user_roles_for_site,
                 mocked_get_role_resource_permissions):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.
        """
        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            responses = {
                ("role1", "urn:resource1"): [1],
                ("role2", "urn:resource2"): [2],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @require_permissions(any, [("urn:resource1", "permission1")])
        def single_requirement(_request):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.return_value = []
        with self.assertRaises(utils.Forbidden):
            single_requirement(self.dummy_request)

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role2"]
        with self.assertRaises(utils.Forbidden):
            single_requirement(self.dummy_request)

        # If the user has a role with the necessary permission,
        # then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        self.assertTrue(single_requirement(self.dummy_request))

        @require_permissions(any, [("urn:resource1", "permission1"),
                                   ("urn:resource2", "permission2")])
        def multiple_requirements(_request):
            return True

        # If the user has any one of the permissions, then access is
        # allowed.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        self.assertTrue(multiple_requirements(self.dummy_request))

        mocked_get_user_roles_for_site.return_value = ["role2"]
        self.assertTrue(multiple_requirements(self.dummy_request))

        mocked_get_user_roles_for_site.return_value = ["role1", "role2"]
        self.assertTrue(multiple_requirements(self.dummy_request))

        # If the user has a role without the necessary permission,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role3"]
        with self.assertRaises(utils.Forbidden):
            single_requirement(self.dummy_request)

    @patch.dict("management_layer.mappings.SITE_CLIENT_ID_TO_ID_MAP",
                TEST_SITE_CLIENT_ID_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.ROLE_LABEL_TO_ID_MAP",
                TEST_ROLE_LABEL_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.PERMISSION_NAME_TO_ID_MAP",
                TEST_PERMISSION_NAME_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.RESOURCE_URN_TO_ID_MAP",
                TEST_RESOURCE_URN_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_combo(self, mocked_get_user_roles_for_site,
                   mocked_get_role_resource_permissions):
        """
        A test of the 'any' operator by mocking roles, resources and
        permissions.

        :param mocked_get_user_roles_for_site: Function mocked by @patch
            decorator
        :param mocked_get_role_resource_permissions: Function mocked by @patch
            decorator
        """
        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            responses = {
                ("role1", "urn:resource1"): [1],
                ("role2", "urn:resource2"): [2],
                ("role3", "urn:resource3"): [3],
            }
            return responses.get((role, resource), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        @require_permissions(all, [("urn:resource1", "permission1")])
        @require_permissions(any, [("urn:resource2", "permission2"),
                                   ("urn:resource3", "permission3")])
        def combo_requirement(_request):
            return True

        # The values for the user and site is not important since this test
        # mocks the roles returned.

        # If the user has no roles, then access is denied.
        mocked_get_user_roles_for_site.return_value = []
        with self.assertRaises(utils.Forbidden):
            combo_requirement(self.dummy_request)

        # If the user has roles partially fulfilling the required permissions,
        # then access is denied.
        mocked_get_user_roles_for_site.return_value = ["role1"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(self.dummy_request)

        mocked_get_user_roles_for_site.return_value = ["role2"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(self.dummy_request)

        mocked_get_user_roles_for_site.return_value = ["role3"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(self.dummy_request)

        mocked_get_user_roles_for_site.return_value = ["role2", "role3"]
        with self.assertRaises(utils.Forbidden):
            combo_requirement(self.dummy_request)

        # If the user has roles with the necessary permissions,
        # then access is allowed.
        mocked_get_user_roles_for_site.return_value = ["role1", "role2"]
        self.assertTrue(combo_requirement(self.dummy_request))

        mocked_get_user_roles_for_site.return_value = ["role1", "role3"]
        self.assertTrue(combo_requirement(self.dummy_request))


class TestUtils(TestCase):

    @patch.dict("management_layer.mappings.ROLE_LABEL_TO_ID_MAP",
                TEST_ROLE_LABEL_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.PERMISSION_NAME_TO_ID_MAP",
                TEST_PERMISSION_NAME_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.RESOURCE_URN_TO_ID_MAP",
                TEST_RESOURCE_URN_TO_ID_MAP, clear=True)
    @patch("access_control.api.access_control_api"
           ".AccessControlApi.roleresourcepermission_list")
    def test_role_has_permissions(self, mocked_roleresourcepermission_list):
        """
        Test that the "role_has_permissions" function work as intended.
        :param mocked_roleresourcepermission_list: Function mocked by @patch
            decorator
        """
        def dummy_roleresourcepermission_list(role_id, resource_id):
            responses = {
                (1, 1): [
                    RoleResourcePermission(**{
                        "role_id": role_id,
                        "resource_id": resource_id,
                        "permission_id": TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                        "created_at": datetime.now(),
                        "updated_at": datetime.now()
                    })
                ]
            }
            return responses.get((role_id, resource_id), [])

        mocked_roleresourcepermission_list.side_effect = \
            dummy_roleresourcepermission_list

        # We test both the cached and non-cached use-cases. It is important
        # that we test with nocache=True first, since this will not read from
        # the cache, but populate it for the next iteration where nocache=False.
        for nocache in [True, False]:
            # Call function using labels
            self.assertTrue(
                utils.role_has_permission("role1", "permission1",
                                          "urn:resource1", nocache)
            )

            self.assertFalse(
                utils.role_has_permission("role1", "permission2",
                                          "urn:resource1", nocache)
            )

            self.assertFalse(
                utils.role_has_permission("role1", "permission1",
                                          "urn:resource2", nocache)
            )

            # Call function using ids
            self.assertTrue(
                utils.role_has_permission(
                    TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                    TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"], nocache)
            )

            self.assertFalse(
                utils.role_has_permission(
                    TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_PERMISSION_NAME_TO_ID_MAP["permission2"],
                    TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"], nocache)
            )

            self.assertFalse(
                utils.role_has_permission(
                    TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                    TEST_RESOURCE_URN_TO_ID_MAP["urn:resource2"], nocache)
            )

    @patch.dict("management_layer.mappings.ROLE_LABEL_TO_ID_MAP",
                TEST_ROLE_LABEL_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.PERMISSION_NAME_TO_ID_MAP",
                TEST_PERMISSION_NAME_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.RESOURCE_URN_TO_ID_MAP",
                TEST_RESOURCE_URN_TO_ID_MAP, clear=True)
    @patch("access_control.api.access_control_api"
           ".AccessControlApi.roleresourcepermission_list")
    def test_roles_have_permissions(self, mocked_roleresourcepermission_list):
        """
        Test that the "roles_have_permissions" function work as intended.
        :param mocked_roleresourcepermission_list: Function mocked by @patch
            decorator
        """
        def dummy_roleresourcepermission_list(role_id, resource_id):
            responses = {
                (1, 1): [
                    RoleResourcePermission(**{
                        "role_id": role_id,
                        "resource_id": resource_id,
                        "permission_id": TEST_PERMISSION_NAME_TO_ID_MAP["permission1"],
                        "created_at": datetime.now(),
                        "updated_at": datetime.now()
                    })
                ]
            }
            return responses.get((role_id, resource_id), [])

        mocked_roleresourcepermission_list.side_effect = \
            dummy_roleresourcepermission_list

        # We test both the cached and non-cached use-cases. It is important
        # that we test with nocache=True first, since this will not read from
        # the cache, but populate it for the next iteration where nocache=False.
        # Test using the 'all' operator
        for nocache in [True, False]:
            # Call function using labels
            self.assertTrue(
                utils.roles_have_permissions(
                    ["role1", "role2"], all,
                    [("urn:resource1", "permission1")],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    ["role1", "role2"], all,
                    [("urn:resource1", "permission2")],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    ["role1", "role2"], all,
                    [("urn:resource2", "permission1")],
                    nocache
                )
            )

            # Call function using ids
            self.assertTrue(
                utils.roles_have_permissions(
                    [TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]], all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"])],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    [TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]], all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission2"])],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    [TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]], all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource2"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"])],
                    nocache
                )
            )

        # Test using the 'any' operator
        for nocache in [True, False]:
            # Call function using labels
            self.assertTrue(
                utils.roles_have_permissions(
                    ["role1", "role2"], any,
                    [("urn:resource1", "permission1"),
                     ("urn:resource3", "permission3")],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    ["role1", "role2"], any,
                    [("urn:resource3", "permission3"),
                     ("urn:resource4", "permission4")],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    ["role1", "role2"], any,
                    [("urn:resource2", "permission1")],
                    nocache
                )
            )

            # Call function using ids
            self.assertTrue(
                utils.roles_have_permissions(
                    [TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]], any,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"]),
                     (TEST_RESOURCE_URN_TO_ID_MAP["urn:resource3"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission3"])],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    [TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]], all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource3"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission3"]),
                     (TEST_RESOURCE_URN_TO_ID_MAP["urn:resource4"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission4"])],
                    nocache
                )
            )

            self.assertFalse(
                utils.roles_have_permissions(
                    [TEST_ROLE_LABEL_TO_ID_MAP["role1"], TEST_ROLE_LABEL_TO_ID_MAP["role2"]], all,
                    [(TEST_RESOURCE_URN_TO_ID_MAP["urn:resource1"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission1"]),
                     (TEST_RESOURCE_URN_TO_ID_MAP["urn:resource3"],
                      TEST_PERMISSION_NAME_TO_ID_MAP["permission3"])],
                    nocache
                )
            )

        # Check that the TECH_ADMIN role grants permission to everything
        # for 'all' and 'any' operator.
        for operator in [all, any]:
            self.assertTrue(
                utils.roles_have_permissions(
                    [management_layer.constants.TECH_ADMIN], operator,
                    [("urn:resource{}".format(i),
                      "permission{}".format(i)) for i in range(1, 11)],
                    nocache
                )
            )

    @patch.dict("management_layer.mappings.ROLE_LABEL_TO_ID_MAP",
                TEST_ROLE_LABEL_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.PERMISSION_NAME_TO_ID_MAP",
                TEST_PERMISSION_NAME_TO_ID_MAP, clear=True)
    @patch.dict("management_layer.mappings.RESOURCE_URN_TO_ID_MAP",
                TEST_RESOURCE_URN_TO_ID_MAP, clear=True)
    @patch("management_layer.permission.utils.get_role_resource_permissions")
    @patch("management_layer.permission.utils.get_user_roles_for_site")
    def test_user_has_permissions(self, mocked_get_user_roles_for_site,
                                  mocked_get_role_resource_permissions):
        """
        """
        # All users will have only 'role1' on any site
        mocked_get_user_roles_for_site.return_value = [
            TEST_ROLE_LABEL_TO_ID_MAP["role1"]
        ]

        def dummy_get_role_resource_permissions(role, resource, _nocache):
            # Return hand-crafted responses for this test.
            role_id = role if type(role) is int else TEST_ROLE_LABEL_TO_ID_MAP[role]
            resource_id = resource if type(resource) is int else \
                TEST_RESOURCE_URN_TO_ID_MAP[resource]
            responses = {
                (1, 1): [TEST_PERMISSION_NAME_TO_ID_MAP["permission1"]],
                (2, 2): [TEST_PERMISSION_NAME_TO_ID_MAP["permission2"]]
            }
            return responses.get((role_id, resource_id), [])

        mocked_get_role_resource_permissions.side_effect = \
            dummy_get_role_resource_permissions

        user = uuid1()
        site = uuid1()

        # Because the user has only role1 assigned and role1 implies only
        # permission1 on resource1, only this one permission check will succeed.
        self.assertTrue(utils.user_has_permissions(
            user, any, [("urn:resource1", "permission1")], site=site
        ))

        self.assertFalse(utils.user_has_permissions(
            user, any, [("urn:resource1", "permission2")], site=site
        ))

        self.assertFalse(utils.user_has_permissions(
            user, any, [("urn:resource2", "permission2")], site=site
        ))

    def test_get_user_roles_for_site_or_domain(self):
        # We just test the validation performed by this function.
        # Other tests cover the lookups.
        user = uuid1()
        site = uuid1()
        domain = 1

        # Either a site or domain must be specified
        with self.assertRaises(RuntimeError):
            utils.get_user_roles_for_site_or_domain(user)

        # Both a site and domain cannot be specified
        with self.assertRaises(RuntimeError):
            utils.get_user_roles_for_site_or_domain(
                user, site=site, domain=domain
            )

    def test_get_role_resource_permissions(self):
        # TODO
        pass

    def test_get_all_user_roles(self):
        # TODO
        pass

    def test_get_user_roles_for_domain(self):
        # TODO
        pass

    def test_get_user_roles_for_site(self):
        # TODO
        pass