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

from swagger_client.configuration import Configuration


class MediaResponse(object):
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
        'media_links': 'list[MediaLinks]'
    }

    attribute_map = {
        'media_links': 'MediaLinks'
    }

    def __init__(self, media_links=None, _configuration=None):  # noqa: E501
        """MediaResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._media_links = None
        self.discriminator = None

        if media_links is not None:
            self.media_links = media_links

    @property
    def media_links(self):
        """Gets the media_links of this MediaResponse.  # noqa: E501

        List of Media Links  # noqa: E501

        :return: The media_links of this MediaResponse.  # noqa: E501
        :rtype: list[MediaLinks]
        """
        return self._media_links

    @media_links.setter
    def media_links(self, media_links):
        """Sets the media_links of this MediaResponse.

        List of Media Links  # noqa: E501

        :param media_links: The media_links of this MediaResponse.  # noqa: E501
        :type: list[MediaLinks]
        """

        self._media_links = media_links

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
        if issubclass(MediaResponse, dict):
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
        if not isinstance(other, MediaResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaResponse):
            return True

        return self.to_dict() != other.to_dict()
