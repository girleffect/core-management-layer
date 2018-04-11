"""
Do not modify this file. It is generated from the Swagger specification.

Container module for JSONSchema definitions.
This does not include inlined definitions.

The pretty-printing functionality provided by the json module is superior to
what is provided by pformat, hence the use of json.loads().
"""
import json

# When no schema is provided in the definition, we use an empty schema
__UNSPECIFIED__ = {}

admin_note = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "creator_id": {
            "description": "The user making the request will be considered the creator and thus this field is not available when creating admin note.",
            "format": "uuid",
            "readOnly": true,
            "type": "string",
            "x-related-info": {
                "label": "username",
                "model": "user"
            }
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "note": {
            "type": "string"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "id",
        "user_id",
        "creator_id",
        "note",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

admin_note_create = json.loads("""
{
    "properties": {
        "creator_id": {
            "description": "The user making the request will be considered the creator and thus this field is not available when creating admin note.",
            "format": "uuid",
            "readOnly": true,
            "type": "string",
            "x-related-info": {
                "label": "username",
                "model": "user"
            }
        },
        "note": {
            "type": "string"
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "creator_id",
        "note"
    ],
    "type": "object"
}
""")

admin_note_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "note": {
            "type": "string"
        }
    },
    "type": "object"
}
""")

all_user_roles = json.loads("""
{
    "description": "An object containing the effective roles that a user has in any place in the organisational tree.",
    "properties": {
        "roles_map": {
            "additionalProperties": {
                "items": {
                    "type": "integer"
                },
                "type": "array"
            },
            "description": "Domain and site roles",
            "example": {
                "d:1": [
                    1
                ],
                "d:2": [
                    1,
                    2
                ],
                "s:1": [
                    1,
                    2,
                    3
                ]
            },
            "type": "object"
        },
        "user_id": {
            "format": "uuid",
            "type": "string"
        }
    },
    "required": [
        "user_id",
        "roles_map"
    ],
    "type": "object"
}
""")

client = json.loads("""
{
    "properties": {
        "_post_logout_redirect_uris": {
            "description": "New-line delimited list of post-logout redirect URIs",
            "type": "string"
        },
        "_redirect_uris": {
            "description": "New-line delimited list of redirect URIs",
            "type": "string"
        },
        "client_id": {
            "description": "",
            "type": "string",
            "x-related-info": {
                "model": null
            }
        },
        "contact_email": {
            "description": "",
            "type": "string"
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "logo": {
            "description": "",
            "format": "uri",
            "type": "string"
        },
        "name": {
            "description": "",
            "type": "string"
        },
        "require_consent": {
            "description": "If disabled, the Server will NEVER ask the user for consent.",
            "type": "boolean"
        },
        "response_type": {
            "description": "",
            "type": "string"
        },
        "reuse_consent": {
            "description": "If enabled, the Server will save the user consent given to a specific client, so that user will not be prompted for the same authorization multiple times.",
            "type": "boolean"
        },
        "terms_url": {
            "description": "External reference to the privacy policy of the client.",
            "type": "string"
        },
        "website_url": {
            "description": "",
            "type": "string"
        }
    },
    "required": [
        "id",
        "client_id",
        "response_type"
    ],
    "type": "object"
}
""")

domain = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "name": {
            "maxLength": 100,
            "type": "string"
        },
        "parent_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name",
                "model": "domain"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "id",
        "name",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

domain_create = json.loads("""
{
    "properties": {
        "description": {
            "type": "string"
        },
        "name": {
            "maxLength": 100,
            "type": "string"
        },
        "parent_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name",
                "model": "domain"
            }
        }
    },
    "required": [
        "name"
    ],
    "type": "object"
}
""")

domain_role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "grant_implicitly": {
            "type": "boolean"
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "domain_id",
        "role_id",
        "grant_implicitly",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

domain_role_create = json.loads("""
{
    "properties": {
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "grant_implicitly": {
            "type": "boolean"
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        }
    },
    "required": [
        "domain_id",
        "role_id"
    ],
    "type": "object"
}
""")

domain_role_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "grant_implicitly": {
            "type": "boolean"
        }
    },
    "type": "object"
}
""")

domain_roles = json.loads("""
{
    "description": "An object containing the domain roles defined for a given domain and its lineage.",
    "properties": {
        "domain_id": {
            "description": "The domain for which the request was made.",
            "type": "integer"
        },
        "roles_map": {
            "additionalProperties": {
                "description": "The list of role ids for the domain",
                "items": {
                    "type": "integer"
                },
                "type": "array"
            },
            "description": "A dictionary where the keys are domain ids prefixed with `d:` and the values are lists of role ids.",
            "example": {
                "d:1": [
                    1
                ],
                "d:2": [
                    1,
                    2
                ]
            },
            "type": "object"
        }
    },
    "required": [
        "domain_id",
        "roles_map"
    ],
    "type": "object"
}
""")

domain_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "description": {
            "type": "string"
        },
        "name": {
            "maxLength": 100,
            "type": "string"
        },
        "parent_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name",
                "model": "domain"
            }
        }
    },
    "type": "object"
}
""")

invitation = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "email": {
            "format": "email",
            "type": "string"
        },
        "expires_at": {
            "format": "date-time",
            "type": "string"
        },
        "first_name": {
            "maxLength": 100,
            "type": "string"
        },
        "id": {
            "format": "uuid",
            "readOnly": true,
            "type": "string"
        },
        "invitor_id": {
            "description": "The user that created the invitation",
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username",
                "model": "user"
            }
        },
        "last_name": {
            "maxLength": 100,
            "type": "string"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "id",
        "invitor_id",
        "first_name",
        "last_name",
        "email",
        "expires_at",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

invitation_create = json.loads("""
{
    "properties": {
        "email": {
            "format": "email",
            "type": "string"
        },
        "expires_at": {
            "format": "date-time",
            "type": "string"
        },
        "first_name": {
            "maxLength": 100,
            "type": "string"
        },
        "invitor_id": {
            "description": "The user that created the invitation",
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username",
                "model": "user"
            }
        },
        "last_name": {
            "maxLength": 100,
            "type": "string"
        }
    },
    "required": [
        "invitor_id",
        "first_name",
        "last_name",
        "email"
    ],
    "type": "object"
}
""")

invitation_domain_role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "invitation_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "email"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "invitation_id",
        "domain_id",
        "role_id",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

invitation_domain_role_create = json.loads("""
{
    "properties": {
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "invitation_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "email"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        }
    },
    "required": [
        "invitation_id",
        "domain_id",
        "role_id"
    ],
    "type": "object"
}
""")

invitation_site_role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "invitation_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "email"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "invitation_id",
        "site_id",
        "role_id",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

invitation_site_role_create = json.loads("""
{
    "properties": {
        "invitation_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "email"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        }
    },
    "required": [
        "invitation_id",
        "site_id",
        "role_id"
    ],
    "type": "object"
}
""")

invitation_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "email": {
            "format": "email",
            "type": "string"
        },
        "expires_at": {
            "format": "date-time",
            "type": "string"
        },
        "first_name": {
            "maxLength": 100,
            "type": "string"
        },
        "last_name": {
            "maxLength": 100,
            "type": "string"
        }
    },
    "type": "object"
}
""")

permission = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "name": {
            "maxLength": 50,
            "type": "string"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "id",
        "name",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

permission_create = json.loads("""
{
    "properties": {
        "description": {
            "type": "string"
        },
        "name": {
            "maxLength": 50,
            "type": "string"
        }
    },
    "required": [
        "name"
    ],
    "type": "object"
}
""")

permission_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "description": {
            "type": "string"
        },
        "name": {
            "maxLength": 50,
            "type": "string"
        }
    },
    "type": "object"
}
""")

resource = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "urn": {
            "format": "uri",
            "type": "string"
        }
    },
    "required": [
        "id",
        "urn",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

resource_create = json.loads("""
{
    "properties": {
        "description": {
            "type": "string"
        },
        "urn": {
            "format": "uri",
            "type": "string"
        }
    },
    "required": [
        "urn"
    ],
    "type": "object"
}
""")

resource_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "description": {
            "type": "string"
        },
        "urn": {
            "format": "uri",
            "type": "string"
        }
    },
    "type": "object"
}
""")

role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "label": {
            "maxLength": 100,
            "type": "string",
            "x-scope": [
                "",
                "#/definitions/role"
            ]
        },
        "requires_2fa": {
            "type": "boolean"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "id",
        "label",
        "requires_2fa",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

role_create = json.loads("""
{
    "properties": {
        "description": {
            "type": "string"
        },
        "label": {
            "maxLength": 100,
            "type": "string",
            "x-scope": [
                "",
                "#/definitions/role_create"
            ]
        },
        "requires_2fa": {
            "type": "boolean"
        }
    },
    "required": [
        "label",
        "requires_2fa"
    ],
    "type": "object"
}
""")

role_label = json.loads("""
{
    "maxLength": 100,
    "type": "string"
}
""")

role_resource_permission = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "permission_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "resource_id": {
            "type": "integer",
            "x-related-info": {
                "label": "urn"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "role_id",
        "resource_id",
        "permission_id",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

role_resource_permission_create = json.loads("""
{
    "properties": {
        "permission_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "resource_id": {
            "type": "integer",
            "x-related-info": {
                "label": "urn"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        }
    },
    "required": [
        "role_id",
        "resource_id",
        "permission_id"
    ],
    "type": "object"
}
""")

role_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "description": {
            "type": "string"
        },
        "label": {
            "maxLength": 100,
            "type": "string"
        },
        "requires_2fa": {
            "type": "boolean"
        }
    },
    "type": "object"
}
""")

site = json.loads("""
{
    "properties": {
        "client_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "name"
            }
        },
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "id": {
            "readOnly": true,
            "type": "integer"
        },
        "is_active": {
            "type": "boolean"
        },
        "name": {
            "maxLength": 100,
            "type": "string"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "id",
        "domain_id",
        "name",
        "is_active",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

site_and_domain_roles = json.loads("""
{
    "description": "An object containing the site- and domain lineage roles defined for a given site.",
    "properties": {
        "roles_map": {
            "additionalProperties": {
                "description": "The list of role ids for the site or domain",
                "items": {
                    "type": "integer"
                },
                "type": "array"
            },
            "description": "A dictionary where the keys are site and domain ids prefixed with `s:` and `d:`, respectively and the values are lists of role ids.",
            "example": {
                "d:1": [
                    1
                ],
                "d:2": [
                    1,
                    2
                ],
                "s:1": [
                    1,
                    2,
                    3
                ]
            },
            "type": "object"
        },
        "site_id": {
            "description": "The site for which the request was made.",
            "type": "integer"
        }
    },
    "required": [
        "site_id",
        "roles_map"
    ],
    "type": "object"
}
""")

site_create = json.loads("""
{
    "properties": {
        "client_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "name"
            }
        },
        "description": {
            "type": "string"
        },
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "is_active": {
            "type": "boolean"
        },
        "name": {
            "maxLength": 100,
            "type": "string"
        }
    },
    "required": [
        "domain_id",
        "name"
    ],
    "type": "object"
}
""")

site_data_schema = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "schema": {
            "type": "object"
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "site_id",
        "schema",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

site_data_schema_create = json.loads("""
{
    "properties": {
        "schema": {
            "type": "object"
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        }
    },
    "required": [
        "site_id",
        "schema"
    ],
    "type": "object"
}
""")

site_data_schema_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "schema": {
            "type": "object"
        }
    },
    "type": "object"
}
""")

site_role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "grant_implicitly": {
            "type": "boolean"
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "site_id",
        "role_id",
        "grant_implicitly",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

site_role_create = json.loads("""
{
    "properties": {
        "grant_implicitly": {
            "type": "boolean"
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        }
    },
    "required": [
        "site_id",
        "role_id"
    ],
    "type": "object"
}
""")

site_role_labels_aggregated = json.loads("""
{
    "description": "An object containing a site ID and an aggregated list of all the role labels supported by the site and all the domains in its lineage.",
    "properties": {
        "roles": {
            "items": {
                "maxLength": 100,
                "type": "string",
                "x-scope": [
                    "",
                    "#/definitions/site_role_labels_aggregated"
                ]
            },
            "type": "array"
        },
        "site_id": {
            "type": "integer"
        }
    },
    "type": "object"
}
""")

site_role_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "grant_implicitly": {
            "type": "boolean"
        }
    },
    "type": "object"
}
""")

site_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "client_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "name"
            }
        },
        "description": {
            "type": "string"
        },
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "is_active": {
            "type": "boolean"
        },
        "name": {
            "maxLength": 100,
            "type": "string"
        }
    },
    "type": "object"
}
""")

user = json.loads("""
{
    "properties": {
        "avatar": {
            "format": "uri",
            "type": "string"
        },
        "birth_date": {
            "format": "date",
            "type": "string"
        },
        "country_code": {
            "maxLength": 2,
            "minLength": 2,
            "type": "string"
        },
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "date_joined": {
            "description": "",
            "format": "date",
            "readOnly": true,
            "type": "string"
        },
        "email": {
            "description": "",
            "format": "email",
            "type": "string"
        },
        "email_verified": {
            "type": "boolean"
        },
        "first_name": {
            "description": "",
            "type": "string"
        },
        "gender": {
            "type": "string"
        },
        "id": {
            "description": "The UUID of the user",
            "format": "uuid",
            "readOnly": true,
            "type": "string"
        },
        "is_active": {
            "description": "Designates whether this user should be treated as active. Deselect this instead of deleting accounts.",
            "type": "boolean"
        },
        "last_login": {
            "description": "",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "last_name": {
            "description": "",
            "type": "string"
        },
        "msisdn": {
            "maxLength": 15,
            "type": "string"
        },
        "msisdn_verified": {
            "type": "boolean"
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "username": {
            "description": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "readOnly": true,
            "type": "string"
        }
    },
    "required": [
        "id",
        "username",
        "is_active",
        "date_joined",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

user_domain_role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "domain_id",
        "role_id",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

user_domain_role_create = json.loads("""
{
    "properties": {
        "domain_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "domain_id",
        "role_id"
    ],
    "type": "object"
}
""")

user_site_data = json.loads("""
{
    "properties": {
        "blocked": {
            "type": "boolean"
        },
        "consented_at": {
            "format": "date-time",
            "type": "string"
        },
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "data": {
            "type": "object"
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "site_id",
        "consented_at",
        "blocked",
        "data",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

user_site_data_create = json.loads("""
{
    "properties": {
        "blocked": {
            "type": "boolean"
        },
        "consented_at": {
            "format": "date-time",
            "type": "string"
        },
        "data": {
            "type": "object"
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "site_id",
        "data"
    ],
    "type": "object"
}
""")

user_site_data_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "blocked": {
            "type": "boolean"
        },
        "consented_at": {
            "format": "date-time",
            "type": "string"
        },
        "data": {
            "type": "object"
        }
    },
    "type": "object"
}
""")

user_site_role = json.loads("""
{
    "properties": {
        "created_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "updated_at": {
            "format": "date-time",
            "readOnly": true,
            "type": "string"
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "site_id",
        "role_id",
        "created_at",
        "updated_at"
    ],
    "type": "object"
}
""")

user_site_role_create = json.loads("""
{
    "properties": {
        "role_id": {
            "type": "integer",
            "x-related-info": {
                "label": "label"
            }
        },
        "site_id": {
            "type": "integer",
            "x-related-info": {
                "label": "name"
            }
        },
        "user_id": {
            "format": "uuid",
            "type": "string",
            "x-related-info": {
                "label": "username"
            }
        }
    },
    "required": [
        "user_id",
        "site_id",
        "role_id"
    ],
    "type": "object"
}
""")

user_site_role_labels_aggregated = json.loads("""
{
    "description": "An object containing a user ID, site ID and an aggregated list of all the role labels assigned to the user for the site and all the domains in its lineage.",
    "properties": {
        "roles": {
            "items": {
                "maxLength": 100,
                "type": "string",
                "x-scope": [
                    "",
                    "#/definitions/user_site_role_labels_aggregated"
                ]
            },
            "type": "array"
        },
        "site_id": {
            "type": "integer"
        },
        "user_id": {
            "format": "uuid",
            "type": "string"
        }
    },
    "type": "object"
}
""")

user_update = json.loads("""
{
    "minProperties": 1,
    "properties": {
        "avatar": {
            "format": "uri",
            "type": "string"
        },
        "birth_date": {
            "format": "date",
            "type": "string"
        },
        "country_code": {
            "maxLength": 2,
            "minLength": 2,
            "type": "string"
        },
        "email": {
            "description": "",
            "format": "email",
            "type": "string"
        },
        "email_verified": {
            "type": "boolean"
        },
        "first_name": {
            "description": "",
            "type": "string"
        },
        "gender": {
            "type": "string"
        },
        "is_active": {
            "description": "Designates whether this user should be treated as active. Deselect this instead of deleting accounts.",
            "type": "boolean"
        },
        "last_name": {
            "description": "",
            "type": "string"
        },
        "msisdn": {
            "maxLength": 15,
            "type": "string"
        },
        "msisdn_verified": {
            "type": "boolean"
        }
    },
    "type": "object"
}
""")

