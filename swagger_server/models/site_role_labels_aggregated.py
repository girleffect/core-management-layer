# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.role_label import RoleLabel  # noqa: F401,E501
from swagger_server import util


class SiteRoleLabelsAggregated(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, site_id: int=None, roles: List[RoleLabel]=None):  # noqa: E501
        """SiteRoleLabelsAggregated - a model defined in Swagger

        :param site_id: The site_id of this SiteRoleLabelsAggregated.  # noqa: E501
        :type site_id: int
        :param roles: The roles of this SiteRoleLabelsAggregated.  # noqa: E501
        :type roles: List[RoleLabel]
        """
        self.swagger_types = {
            'site_id': int,
            'roles': List[RoleLabel]
        }

        self.attribute_map = {
            'site_id': 'site_id',
            'roles': 'roles'
        }

        self._site_id = site_id
        self._roles = roles

    @classmethod
    def from_dict(cls, dikt) -> 'SiteRoleLabelsAggregated':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The site_role_labels_aggregated of this SiteRoleLabelsAggregated.  # noqa: E501
        :rtype: SiteRoleLabelsAggregated
        """
        return util.deserialize_model(dikt, cls)

    @property
    def site_id(self) -> int:
        """Gets the site_id of this SiteRoleLabelsAggregated.


        :return: The site_id of this SiteRoleLabelsAggregated.
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: int):
        """Sets the site_id of this SiteRoleLabelsAggregated.


        :param site_id: The site_id of this SiteRoleLabelsAggregated.
        :type site_id: int
        """

        self._site_id = site_id

    @property
    def roles(self) -> List[RoleLabel]:
        """Gets the roles of this SiteRoleLabelsAggregated.


        :return: The roles of this SiteRoleLabelsAggregated.
        :rtype: List[RoleLabel]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: List[RoleLabel]):
        """Sets the roles of this SiteRoleLabelsAggregated.


        :param roles: The roles of this SiteRoleLabelsAggregated.
        :type roles: List[RoleLabel]
        """

        self._roles = roles
