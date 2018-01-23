# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.domain_create import DomainCreate  # noqa: E501
from swagger_server.models.domain_role import DomainRole  # noqa: E501
from swagger_server.models.domain_role_create import DomainRoleCreate  # noqa: E501
from swagger_server.models.domain_role_update import DomainRoleUpdate  # noqa: E501
from swagger_server.models.domain_update import DomainUpdate  # noqa: E501
from swagger_server.models.invitation import Invitation  # noqa: E501
from swagger_server.models.invitation_create import InvitationCreate  # noqa: E501
from swagger_server.models.invitation_domain_role import InvitationDomainRole  # noqa: E501
from swagger_server.models.invitation_domain_role_create import InvitationDomainRoleCreate  # noqa: E501
from swagger_server.models.invitation_site_role import InvitationSiteRole  # noqa: E501
from swagger_server.models.invitation_site_role_create import InvitationSiteRoleCreate  # noqa: E501
from swagger_server.models.invitation_update import InvitationUpdate  # noqa: E501
from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.permission_create import PermissionCreate  # noqa: E501
from swagger_server.models.permission_update import PermissionUpdate  # noqa: E501
from swagger_server.models.resource import Resource  # noqa: E501
from swagger_server.models.resource_create import ResourceCreate  # noqa: E501
from swagger_server.models.resource_update import ResourceUpdate  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.role_create import RoleCreate  # noqa: E501
from swagger_server.models.role_resource_permission import RoleResourcePermission  # noqa: E501
from swagger_server.models.role_resource_permission_create import RoleResourcePermissionCreate  # noqa: E501
from swagger_server.models.role_update import RoleUpdate  # noqa: E501
from swagger_server.models.site import Site  # noqa: E501
from swagger_server.models.site_create import SiteCreate  # noqa: E501
from swagger_server.models.site_role import SiteRole  # noqa: E501
from swagger_server.models.site_role_create import SiteRoleCreate  # noqa: E501
from swagger_server.models.site_role_update import SiteRoleUpdate  # noqa: E501
from swagger_server.models.site_update import SiteUpdate  # noqa: E501
from swagger_server.models.user_domain_role import UserDomainRole  # noqa: E501
from swagger_server.models.user_domain_role_create import UserDomainRoleCreate  # noqa: E501
from swagger_server.models.user_site_role import UserSiteRole  # noqa: E501
from swagger_server.models.user_site_role_create import UserSiteRoleCreate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccessControlController(BaseTestCase):
    """AccessControlController integration test stubs"""

    def test_access_control_roleresourcepermission_delete(self):
        """Test case for access_control_roleresourcepermission_delete

        
        """
        response = self.client.open(
            '/api/v1/roleresourcepermissions/{role_id}/{resource_id}/{permission_id}/'.format(role_id=56, resource_id=56, permission_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_create(self):
        """Test case for domain_create

        
        """
        data = DomainCreate()
        response = self.client.open(
            '/api/v1/domains/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_delete(self):
        """Test case for domain_delete

        
        """
        response = self.client.open(
            '/api/v1/domains/{domain_id}/'.format(domain_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_list(self):
        """Test case for domain_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('domain_ids', 56)]
        response = self.client.open(
            '/api/v1/domains/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_read(self):
        """Test case for domain_read

        
        """
        response = self.client.open(
            '/api/v1/domains/{domain_id}/'.format(domain_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_update(self):
        """Test case for domain_update

        
        """
        data = DomainUpdate()
        response = self.client.open(
            '/api/v1/domains/{domain_id}/'.format(domain_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domainrole_create(self):
        """Test case for domainrole_create

        
        """
        data = DomainRoleCreate()
        response = self.client.open(
            '/api/v1/domainroles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domainrole_delete(self):
        """Test case for domainrole_delete

        
        """
        response = self.client.open(
            '/api/v1/domainroles/{domain_id}/{role_id}/'.format(domain_id=56, role_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domainrole_list(self):
        """Test case for domainrole_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('domain_id', 56),
                        ('role_id', 56)]
        response = self.client.open(
            '/api/v1/domainroles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domainrole_read(self):
        """Test case for domainrole_read

        
        """
        response = self.client.open(
            '/api/v1/domainroles/{domain_id}/{role_id}/'.format(domain_id=56, role_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domainrole_update(self):
        """Test case for domainrole_update

        
        """
        data = DomainRoleUpdate()
        response = self.client.open(
            '/api/v1/domainroles/{domain_id}/{role_id}/'.format(domain_id=56, role_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitation_create(self):
        """Test case for invitation_create

        
        """
        data = InvitationCreate()
        response = self.client.open(
            '/api/v1/invitations/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitation_delete(self):
        """Test case for invitation_delete

        
        """
        response = self.client.open(
            '/api/v1/invitations/{invitation_id}/'.format(invitation_id='invitation_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitation_list(self):
        """Test case for invitation_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('invitor_id', 'invitor_id_example'),
                        ('invitation_ids', 56)]
        response = self.client.open(
            '/api/v1/invitations/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitation_read(self):
        """Test case for invitation_read

        
        """
        response = self.client.open(
            '/api/v1/invitations/{invitation_id}/'.format(invitation_id='invitation_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitation_update(self):
        """Test case for invitation_update

        
        """
        data = InvitationUpdate()
        response = self.client.open(
            '/api/v1/invitations/{invitation_id}/'.format(invitation_id='invitation_id_example'),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationdomainrole_create(self):
        """Test case for invitationdomainrole_create

        
        """
        data = InvitationDomainRoleCreate()
        response = self.client.open(
            '/api/v1/invitationdomainroles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationdomainrole_delete(self):
        """Test case for invitationdomainrole_delete

        
        """
        response = self.client.open(
            '/api/v1/invitationdomainroles/{invitation_id}/{domain_id}/{role_id}'.format(invitation_id='invitation_id_example', domain_id=56, role_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationdomainrole_list(self):
        """Test case for invitationdomainrole_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('invitation_id', 'invitation_id_example'),
                        ('domain_id', 56),
                        ('role_id', 56)]
        response = self.client.open(
            '/api/v1/invitationdomainroles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationdomainrole_read(self):
        """Test case for invitationdomainrole_read

        
        """
        response = self.client.open(
            '/api/v1/invitationdomainroles/{invitation_id}/{domain_id}/{role_id}'.format(invitation_id='invitation_id_example', domain_id=56, role_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationsiterole_create(self):
        """Test case for invitationsiterole_create

        
        """
        data = InvitationSiteRoleCreate()
        response = self.client.open(
            '/api/v1/invitationsiteroles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationsiterole_delete(self):
        """Test case for invitationsiterole_delete

        
        """
        response = self.client.open(
            '/api/v1/invitationsiteroles/{invitation_id}/{site_id}/{role_id}'.format(invitation_id='invitation_id_example', site_id=56, role_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationsiterole_list(self):
        """Test case for invitationsiterole_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('invitation_id', 'invitation_id_example'),
                        ('site_id', 56),
                        ('role_id', 56)]
        response = self.client.open(
            '/api/v1/invitationsiteroles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_invitationsiterole_read(self):
        """Test case for invitationsiterole_read

        
        """
        response = self.client.open(
            '/api/v1/invitationsiteroles/{invitation_id}/{site_id}/{role_id}'.format(invitation_id='invitation_id_example', site_id=56, role_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_permission_create(self):
        """Test case for permission_create

        
        """
        data = PermissionCreate()
        response = self.client.open(
            '/api/v1/permissions/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_permission_delete(self):
        """Test case for permission_delete

        
        """
        response = self.client.open(
            '/api/v1/permissions/{permission_id}/'.format(permission_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_permission_list(self):
        """Test case for permission_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('permission_ids', 56)]
        response = self.client.open(
            '/api/v1/permissions/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_permission_read(self):
        """Test case for permission_read

        
        """
        response = self.client.open(
            '/api/v1/permissions/{permission_id}/'.format(permission_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_permission_update(self):
        """Test case for permission_update

        
        """
        data = PermissionUpdate()
        response = self.client.open(
            '/api/v1/permissions/{permission_id}/'.format(permission_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resource_create(self):
        """Test case for resource_create

        
        """
        data = ResourceCreate()
        response = self.client.open(
            '/api/v1/resources/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resource_delete(self):
        """Test case for resource_delete

        
        """
        response = self.client.open(
            '/api/v1/resources/{resource_id}/'.format(resource_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resource_list(self):
        """Test case for resource_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('prefix', 'prefix_example'),
                        ('resource_ids', 56)]
        response = self.client.open(
            '/api/v1/resources/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resource_read(self):
        """Test case for resource_read

        
        """
        response = self.client.open(
            '/api/v1/resources/{resource_id}/'.format(resource_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resource_update(self):
        """Test case for resource_update

        
        """
        data = ResourceUpdate()
        response = self.client.open(
            '/api/v1/resources/{resource_id}/'.format(resource_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_role_create(self):
        """Test case for role_create

        
        """
        data = RoleCreate()
        response = self.client.open(
            '/api/v1/roles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_role_delete(self):
        """Test case for role_delete

        
        """
        response = self.client.open(
            '/api/v1/roles/{role_id}/'.format(role_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_role_list(self):
        """Test case for role_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('role_ids', 56)]
        response = self.client.open(
            '/api/v1/roles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_role_read(self):
        """Test case for role_read

        
        """
        response = self.client.open(
            '/api/v1/roles/{role_id}/'.format(role_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_role_update(self):
        """Test case for role_update

        
        """
        data = RoleUpdate()
        response = self.client.open(
            '/api/v1/roles/{role_id}/'.format(role_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_roleresourcepermission_create(self):
        """Test case for roleresourcepermission_create

        
        """
        data = RoleResourcePermissionCreate()
        response = self.client.open(
            '/api/v1/roleresourcepermissions/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_roleresourcepermission_list(self):
        """Test case for roleresourcepermission_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('role_id', 56),
                        ('resource_id', 56),
                        ('permission_id', 56)]
        response = self.client.open(
            '/api/v1/roleresourcepermissions/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_roleresourcepermission_read(self):
        """Test case for roleresourcepermission_read

        
        """
        response = self.client.open(
            '/api/v1/roleresourcepermissions/{role_id}/{resource_id}/{permission_id}/'.format(role_id=56, resource_id=56, permission_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_site_create(self):
        """Test case for site_create

        
        """
        data = SiteCreate()
        response = self.client.open(
            '/api/v1/sites/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_site_delete(self):
        """Test case for site_delete

        
        """
        response = self.client.open(
            '/api/v1/sites/{site_id}/'.format(site_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_site_list(self):
        """Test case for site_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('site_ids', 56)]
        response = self.client.open(
            '/api/v1/sites/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_site_read(self):
        """Test case for site_read

        
        """
        response = self.client.open(
            '/api/v1/sites/{site_id}/'.format(site_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_site_update(self):
        """Test case for site_update

        
        """
        data = SiteUpdate()
        response = self.client.open(
            '/api/v1/sites/{site_id}/'.format(site_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_siterole_create(self):
        """Test case for siterole_create

        
        """
        data = SiteRoleCreate()
        response = self.client.open(
            '/api/v1/siteroles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_siterole_delete(self):
        """Test case for siterole_delete

        
        """
        response = self.client.open(
            '/api/v1/siteroles/{site_id}/{role_id}/'.format(site_id=56, role_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_siterole_list(self):
        """Test case for siterole_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('site_id', 56),
                        ('role_id', 56)]
        response = self.client.open(
            '/api/v1/siteroles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_siterole_read(self):
        """Test case for siterole_read

        
        """
        response = self.client.open(
            '/api/v1/siteroles/{site_id}/{role_id}/'.format(site_id=56, role_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_siterole_update(self):
        """Test case for siterole_update

        
        """
        data = SiteRoleUpdate()
        response = self.client.open(
            '/api/v1/siteroles/{site_id}/{role_id}/'.format(site_id=56, role_id=56),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_userdomainrole_create(self):
        """Test case for userdomainrole_create

        
        """
        data = UserDomainRoleCreate()
        response = self.client.open(
            '/api/v1/userdomainroles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_userdomainrole_delete(self):
        """Test case for userdomainrole_delete

        
        """
        response = self.client.open(
            '/api/v1/userdomainroles/{user_id}/{domain_id}/{role_id}/'.format(user_id='user_id_example', domain_id=56, role_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_userdomainrole_list(self):
        """Test case for userdomainrole_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('user_id', 'user_id_example'),
                        ('domain_id', 56),
                        ('role_id', 56)]
        response = self.client.open(
            '/api/v1/userdomainroles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_userdomainrole_read(self):
        """Test case for userdomainrole_read

        
        """
        response = self.client.open(
            '/api/v1/userdomainroles/{user_id}/{domain_id}/{role_id}/'.format(user_id='user_id_example', domain_id=56, role_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usersiterole_create(self):
        """Test case for usersiterole_create

        
        """
        data = UserSiteRoleCreate()
        response = self.client.open(
            '/api/v1/usersiteroles/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usersiterole_list(self):
        """Test case for usersiterole_list

        
        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('user_id', 'user_id_example'),
                        ('site_id', 56),
                        ('role_id', 56)]
        response = self.client.open(
            '/api/v1/usersiteroles/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
