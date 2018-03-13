# coding: utf-8

"""
    Access Control API

    # The Access Control API  ## Overview The Access Control API is an API exposed to other core components. It uses an API Key in an HTTP header to perform authentication and authorisation.  Most of the API calls facilitates CRUD of the entities defined in the Access Control component. Others calls allows the retrieval of information in a form that is convenient for other components (most notably the Management Layer) to consume.   # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SiteUpdate(object):
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
        'client_id': 'str',
        'domain_id': 'int',
        'name': 'str',
        'description': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'client_id': 'client_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'description': 'description',
        'is_active': 'is_active'
    }

    def __init__(self, client_id=None, domain_id=None, name=None, description=None, is_active=None):  # noqa: E501
        """SiteUpdate - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._domain_id = None
        self._name = None
        self._description = None
        self._is_active = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_active is not None:
            self.is_active = is_active

    @property
    def client_id(self):
        """Gets the client_id of this SiteUpdate.  # noqa: E501


        :return: The client_id of this SiteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SiteUpdate.


        :param client_id: The client_id of this SiteUpdate.  # noqa: E501
        :type: str
        """
        if client_id is not None and len(client_id) > 255:
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `255`")  # noqa: E501

        self._client_id = client_id

    @property
    def domain_id(self):
        """Gets the domain_id of this SiteUpdate.  # noqa: E501


        :return: The domain_id of this SiteUpdate.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SiteUpdate.


        :param domain_id: The domain_id of this SiteUpdate.  # noqa: E501
        :type: int
        """

        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this SiteUpdate.  # noqa: E501


        :return: The name of this SiteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteUpdate.


        :param name: The name of this SiteUpdate.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 30:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this SiteUpdate.  # noqa: E501


        :return: The description of this SiteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SiteUpdate.


        :param description: The description of this SiteUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_active(self):
        """Gets the is_active of this SiteUpdate.  # noqa: E501


        :return: The is_active of this SiteUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this SiteUpdate.


        :param is_active: The is_active of this SiteUpdate.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if not isinstance(other, SiteUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
