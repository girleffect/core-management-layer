# coding: utf-8

# flake8: noqa

"""
    Authentication Service API

    This is the API that will be exposed by the Authentication Service.  The Authentication Service facilitates user registration and login via web-based flows as defined for the OpenID Connect specification.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.authentication_api import AuthenticationApi
from swagger_client.api.experimental_api import ExperimentalApi
from swagger_client.api.oidc_provider_api import OidcProviderApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.address import Address
from swagger_client.models.client import Client
from swagger_client.models.content import Content
from swagger_client.models.o_auth2_error import OAuth2Error
from swagger_client.models.problem_detail import ProblemDetail
from swagger_client.models.session import Session
from swagger_client.models.token import Token
from swagger_client.models.user import User
from swagger_client.models.user_info import UserInfo
from swagger_client.models.user_update import UserUpdate
