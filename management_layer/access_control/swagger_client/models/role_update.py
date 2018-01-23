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


class RoleUpdate(object):
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
        'label': 'str',
        'is_admin_role': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'label': 'label',
        'is_admin_role': 'is_admin_role',
        'description': 'description'
    }

    def __init__(self, label=None, is_admin_role=None, description=None):  # noqa: E501
        """RoleUpdate - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._is_admin_role = None
        self._description = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if is_admin_role is not None:
            self.is_admin_role = is_admin_role
        if description is not None:
            self.description = description

    @property
    def label(self):
        """Gets the label of this RoleUpdate.  # noqa: E501


        :return: The label of this RoleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this RoleUpdate.


        :param label: The label of this RoleUpdate.  # noqa: E501
        :type: str
        """
        if label is not None and len(label) > 100:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `100`")  # noqa: E501

        self._label = label

    @property
    def is_admin_role(self):
        """Gets the is_admin_role of this RoleUpdate.  # noqa: E501


        :return: The is_admin_role of this RoleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin_role

    @is_admin_role.setter
    def is_admin_role(self, is_admin_role):
        """Sets the is_admin_role of this RoleUpdate.


        :param is_admin_role: The is_admin_role of this RoleUpdate.  # noqa: E501
        :type: bool
        """

        self._is_admin_role = is_admin_role

    @property
    def description(self):
        """Gets the description of this RoleUpdate.  # noqa: E501


        :return: The description of this RoleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleUpdate.


        :param description: The description of this RoleUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, RoleUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
