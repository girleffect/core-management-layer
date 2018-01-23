# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserSiteDataCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id: str=None, site_id: int=None, data_processing_consent_provided: bool=None, data: object=None):  # noqa: E501
        """UserSiteDataCreate - a model defined in Swagger

        :param user_id: The user_id of this UserSiteDataCreate.  # noqa: E501
        :type user_id: str
        :param site_id: The site_id of this UserSiteDataCreate.  # noqa: E501
        :type site_id: int
        :param data_processing_consent_provided: The data_processing_consent_provided of this UserSiteDataCreate.  # noqa: E501
        :type data_processing_consent_provided: bool
        :param data: The data of this UserSiteDataCreate.  # noqa: E501
        :type data: object
        """
        self.swagger_types = {
            'user_id': str,
            'site_id': int,
            'data_processing_consent_provided': bool,
            'data': object
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'site_id': 'site_id',
            'data_processing_consent_provided': 'data_processing_consent_provided',
            'data': 'data'
        }

        self._user_id = user_id
        self._site_id = site_id
        self._data_processing_consent_provided = data_processing_consent_provided
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'UserSiteDataCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_site_data_create of this UserSiteDataCreate.  # noqa: E501
        :rtype: UserSiteDataCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this UserSiteDataCreate.


        :return: The user_id of this UserSiteDataCreate.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this UserSiteDataCreate.


        :param user_id: The user_id of this UserSiteDataCreate.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def site_id(self) -> int:
        """Gets the site_id of this UserSiteDataCreate.


        :return: The site_id of this UserSiteDataCreate.
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: int):
        """Sets the site_id of this UserSiteDataCreate.


        :param site_id: The site_id of this UserSiteDataCreate.
        :type site_id: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def data_processing_consent_provided(self) -> bool:
        """Gets the data_processing_consent_provided of this UserSiteDataCreate.


        :return: The data_processing_consent_provided of this UserSiteDataCreate.
        :rtype: bool
        """
        return self._data_processing_consent_provided

    @data_processing_consent_provided.setter
    def data_processing_consent_provided(self, data_processing_consent_provided: bool):
        """Sets the data_processing_consent_provided of this UserSiteDataCreate.


        :param data_processing_consent_provided: The data_processing_consent_provided of this UserSiteDataCreate.
        :type data_processing_consent_provided: bool
        """
        if data_processing_consent_provided is None:
            raise ValueError("Invalid value for `data_processing_consent_provided`, must not be `None`")  # noqa: E501

        self._data_processing_consent_provided = data_processing_consent_provided

    @property
    def data(self) -> object:
        """Gets the data of this UserSiteDataCreate.


        :return: The data of this UserSiteDataCreate.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data: object):
        """Sets the data of this UserSiteDataCreate.


        :param data: The data of this UserSiteDataCreate.
        :type data: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
