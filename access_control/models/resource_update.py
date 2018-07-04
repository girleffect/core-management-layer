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


class ResourceUpdate(object):
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
        'urn': 'str',
        'description': 'str'
    }

    attribute_map = {
        'urn': 'urn',
        'description': 'description'
    }

    def __init__(self, urn=None, description=None):  # noqa: E501
        """ResourceUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._urn = None
        self._description = None
        self.discriminator = None

        if urn is not None:
            self.urn = urn
        if description is not None:
            self.description = description

    @property
    def urn(self):
        """Gets the urn of this ResourceUpdate.  # noqa: E501


        :return: The urn of this ResourceUpdate.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this ResourceUpdate.


        :param urn: The urn of this ResourceUpdate.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def description(self):
        """Gets the description of this ResourceUpdate.  # noqa: E501


        :return: The description of this ResourceUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResourceUpdate.


        :param description: The description of this ResourceUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, ResourceUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
