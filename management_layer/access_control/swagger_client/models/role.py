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

from swagger_client.models.role_label import RoleLabel  # noqa: F401,E501


class Role(object):
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
        'label': 'RoleLabel',
        'is_admin_role': 'bool',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'is_admin_role': 'is_admin_role',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, label=None, is_admin_role=None, description=None, created_at=None, updated_at=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._label = None
        self._is_admin_role = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.label = label
        self.is_admin_role = is_admin_role
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501


        :return: The id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.


        :param id: The id of this Role.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this Role.  # noqa: E501


        :return: The label of this Role.  # noqa: E501
        :rtype: RoleLabel
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Role.


        :param label: The label of this Role.  # noqa: E501
        :type: RoleLabel
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def is_admin_role(self):
        """Gets the is_admin_role of this Role.  # noqa: E501


        :return: The is_admin_role of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin_role

    @is_admin_role.setter
    def is_admin_role(self, is_admin_role):
        """Sets the is_admin_role of this Role.


        :param is_admin_role: The is_admin_role of this Role.  # noqa: E501
        :type: bool
        """
        if is_admin_role is None:
            raise ValueError("Invalid value for `is_admin_role`, must not be `None`")  # noqa: E501

        self._is_admin_role = is_admin_role

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501


        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.


        :param description: The description of this Role.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Role.  # noqa: E501


        :return: The created_at of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Role.


        :param created_at: The created_at of this Role.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Role.  # noqa: E501


        :return: The updated_at of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Role.


        :param updated_at: The updated_at of this Role.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
