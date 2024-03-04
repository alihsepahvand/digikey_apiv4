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


class ParameterFilterOptionsResponse(object):
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
        'category': 'BaseFilterV3',
        'parameter_type': 'str',
        'parameter_id': 'int',
        'parameter_name': 'str',
        'filter_values': 'list[FilterValue]'
    }

    attribute_map = {
        'category': 'Category',
        'parameter_type': 'ParameterType',
        'parameter_id': 'ParameterId',
        'parameter_name': 'ParameterName',
        'filter_values': 'FilterValues'
    }

    def __init__(self, category=None, parameter_type=None, parameter_id=None, parameter_name=None, filter_values=None, _configuration=None):  # noqa: E501
        """ParameterFilterOptionsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._category = None
        self._parameter_type = None
        self._parameter_id = None
        self._parameter_name = None
        self._filter_values = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if parameter_type is not None:
            self.parameter_type = parameter_type
        if parameter_id is not None:
            self.parameter_id = parameter_id
        if parameter_name is not None:
            self.parameter_name = parameter_name
        if filter_values is not None:
            self.filter_values = filter_values

    @property
    def category(self):
        """Gets the category of this ParameterFilterOptionsResponse.  # noqa: E501


        :return: The category of this ParameterFilterOptionsResponse.  # noqa: E501
        :rtype: BaseFilterV3
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ParameterFilterOptionsResponse.


        :param category: The category of this ParameterFilterOptionsResponse.  # noqa: E501
        :type: BaseFilterV3
        """

        self._category = category

    @property
    def parameter_type(self):
        """Gets the parameter_type of this ParameterFilterOptionsResponse.  # noqa: E501

        Parameter Type  # noqa: E501

        :return: The parameter_type of this ParameterFilterOptionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        """Sets the parameter_type of this ParameterFilterOptionsResponse.

        Parameter Type  # noqa: E501

        :param parameter_type: The parameter_type of this ParameterFilterOptionsResponse.  # noqa: E501
        :type: str
        """

        self._parameter_type = parameter_type

    @property
    def parameter_id(self):
        """Gets the parameter_id of this ParameterFilterOptionsResponse.  # noqa: E501

        Parameter Id  # noqa: E501

        :return: The parameter_id of this ParameterFilterOptionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this ParameterFilterOptionsResponse.

        Parameter Id  # noqa: E501

        :param parameter_id: The parameter_id of this ParameterFilterOptionsResponse.  # noqa: E501
        :type: int
        """

        self._parameter_id = parameter_id

    @property
    def parameter_name(self):
        """Gets the parameter_name of this ParameterFilterOptionsResponse.  # noqa: E501

        Parameter Name  # noqa: E501

        :return: The parameter_name of this ParameterFilterOptionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this ParameterFilterOptionsResponse.

        Parameter Name  # noqa: E501

        :param parameter_name: The parameter_name of this ParameterFilterOptionsResponse.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def filter_values(self):
        """Gets the filter_values of this ParameterFilterOptionsResponse.  # noqa: E501

        List of Filter Values for the Parameter  # noqa: E501

        :return: The filter_values of this ParameterFilterOptionsResponse.  # noqa: E501
        :rtype: list[FilterValue]
        """
        return self._filter_values

    @filter_values.setter
    def filter_values(self, filter_values):
        """Sets the filter_values of this ParameterFilterOptionsResponse.

        List of Filter Values for the Parameter  # noqa: E501

        :param filter_values: The filter_values of this ParameterFilterOptionsResponse.  # noqa: E501
        :type: list[FilterValue]
        """

        self._filter_values = filter_values

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
        if issubclass(ParameterFilterOptionsResponse, dict):
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
        if not isinstance(other, ParameterFilterOptionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParameterFilterOptionsResponse):
            return True

        return self.to_dict() != other.to_dict()