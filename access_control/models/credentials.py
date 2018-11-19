# coding: utf-8

"""
    Access Control API

    # The Access Control API  ## Overview The Access Control API is an API exposed to other core components. It uses an API Key in an HTTP header to perform authentication and authorisation.  Most of the API calls facilitates CRUD of the entities defined in the Access Control component. Others calls allows the retrieval of information in a form that is convenient for other components (most notably the Management Layer) to consume.   # noqa: E501

    OpenAPI spec version: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Credentials(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'site_id': 'int',
        'account_id': 'str',
        'account_secret': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'site_id': 'site_id',
        'account_id': 'account_id',
        'account_secret': 'account_secret',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, site_id=None, account_id=None, account_secret=None, description=None, created_at=None, updated_at=None):  # noqa: E501
        """Credentials - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._site_id = None
        self._account_id = None
        self._account_secret = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.site_id = site_id
        self.account_id = account_id
        self.account_secret = account_secret
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Credentials.  # noqa: E501


        :return: The id of this Credentials.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Credentials.


        :param id: The id of this Credentials.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def site_id(self):
        """Gets the site_id of this Credentials.  # noqa: E501


        :return: The site_id of this Credentials.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Credentials.


        :param site_id: The site_id of this Credentials.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def account_id(self):
        """Gets the account_id of this Credentials.  # noqa: E501


        :return: The account_id of this Credentials.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Credentials.


        :param account_id: The account_id of this Credentials.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if account_id is not None and len(account_id) > 256:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `256`")  # noqa: E501
        if account_id is not None and len(account_id) < 32:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `32`")  # noqa: E501

        self._account_id = account_id

    @property
    def account_secret(self):
        """Gets the account_secret of this Credentials.  # noqa: E501


        :return: The account_secret of this Credentials.  # noqa: E501
        :rtype: str
        """
        return self._account_secret

    @account_secret.setter
    def account_secret(self, account_secret):
        """Sets the account_secret of this Credentials.


        :param account_secret: The account_secret of this Credentials.  # noqa: E501
        :type: str
        """
        if account_secret is None:
            raise ValueError("Invalid value for `account_secret`, must not be `None`")  # noqa: E501
        if account_secret is not None and len(account_secret) > 256:
            raise ValueError("Invalid value for `account_secret`, length must be less than or equal to `256`")  # noqa: E501
        if account_secret is not None and len(account_secret) < 32:
            raise ValueError("Invalid value for `account_secret`, length must be greater than or equal to `32`")  # noqa: E501

        self._account_secret = account_secret

    @property
    def description(self):
        """Gets the description of this Credentials.  # noqa: E501


        :return: The description of this Credentials.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Credentials.


        :param description: The description of this Credentials.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Credentials.  # noqa: E501


        :return: The created_at of this Credentials.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Credentials.


        :param created_at: The created_at of this Credentials.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Credentials.  # noqa: E501


        :return: The updated_at of this Credentials.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Credentials.


        :param updated_at: The updated_at of this Credentials.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Credentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other