# coding: utf-8

"""
    Authentication Service API

    This is the API that will be exposed by the Authentication Service.  The Authentication Service facilitates user registration and login via web-based flows as defined for the OpenID Connect specification.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class User(object):
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
        'id': 'str',
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'is_active': 'bool',
        'date_joined': 'date',
        'last_login': 'str',
        'email_verified': 'bool',
        'msisdn_verified': 'bool',
        'msisdn': 'str',
        'gender': 'str',
        'birth_date': 'date',
        'avatar': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'is_active': 'is_active',
        'date_joined': 'date_joined',
        'last_login': 'last_login',
        'email_verified': 'email_verified',
        'msisdn_verified': 'msisdn_verified',
        'msisdn': 'msisdn',
        'gender': 'gender',
        'birth_date': 'birth_date',
        'avatar': 'avatar',
        'country_code': 'country_code'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, email=None, is_active=None, date_joined=None, last_login=None, email_verified=None, msisdn_verified=None, msisdn=None, gender=None, birth_date=None, avatar=None, country_code=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._is_active = None
        self._date_joined = None
        self._last_login = None
        self._email_verified = None
        self._msisdn_verified = None
        self._msisdn = None
        self._gender = None
        self._birth_date = None
        self._avatar = None
        self._country_code = None
        self.discriminator = None

        self.id = id
        self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        self.is_active = is_active
        self.date_joined = date_joined
        if last_login is not None:
            self.last_login = last_login
        if email_verified is not None:
            self.email_verified = email_verified
        if msisdn_verified is not None:
            self.msisdn_verified = msisdn_verified
        if msisdn is not None:
            self.msisdn = msisdn
        if gender is not None:
            self.gender = gender
        if birth_date is not None:
            self.birth_date = birth_date
        if avatar is not None:
            self.avatar = avatar
        if country_code is not None:
            self.country_code = country_code

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        A UUID identifying the user  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        A UUID identifying the user  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

          # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

          # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

          # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

          # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

          # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

          # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def is_active(self):
        """Gets the is_active of this User.  # noqa: E501

        Designates whether this user should be treated as active. Deselect this instead of deleting accounts.  # noqa: E501

        :return: The is_active of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this User.

        Designates whether this user should be treated as active. Deselect this instead of deleting accounts.  # noqa: E501

        :param is_active: The is_active of this User.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def date_joined(self):
        """Gets the date_joined of this User.  # noqa: E501

          # noqa: E501

        :return: The date_joined of this User.  # noqa: E501
        :rtype: date
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """Sets the date_joined of this User.

          # noqa: E501

        :param date_joined: The date_joined of this User.  # noqa: E501
        :type: date
        """
        if date_joined is None:
            raise ValueError("Invalid value for `date_joined`, must not be `None`")  # noqa: E501

        self._date_joined = date_joined

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501

          # noqa: E501

        :return: The last_login of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.

          # noqa: E501

        :param last_login: The last_login of this User.  # noqa: E501
        :type: str
        """

        self._last_login = last_login

    @property
    def email_verified(self):
        """Gets the email_verified of this User.  # noqa: E501


        :return: The email_verified of this User.  # noqa: E501
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this User.


        :param email_verified: The email_verified of this User.  # noqa: E501
        :type: bool
        """

        self._email_verified = email_verified

    @property
    def msisdn_verified(self):
        """Gets the msisdn_verified of this User.  # noqa: E501


        :return: The msisdn_verified of this User.  # noqa: E501
        :rtype: bool
        """
        return self._msisdn_verified

    @msisdn_verified.setter
    def msisdn_verified(self, msisdn_verified):
        """Sets the msisdn_verified of this User.


        :param msisdn_verified: The msisdn_verified of this User.  # noqa: E501
        :type: bool
        """

        self._msisdn_verified = msisdn_verified

    @property
    def msisdn(self):
        """Gets the msisdn of this User.  # noqa: E501


        :return: The msisdn of this User.  # noqa: E501
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn):
        """Sets the msisdn of this User.


        :param msisdn: The msisdn of this User.  # noqa: E501
        :type: str
        """
        if msisdn is not None and len(msisdn) > 15:
            raise ValueError("Invalid value for `msisdn`, length must be less than or equal to `15`")  # noqa: E501

        self._msisdn = msisdn

    @property
    def gender(self):
        """Gets the gender of this User.  # noqa: E501


        :return: The gender of this User.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this User.


        :param gender: The gender of this User.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def birth_date(self):
        """Gets the birth_date of this User.  # noqa: E501


        :return: The birth_date of this User.  # noqa: E501
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this User.


        :param birth_date: The birth_date of this User.  # noqa: E501
        :type: date
        """

        self._birth_date = birth_date

    @property
    def avatar(self):
        """Gets the avatar of this User.  # noqa: E501


        :return: The avatar of this User.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this User.


        :param avatar: The avatar of this User.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def country_code(self):
        """Gets the country_code of this User.  # noqa: E501


        :return: The country_code of this User.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this User.


        :param country_code: The country_code of this User.  # noqa: E501
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._country_code = country_code

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other