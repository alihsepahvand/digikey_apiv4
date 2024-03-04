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


class Recommendation(object):
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
        'product_number': 'str',
        'recommended_products': 'list[RecommendedProduct]',
        'search_locale_used': 'IsoSearchLocale'
    }

    attribute_map = {
        'product_number': 'ProductNumber',
        'recommended_products': 'RecommendedProducts',
        'search_locale_used': 'SearchLocaleUsed'
    }

    def __init__(self, product_number=None, recommended_products=None, search_locale_used=None, _configuration=None):  # noqa: E501
        """Recommendation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_number = None
        self._recommended_products = None
        self._search_locale_used = None
        self.discriminator = None

        if product_number is not None:
            self.product_number = product_number
        if recommended_products is not None:
            self.recommended_products = recommended_products
        if search_locale_used is not None:
            self.search_locale_used = search_locale_used

    @property
    def product_number(self):
        """Gets the product_number of this Recommendation.  # noqa: E501

        The product number that the recommendations are for.  # noqa: E501

        :return: The product_number of this Recommendation.  # noqa: E501
        :rtype: str
        """
        return self._product_number

    @product_number.setter
    def product_number(self, product_number):
        """Sets the product_number of this Recommendation.

        The product number that the recommendations are for.  # noqa: E501

        :param product_number: The product_number of this Recommendation.  # noqa: E501
        :type: str
        """

        self._product_number = product_number

    @property
    def recommended_products(self):
        """Gets the recommended_products of this Recommendation.  # noqa: E501

        The list of recommended products.  # noqa: E501

        :return: The recommended_products of this Recommendation.  # noqa: E501
        :rtype: list[RecommendedProduct]
        """
        return self._recommended_products

    @recommended_products.setter
    def recommended_products(self, recommended_products):
        """Sets the recommended_products of this Recommendation.

        The list of recommended products.  # noqa: E501

        :param recommended_products: The recommended_products of this Recommendation.  # noqa: E501
        :type: list[RecommendedProduct]
        """

        self._recommended_products = recommended_products

    @property
    def search_locale_used(self):
        """Gets the search_locale_used of this Recommendation.  # noqa: E501


        :return: The search_locale_used of this Recommendation.  # noqa: E501
        :rtype: IsoSearchLocale
        """
        return self._search_locale_used

    @search_locale_used.setter
    def search_locale_used(self, search_locale_used):
        """Sets the search_locale_used of this Recommendation.


        :param search_locale_used: The search_locale_used of this Recommendation.  # noqa: E501
        :type: IsoSearchLocale
        """

        self._search_locale_used = search_locale_used

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
        if issubclass(Recommendation, dict):
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
        if not isinstance(other, Recommendation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Recommendation):
            return True

        return self.to_dict() != other.to_dict()
