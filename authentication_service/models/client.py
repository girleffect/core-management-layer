# coding: utf-8

"""
    Authentication Service API

    This is the API that will be exposed by the Authentication Service. The Authentication Service facilitates user registration and login via web-based flows as defined for the OpenID Connect specification.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Client(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'post_logout_redirect_uris': 'str',
        'redirect_uris': 'str',
        'client_id': 'str',
        'contact_email': 'str',
        'logo': 'str',
        'name': 'str',
        'require_consent': 'bool',
        'response_type': 'str',
        'reuse_consent': 'bool',
        'terms_url': 'str',
        'website_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'post_logout_redirect_uris': '_post_logout_redirect_uris',
        'redirect_uris': '_redirect_uris',
        'client_id': 'client_id',
        'contact_email': 'contact_email',
        'logo': 'logo',
        'name': 'name',
        'require_consent': 'require_consent',
        'response_type': 'response_type',
        'reuse_consent': 'reuse_consent',
        'terms_url': 'terms_url',
        'website_url': 'website_url'
    }

    def __init__(self, id=None, post_logout_redirect_uris=None, redirect_uris=None, client_id=None, contact_email=None, logo=None, name=None, require_consent=None, response_type=None, reuse_consent=None, terms_url=None, website_url=None):  # noqa: E501
        """Client - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._post_logout_redirect_uris = None
        self._redirect_uris = None
        self._client_id = None
        self._contact_email = None
        self._logo = None
        self._name = None
        self._require_consent = None
        self._response_type = None
        self._reuse_consent = None
        self._terms_url = None
        self._website_url = None
        self.discriminator = None

        self.id = id
        if post_logout_redirect_uris is not None:
            self.post_logout_redirect_uris = post_logout_redirect_uris
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        self.client_id = client_id
        if contact_email is not None:
            self.contact_email = contact_email
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if require_consent is not None:
            self.require_consent = require_consent
        self.response_type = response_type
        if reuse_consent is not None:
            self.reuse_consent = reuse_consent
        if terms_url is not None:
            self.terms_url = terms_url
        if website_url is not None:
            self.website_url = website_url

    @property
    def id(self):
        """Gets the id of this Client.  # noqa: E501

          # noqa: E501

        :return: The id of this Client.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Client.

          # noqa: E501

        :param id: The id of this Client.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def post_logout_redirect_uris(self):
        """Gets the post_logout_redirect_uris of this Client.  # noqa: E501

        New-line delimited list of post-logout redirect URIs  # noqa: E501

        :return: The post_logout_redirect_uris of this Client.  # noqa: E501
        :rtype: str
        """
        return self._post_logout_redirect_uris

    @post_logout_redirect_uris.setter
    def post_logout_redirect_uris(self, post_logout_redirect_uris):
        """Sets the post_logout_redirect_uris of this Client.

        New-line delimited list of post-logout redirect URIs  # noqa: E501

        :param post_logout_redirect_uris: The post_logout_redirect_uris of this Client.  # noqa: E501
        :type: str
        """

        self._post_logout_redirect_uris = post_logout_redirect_uris

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this Client.  # noqa: E501

        New-line delimited list of redirect URIs  # noqa: E501

        :return: The redirect_uris of this Client.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this Client.

        New-line delimited list of redirect URIs  # noqa: E501

        :param redirect_uris: The redirect_uris of this Client.  # noqa: E501
        :type: str
        """

        self._redirect_uris = redirect_uris

    @property
    def client_id(self):
        """Gets the client_id of this Client.  # noqa: E501

          # noqa: E501

        :return: The client_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Client.

          # noqa: E501

        :param client_id: The client_id of this Client.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def contact_email(self):
        """Gets the contact_email of this Client.  # noqa: E501

          # noqa: E501

        :return: The contact_email of this Client.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this Client.

          # noqa: E501

        :param contact_email: The contact_email of this Client.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def logo(self):
        """Gets the logo of this Client.  # noqa: E501

          # noqa: E501

        :return: The logo of this Client.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Client.

          # noqa: E501

        :param logo: The logo of this Client.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this Client.  # noqa: E501

          # noqa: E501

        :return: The name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Client.

          # noqa: E501

        :param name: The name of this Client.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def require_consent(self):
        """Gets the require_consent of this Client.  # noqa: E501

        If disabled, the Server will NEVER ask the user for consent.  # noqa: E501

        :return: The require_consent of this Client.  # noqa: E501
        :rtype: bool
        """
        return self._require_consent

    @require_consent.setter
    def require_consent(self, require_consent):
        """Sets the require_consent of this Client.

        If disabled, the Server will NEVER ask the user for consent.  # noqa: E501

        :param require_consent: The require_consent of this Client.  # noqa: E501
        :type: bool
        """

        self._require_consent = require_consent

    @property
    def response_type(self):
        """Gets the response_type of this Client.  # noqa: E501

          # noqa: E501

        :return: The response_type of this Client.  # noqa: E501
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this Client.

          # noqa: E501

        :param response_type: The response_type of this Client.  # noqa: E501
        :type: str
        """
        if response_type is None:
            raise ValueError("Invalid value for `response_type`, must not be `None`")  # noqa: E501

        self._response_type = response_type

    @property
    def reuse_consent(self):
        """Gets the reuse_consent of this Client.  # noqa: E501

        If enabled, the Server will save the user consent given to a specific client, so that user won't be prompted for the same authorization multiple times.  # noqa: E501

        :return: The reuse_consent of this Client.  # noqa: E501
        :rtype: bool
        """
        return self._reuse_consent

    @reuse_consent.setter
    def reuse_consent(self, reuse_consent):
        """Sets the reuse_consent of this Client.

        If enabled, the Server will save the user consent given to a specific client, so that user won't be prompted for the same authorization multiple times.  # noqa: E501

        :param reuse_consent: The reuse_consent of this Client.  # noqa: E501
        :type: bool
        """

        self._reuse_consent = reuse_consent

    @property
    def terms_url(self):
        """Gets the terms_url of this Client.  # noqa: E501

        External reference to the privacy policy of the client.  # noqa: E501

        :return: The terms_url of this Client.  # noqa: E501
        :rtype: str
        """
        return self._terms_url

    @terms_url.setter
    def terms_url(self, terms_url):
        """Sets the terms_url of this Client.

        External reference to the privacy policy of the client.  # noqa: E501

        :param terms_url: The terms_url of this Client.  # noqa: E501
        :type: str
        """

        self._terms_url = terms_url

    @property
    def website_url(self):
        """Gets the website_url of this Client.  # noqa: E501

          # noqa: E501

        :return: The website_url of this Client.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this Client.

          # noqa: E501

        :param website_url: The website_url of this Client.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
