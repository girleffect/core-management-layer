# coding: utf-8

"""
    User Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UserSiteDataCreate(object):
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
        'user_id': 'str',
        'site_id': 'int',
        'data': 'object'
    }

    attribute_map = {
        'user_id': 'user_id',
        'site_id': 'site_id',
        'data': 'data'
    }

    def __init__(self, user_id=None, site_id=None, data=None):  # noqa: E501
        """UserSiteDataCreate - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._site_id = None
        self._data = None
        self.discriminator = None

        self.user_id = user_id
        self.site_id = site_id
        self.data = data

    @property
    def user_id(self):
        """Gets the user_id of this UserSiteDataCreate.  # noqa: E501


        :return: The user_id of this UserSiteDataCreate.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserSiteDataCreate.


        :param user_id: The user_id of this UserSiteDataCreate.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def site_id(self):
        """Gets the site_id of this UserSiteDataCreate.  # noqa: E501


        :return: The site_id of this UserSiteDataCreate.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this UserSiteDataCreate.


        :param site_id: The site_id of this UserSiteDataCreate.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def data(self):
        """Gets the data of this UserSiteDataCreate.  # noqa: E501


        :return: The data of this UserSiteDataCreate.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserSiteDataCreate.


        :param data: The data of this UserSiteDataCreate.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, UserSiteDataCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
