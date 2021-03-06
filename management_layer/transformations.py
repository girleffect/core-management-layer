from datetime import datetime, date

from management_layer.transformation import Transformation, Mapping


def datetime_to_string(x: datetime) -> str:
    return x.strftime("%Y-%m-%dT%H:%M:%SZ")


def date_to_string(x: date) -> str:
    return x.strftime("%Y-%m-%d")


ADMIN_NOTE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "user_id", "creator_id", "note"]
)

COUNTRY = Transformation(
    copy_fields=["code", "name"]
)

CREDENTIALS = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "site_id", "account_id", "account_secret", "description"]
)

DOMAIN = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "parent_id", "name", "description"]
)

DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["domain_id", "role_id", "grant_implicitly"]
)

INVITATION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("expires_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "first_name", "last_name", "email",
                 "invitor_id", "organisation_id",
                 "invitation_redirect_url_id"]
)

INVITATION_REDIRECT_URL = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
    ],
    copy_fields=["id", "url", "description"]
)

INVITATION_DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["invitation_id", "domain_id", "role_id"]
)

INVITATION_SITE_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["invitation_id", "site_id", "role_id"]
)

ORGANISATION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "name", "description"]
)

PERMISSION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "name", "description"]
)

RESOURCE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "urn", "description"]
)

ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "label", "description", "requires_2fa"]
)

ROLE_RESOURCE_PERMISSION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["role_id", "resource_id", "permission_id"]
)

SITE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "name", "domain_id", "description",
                 "client_id", "is_active", "deletion_method_id", "deletion_method_data"]
)

SITE_DATA_SCHEMA = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["site_id", "schema"]
)

SITE_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["site_id", "role_id", "grant_implicitly"]
)

USER_DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "domain_id", "role_id"]
)

USER_SITE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("consented_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "user_id", "site_id"]
)

USER_SITE_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "site_id", "role_id"]
)

USER_SITE_DATA = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("consented_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "site_id", "data", "blocked"]
)

CLIENT = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "_post_logout_redirect_uris", "_redirect_uris",
                 "client_id", "contact_email", "logo", "name",
                 "require_consent", "response_type", "reuse_consent",
                 "terms_url", "website_url"]
)

USER = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        # The `date_joined` field has a datetime type, despite its name. It is a Django field and
        # was left as is.
        Mapping("date_joined", conversion=datetime_to_string),
        Mapping("last_login", conversion=datetime_to_string),
        Mapping("birth_date", conversion=date_to_string)
    ],
    copy_fields=["id", "username", "first_name", "last_name", "email",
                 "is_active", "email_verified", "msisdn_verified", "msisdn",
                 "gender", "avatar", "country_code", "organisation_id"]
)

DELETED_USER = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("deleted_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "username", "email", "msisdn", "reason", "deleter_id"]
)

DELETED_USER_SITE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("deletion_requested_at", conversion=datetime_to_string),
        Mapping("deletion_confirmed_at", conversion=datetime_to_string)
    ],
    copy_fields=["deleted_user_id", "site_id", "deletion_requested_via", "deletion_confirmed_via"]
)

DELETION_METHOD = Transformation(
    mappings=[
        Mapping(input_field="created_at", conversion=datetime_to_string),
        Mapping(input_field="updated_at", conversion=datetime_to_string)
    ],
    copy_fields=[
        "id", "label", "data_schema", "description"
    ]
)
