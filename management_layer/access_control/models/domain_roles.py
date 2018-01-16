# coding: utf-8

"""
    Access Control API

    # The Access Control API  ## Overview The Access Control API is an API exposed to other core components. It uses an API Key in an HTTP header to perform authentication and authorisation.  Most of the API calls facilitates CRUD of the entities defined in the Access Control component. Others calls allows the retrieval of information in a form that is convenient for other components (most notably the Management Layer) to consume. 

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DomainRoles(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'domain_id': 'int',
        'roles_map': 'dict(str, list[int])'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'roles_map': 'roles_map'
    }

    def __init__(self, domain_id=None, roles_map=None):
        """
        DomainRoles - a model defined in Swagger
        """

        self._domain_id = None
        self._roles_map = None

        self.domain_id = domain_id
        self.roles_map = roles_map

    @property
    def domain_id(self):
        """
        Gets the domain_id of this DomainRoles.
        The domain for which the request was made.

        :return: The domain_id of this DomainRoles.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this DomainRoles.
        The domain for which the request was made.

        :param domain_id: The domain_id of this DomainRoles.
        :type: int
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")

        self._domain_id = domain_id

    @property
    def roles_map(self):
        """
        Gets the roles_map of this DomainRoles.
        A dictionary where the keys are domain ids prefixed with `d:` and the values are lists of role ids.

        :return: The roles_map of this DomainRoles.
        :rtype: dict(str, list[int])
        """
        return self._roles_map

    @roles_map.setter
    def roles_map(self, roles_map):
        """
        Sets the roles_map of this DomainRoles.
        A dictionary where the keys are domain ids prefixed with `d:` and the values are lists of role ids.

        :param roles_map: The roles_map of this DomainRoles.
        :type: dict(str, list[int])
        """
        if roles_map is None:
            raise ValueError("Invalid value for `roles_map`, must not be `None`")

        self._roles_map = roles_map

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DomainRoles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other