"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
import management_layer.api.views as views
import aiohttp_cors

def add_routes(app, with_ui=False):
    app.router.add_view(r"/usersiteroles/{user_id}/{site_id}/{role_id}", views.UsersiterolesUserIdSiteIdRoleId)
    app.router.add_view(r"/usersiteroles", views.Usersiteroles)
    app.router.add_view(r"/usersitedata/{user_id}/{site_id}", views.UsersitedataUserIdSiteId)
    app.router.add_view(r"/usersitedata", views.Usersitedata)
    app.router.add_view(r"/users/{user_id}/deactivate", views.UsersUserIdDeactivate)
    app.router.add_view(r"/users/{user_id}/activate", views.UsersUserIdActivate)
    app.router.add_view(r"/users/{user_id}", views.UsersUserId)
    app.router.add_view(r"/users", views.Users)
    app.router.add_view(r"/userdomainroles/{user_id}/{domain_id}/{role_id}", views.UserdomainrolesUserIdDomainIdRoleId)
    app.router.add_view(r"/userdomainroles", views.Userdomainroles)
    app.router.add_view(r"/sites/{site_id}/deactivate", views.SitesSiteIdDeactivate)
    app.router.add_view(r"/sites/{site_id}/activate", views.SitesSiteIdActivate)
    app.router.add_view(r"/sites/{site_id}", views.SitesSiteId)
    app.router.add_view(r"/sites", views.Sites)
    app.router.add_view(r"/siteroles/{site_id}/{role_id}", views.SiterolesSiteIdRoleId)
    app.router.add_view(r"/siteroles", views.Siteroles)
    app.router.add_view(r"/sitedataschemas/{site_id}", views.SitedataschemasSiteId)
    app.router.add_view(r"/sitedataschemas", views.Sitedataschemas)
    app.router.add_view(r"/roles/{role_id}", views.RolesRoleId)
    app.router.add_view(r"/roles", views.Roles)
    app.router.add_view(r"/roleresourcepermissions/{role_id}/{resource_id}/{permission_id}", views.RoleresourcepermissionsRoleIdResourceIdPermissionId)
    app.router.add_view(r"/roleresourcepermissions", views.Roleresourcepermissions)
    app.router.add_view(r"/resources/{resource_id}", views.ResourcesResourceId)
    app.router.add_view(r"/resources", views.Resources)
    app.router.add_view(r"/refresh/sites", views.RefreshSites)
    app.router.add_view(r"/refresh/roles", views.RefreshRoles)
    app.router.add_view(r"/refresh/resources", views.RefreshResources)
    app.router.add_view(r"/refresh/permissions", views.RefreshPermissions)
    app.router.add_view(r"/refresh/keys", views.RefreshKeys)
    app.router.add_view(r"/refresh/domains", views.RefreshDomains)
    app.router.add_view(r"/refresh/clients", views.RefreshClients)
    app.router.add_view(r"/refresh/all", views.RefreshAll)
    app.router.add_view(r"/permissions/{permission_id}", views.PermissionsPermissionId)
    app.router.add_view(r"/permissions", views.Permissions)
    app.router.add_view(r"/organisationalunits/{organisational_unit_id}", views.OrganisationalunitsOrganisationalUnitId)
    app.router.add_view(r"/organisationalunits", views.Organisationalunits)
    app.router.add_view(r"/ops/users_with_roles_for_site/{site_id}", views.OpsUsersWithRolesForSiteSiteId)
    app.router.add_view(r"/ops/users_with_roles_for_domain/{domain_id}", views.OpsUsersWithRolesForDomainDomainId)
    app.router.add_view(r"/ops/user_site_role_labels_aggregated/{user_id}/{site_id}", views.OpsUserSiteRoleLabelsAggregatedUserIdSiteId)
    app.router.add_view(r"/ops/user_management_portal_permissions/{user_id}", views.OpsUserManagementPortalPermissionsUserId)
    app.router.add_view(r"/ops/user_has_permissions/{user_id}", views.OpsUserHasPermissionsUserId)
    app.router.add_view(r"/ops/site_role_labels_aggregated/{site_id}", views.OpsSiteRoleLabelsAggregatedSiteId)
    app.router.add_view(r"/ops/site_and_domain_roles/{site_id}", views.OpsSiteAndDomainRolesSiteId)
    app.router.add_view(r"/ops/domain_roles/{domain_id}", views.OpsDomainRolesDomainId)
    app.router.add_view(r"/ops/all_user_roles/{user_id}", views.OpsAllUserRolesUserId)
    app.router.add_view(r"/invitationsiteroles/{invitation_id}/{site_id}/{role_id}", views.InvitationsiterolesInvitationIdSiteIdRoleId)
    app.router.add_view(r"/invitationsiteroles", views.Invitationsiteroles)
    app.router.add_view(r"/invitations/{invitation_id}", views.InvitationsInvitationId)
    app.router.add_view(r"/invitations", views.Invitations)
    app.router.add_view(r"/invitationdomainroles/{invitation_id}/{domain_id}/{role_id}", views.InvitationdomainrolesInvitationIdDomainIdRoleId)
    app.router.add_view(r"/invitationdomainroles", views.Invitationdomainroles)
    app.router.add_view(r"/domains/{domain_id}", views.DomainsDomainId)
    app.router.add_view(r"/domains", views.Domains)
    app.router.add_view(r"/domainroles/{domain_id}/{role_id}", views.DomainrolesDomainIdRoleId)
    app.router.add_view(r"/domainroles", views.Domainroles)
    app.router.add_view(r"/countries/{country_code}", views.CountriesCountryCode)
    app.router.add_view(r"/countries", views.Countries)
    app.router.add_view(r"/clients/{client_id}", views.ClientsClientId)
    app.router.add_view(r"/clients", views.Clients)
    app.router.add_view(r"/adminnotes/{admin_note_id}", views.AdminnotesAdminNoteId)
    app.router.add_view(r"/adminnotes", views.Adminnotes)
    if with_ui:
        app.router.add_view(r"/the_specification", views.__SWAGGER_SPEC__)
        app.router.add_static(r"/ui", path="ui")

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in app.router.routes():
        cors.add(route)