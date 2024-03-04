# coding: utf-8

"""
    ProductSearch Api

    ProductSearch Api  # noqa: E501

    OpenAPI spec version: v4
    Contact: dl_Agile_Team_B2B_API@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dk_api_client.configuration import Configuration


class DKProblemDetails(object):
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
        'type': 'str',
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str',
        'correlation_id': 'str',
        'errors': 'dict(str, list[str])'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance',
        'correlation_id': 'correlationId',
        'errors': 'errors'
    }

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, correlation_id=None, errors=None, _configuration=None):  # noqa: E501
        """DKProblemDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self._correlation_id = None
        self._errors = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if instance is not None:
            self.instance = instance
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if errors is not None:
            self.errors = errors

    @property
    def type(self):
        """Gets the type of this DKProblemDetails.  # noqa: E501


        :return: The type of this DKProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DKProblemDetails.


        :param type: The type of this DKProblemDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this DKProblemDetails.  # noqa: E501


        :return: The title of this DKProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DKProblemDetails.


        :param title: The title of this DKProblemDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this DKProblemDetails.  # noqa: E501


        :return: The status of this DKProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DKProblemDetails.


        :param status: The status of this DKProblemDetails.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this DKProblemDetails.  # noqa: E501


        :return: The detail of this DKProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this DKProblemDetails.


        :param detail: The detail of this DKProblemDetails.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this DKProblemDetails.  # noqa: E501


        :return: The instance of this DKProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this DKProblemDetails.


        :param instance: The instance of this DKProblemDetails.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def correlation_id(self):
        """Gets the correlation_id of this DKProblemDetails.  # noqa: E501


        :return: The correlation_id of this DKProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this DKProblemDetails.


        :param correlation_id: The correlation_id of this DKProblemDetails.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def errors(self):
        """Gets the errors of this DKProblemDetails.  # noqa: E501


        :return: The errors of this DKProblemDetails.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DKProblemDetails.


        :param errors: The errors of this DKProblemDetails.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._errors = errors

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
        if issubclass(DKProblemDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DKProblemDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DKProblemDetails):
            return True

        return self.to_dict() != other.to_dict()
