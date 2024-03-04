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


class PackageTypeByQuantityProduct(object):
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
        'recommended_quantity': 'int',
        'digi_key_product_number': 'str',
        'quantity_available': 'int',
        'product_description': 'str',
        'detailed_description': 'str',
        'manufacturer_name': 'str',
        'manufacturer_product_number': 'str',
        'minimum_order_quantity': 'int',
        'primary_datasheet_url': 'str',
        'primary_photo_url': 'str',
        'product_status': 'str',
        'manufacturer_lead_weeks': 'str',
        'manufacturer_warehouse_quantity': 'int',
        'rohs_status': 'str',
        'ro_hs_compliant': 'bool',
        'quantity_on_order': 'int',
        'standard_pricing': 'list[BreakPrice]',
        'my_pricing': 'list[BreakPrice]',
        'product_url': 'str',
        'market_place': 'bool',
        'supplier': 'str',
        'stock_note': 'str',
        'package_types': 'list[str]'
    }

    attribute_map = {
        'recommended_quantity': 'RecommendedQuantity',
        'digi_key_product_number': 'DigiKeyProductNumber',
        'quantity_available': 'QuantityAvailable',
        'product_description': 'ProductDescription',
        'detailed_description': 'DetailedDescription',
        'manufacturer_name': 'ManufacturerName',
        'manufacturer_product_number': 'ManufacturerProductNumber',
        'minimum_order_quantity': 'MinimumOrderQuantity',
        'primary_datasheet_url': 'PrimaryDatasheetUrl',
        'primary_photo_url': 'PrimaryPhotoUrl',
        'product_status': 'ProductStatus',
        'manufacturer_lead_weeks': 'ManufacturerLeadWeeks',
        'manufacturer_warehouse_quantity': 'ManufacturerWarehouseQuantity',
        'rohs_status': 'RohsStatus',
        'ro_hs_compliant': 'RoHSCompliant',
        'quantity_on_order': 'QuantityOnOrder',
        'standard_pricing': 'StandardPricing',
        'my_pricing': 'MyPricing',
        'product_url': 'ProductUrl',
        'market_place': 'MarketPlace',
        'supplier': 'Supplier',
        'stock_note': 'StockNote',
        'package_types': 'PackageTypes'
    }

    def __init__(self, recommended_quantity=None, digi_key_product_number=None, quantity_available=None, product_description=None, detailed_description=None, manufacturer_name=None, manufacturer_product_number=None, minimum_order_quantity=None, primary_datasheet_url=None, primary_photo_url=None, product_status=None, manufacturer_lead_weeks=None, manufacturer_warehouse_quantity=None, rohs_status=None, ro_hs_compliant=None, quantity_on_order=None, standard_pricing=None, my_pricing=None, product_url=None, market_place=None, supplier=None, stock_note=None, package_types=None, _configuration=None):  # noqa: E501
        """PackageTypeByQuantityProduct - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._recommended_quantity = None
        self._digi_key_product_number = None
        self._quantity_available = None
        self._product_description = None
        self._detailed_description = None
        self._manufacturer_name = None
        self._manufacturer_product_number = None
        self._minimum_order_quantity = None
        self._primary_datasheet_url = None
        self._primary_photo_url = None
        self._product_status = None
        self._manufacturer_lead_weeks = None
        self._manufacturer_warehouse_quantity = None
        self._rohs_status = None
        self._ro_hs_compliant = None
        self._quantity_on_order = None
        self._standard_pricing = None
        self._my_pricing = None
        self._product_url = None
        self._market_place = None
        self._supplier = None
        self._stock_note = None
        self._package_types = None
        self.discriminator = None

        if recommended_quantity is not None:
            self.recommended_quantity = recommended_quantity
        if digi_key_product_number is not None:
            self.digi_key_product_number = digi_key_product_number
        if quantity_available is not None:
            self.quantity_available = quantity_available
        if product_description is not None:
            self.product_description = product_description
        if detailed_description is not None:
            self.detailed_description = detailed_description
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if manufacturer_product_number is not None:
            self.manufacturer_product_number = manufacturer_product_number
        if minimum_order_quantity is not None:
            self.minimum_order_quantity = minimum_order_quantity
        if primary_datasheet_url is not None:
            self.primary_datasheet_url = primary_datasheet_url
        if primary_photo_url is not None:
            self.primary_photo_url = primary_photo_url
        if product_status is not None:
            self.product_status = product_status
        if manufacturer_lead_weeks is not None:
            self.manufacturer_lead_weeks = manufacturer_lead_weeks
        if manufacturer_warehouse_quantity is not None:
            self.manufacturer_warehouse_quantity = manufacturer_warehouse_quantity
        if rohs_status is not None:
            self.rohs_status = rohs_status
        if ro_hs_compliant is not None:
            self.ro_hs_compliant = ro_hs_compliant
        if quantity_on_order is not None:
            self.quantity_on_order = quantity_on_order
        if standard_pricing is not None:
            self.standard_pricing = standard_pricing
        if my_pricing is not None:
            self.my_pricing = my_pricing
        if product_url is not None:
            self.product_url = product_url
        if market_place is not None:
            self.market_place = market_place
        if supplier is not None:
            self.supplier = supplier
        if stock_note is not None:
            self.stock_note = stock_note
        if package_types is not None:
            self.package_types = package_types

    @property
    def recommended_quantity(self):
        """Gets the recommended_quantity of this PackageTypeByQuantityProduct.  # noqa: E501

        Recommended quantity for product  # noqa: E501

        :return: The recommended_quantity of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: int
        """
        return self._recommended_quantity

    @recommended_quantity.setter
    def recommended_quantity(self, recommended_quantity):
        """Sets the recommended_quantity of this PackageTypeByQuantityProduct.

        Recommended quantity for product  # noqa: E501

        :param recommended_quantity: The recommended_quantity of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: int
        """

        self._recommended_quantity = recommended_quantity

    @property
    def digi_key_product_number(self):
        """Gets the digi_key_product_number of this PackageTypeByQuantityProduct.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_product_number of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._digi_key_product_number

    @digi_key_product_number.setter
    def digi_key_product_number(self, digi_key_product_number):
        """Sets the digi_key_product_number of this PackageTypeByQuantityProduct.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_product_number: The digi_key_product_number of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._digi_key_product_number = digi_key_product_number

    @property
    def quantity_available(self):
        """Gets the quantity_available of this PackageTypeByQuantityProduct.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: int
        """
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, quantity_available):
        """Sets the quantity_available of this PackageTypeByQuantityProduct.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: int
        """

        self._quantity_available = quantity_available

    @property
    def product_description(self):
        """Gets the product_description of this PackageTypeByQuantityProduct.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this PackageTypeByQuantityProduct.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def detailed_description(self):
        """Gets the detailed_description of this PackageTypeByQuantityProduct.  # noqa: E501

        Extended catalog description of the product.  # noqa: E501

        :return: The detailed_description of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._detailed_description

    @detailed_description.setter
    def detailed_description(self, detailed_description):
        """Sets the detailed_description of this PackageTypeByQuantityProduct.

        Extended catalog description of the product.  # noqa: E501

        :param detailed_description: The detailed_description of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._detailed_description = detailed_description

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this PackageTypeByQuantityProduct.  # noqa: E501

        Manufacturer of the product.  # noqa: E501

        :return: The manufacturer_name of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this PackageTypeByQuantityProduct.

        Manufacturer of the product.  # noqa: E501

        :param manufacturer_name: The manufacturer_name of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._manufacturer_name = manufacturer_name

    @property
    def manufacturer_product_number(self):
        """Gets the manufacturer_product_number of this PackageTypeByQuantityProduct.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_product_number of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_product_number

    @manufacturer_product_number.setter
    def manufacturer_product_number(self, manufacturer_product_number):
        """Sets the manufacturer_product_number of this PackageTypeByQuantityProduct.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_product_number: The manufacturer_product_number of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._manufacturer_product_number = manufacturer_product_number

    @property
    def minimum_order_quantity(self):
        """Gets the minimum_order_quantity of this PackageTypeByQuantityProduct.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: int
        """
        return self._minimum_order_quantity

    @minimum_order_quantity.setter
    def minimum_order_quantity(self, minimum_order_quantity):
        """Sets the minimum_order_quantity of this PackageTypeByQuantityProduct.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: int
        """

        self._minimum_order_quantity = minimum_order_quantity

    @property
    def primary_datasheet_url(self):
        """Gets the primary_datasheet_url of this PackageTypeByQuantityProduct.  # noqa: E501

        The URL to the product's datasheet.  # noqa: E501

        :return: The primary_datasheet_url of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._primary_datasheet_url

    @primary_datasheet_url.setter
    def primary_datasheet_url(self, primary_datasheet_url):
        """Sets the primary_datasheet_url of this PackageTypeByQuantityProduct.

        The URL to the product's datasheet.  # noqa: E501

        :param primary_datasheet_url: The primary_datasheet_url of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._primary_datasheet_url = primary_datasheet_url

    @property
    def primary_photo_url(self):
        """Gets the primary_photo_url of this PackageTypeByQuantityProduct.  # noqa: E501

        The URL to the product's image.  # noqa: E501

        :return: The primary_photo_url of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._primary_photo_url

    @primary_photo_url.setter
    def primary_photo_url(self, primary_photo_url):
        """Sets the primary_photo_url of this PackageTypeByQuantityProduct.

        The URL to the product's image.  # noqa: E501

        :param primary_photo_url: The primary_photo_url of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._primary_photo_url = primary_photo_url

    @property
    def product_status(self):
        """Gets the product_status of this PackageTypeByQuantityProduct.  # noqa: E501

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key,  Last Time Buy, Not For New Designs, Preliminary. For obsolete parts the part  will become a non-stocking item when stock is depleted; minimums will apply.  Order the quantity available or the quantity available plus a multiple of the  minimum order quantity.  ///  # noqa: E501

        :return: The product_status of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_status

    @product_status.setter
    def product_status(self, product_status):
        """Sets the product_status of this PackageTypeByQuantityProduct.

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key,  Last Time Buy, Not For New Designs, Preliminary. For obsolete parts the part  will become a non-stocking item when stock is depleted; minimums will apply.  Order the quantity available or the quantity available plus a multiple of the  minimum order quantity.  ///  # noqa: E501

        :param product_status: The product_status of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._product_status = product_status

    @property
    def manufacturer_lead_weeks(self):
        """Gets the manufacturer_lead_weeks of this PackageTypeByQuantityProduct.  # noqa: E501

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :return: The manufacturer_lead_weeks of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_lead_weeks

    @manufacturer_lead_weeks.setter
    def manufacturer_lead_weeks(self, manufacturer_lead_weeks):
        """Sets the manufacturer_lead_weeks of this PackageTypeByQuantityProduct.

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :param manufacturer_lead_weeks: The manufacturer_lead_weeks of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._manufacturer_lead_weeks = manufacturer_lead_weeks

    @property
    def manufacturer_warehouse_quantity(self):
        """Gets the manufacturer_warehouse_quantity of this PackageTypeByQuantityProduct.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_warehouse_quantity of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer_warehouse_quantity

    @manufacturer_warehouse_quantity.setter
    def manufacturer_warehouse_quantity(self, manufacturer_warehouse_quantity):
        """Sets the manufacturer_warehouse_quantity of this PackageTypeByQuantityProduct.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_warehouse_quantity: The manufacturer_warehouse_quantity of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: int
        """

        self._manufacturer_warehouse_quantity = manufacturer_warehouse_quantity

    @property
    def rohs_status(self):
        """Gets the rohs_status of this PackageTypeByQuantityProduct.  # noqa: E501

        RoHS status. Can be RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, or ROHS3 Compliant.  # noqa: E501

        :return: The rohs_status of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._rohs_status

    @rohs_status.setter
    def rohs_status(self, rohs_status):
        """Sets the rohs_status of this PackageTypeByQuantityProduct.

        RoHS status. Can be RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, or ROHS3 Compliant.  # noqa: E501

        :param rohs_status: The rohs_status of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._rohs_status = rohs_status

    @property
    def ro_hs_compliant(self):
        """Gets the ro_hs_compliant of this PackageTypeByQuantityProduct.  # noqa: E501

        Boolean value for RoHS compliance.  # noqa: E501

        :return: The ro_hs_compliant of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: bool
        """
        return self._ro_hs_compliant

    @ro_hs_compliant.setter
    def ro_hs_compliant(self, ro_hs_compliant):
        """Sets the ro_hs_compliant of this PackageTypeByQuantityProduct.

        Boolean value for RoHS compliance.  # noqa: E501

        :param ro_hs_compliant: The ro_hs_compliant of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: bool
        """

        self._ro_hs_compliant = ro_hs_compliant

    @property
    def quantity_on_order(self):
        """Gets the quantity_on_order of this PackageTypeByQuantityProduct.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: int
        """
        return self._quantity_on_order

    @quantity_on_order.setter
    def quantity_on_order(self, quantity_on_order):
        """Sets the quantity_on_order of this PackageTypeByQuantityProduct.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: int
        """

        self._quantity_on_order = quantity_on_order

    @property
    def standard_pricing(self):
        """Gets the standard_pricing of this PackageTypeByQuantityProduct.  # noqa: E501

        Standard pricing for the validated locale.  # noqa: E501

        :return: The standard_pricing of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: list[BreakPrice]
        """
        return self._standard_pricing

    @standard_pricing.setter
    def standard_pricing(self, standard_pricing):
        """Sets the standard_pricing of this PackageTypeByQuantityProduct.

        Standard pricing for the validated locale.  # noqa: E501

        :param standard_pricing: The standard_pricing of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: list[BreakPrice]
        """

        self._standard_pricing = standard_pricing

    @property
    def my_pricing(self):
        """Gets the my_pricing of this PackageTypeByQuantityProduct.  # noqa: E501

        My pricing for the validated locale.  # noqa: E501

        :return: The my_pricing of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: list[BreakPrice]
        """
        return self._my_pricing

    @my_pricing.setter
    def my_pricing(self, my_pricing):
        """Sets the my_pricing of this PackageTypeByQuantityProduct.

        My pricing for the validated locale.  # noqa: E501

        :param my_pricing: The my_pricing of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: list[BreakPrice]
        """

        self._my_pricing = my_pricing

    @property
    def product_url(self):
        """Gets the product_url of this PackageTypeByQuantityProduct.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_url

    @product_url.setter
    def product_url(self, product_url):
        """Sets the product_url of this PackageTypeByQuantityProduct.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._product_url = product_url

    @property
    def market_place(self):
        """Gets the market_place of this PackageTypeByQuantityProduct.  # noqa: E501

        Is this product a marketplace product  # noqa: E501

        :return: The market_place of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: bool
        """
        return self._market_place

    @market_place.setter
    def market_place(self, market_place):
        """Sets the market_place of this PackageTypeByQuantityProduct.

        Is this product a marketplace product  # noqa: E501

        :param market_place: The market_place of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: bool
        """

        self._market_place = market_place

    @property
    def supplier(self):
        """Gets the supplier of this PackageTypeByQuantityProduct.  # noqa: E501

        Name of product supplier  # noqa: E501

        :return: The supplier of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this PackageTypeByQuantityProduct.

        Name of product supplier  # noqa: E501

        :param supplier: The supplier of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

    @property
    def stock_note(self):
        """Gets the stock_note of this PackageTypeByQuantityProduct.  # noqa: E501

        Description of Digi-Key's current stocking status for the product. Possible values include: In Stock, Temporarily  Out of Stock, and Limited Supply - Call.  # noqa: E501

        :return: The stock_note of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: str
        """
        return self._stock_note

    @stock_note.setter
    def stock_note(self, stock_note):
        """Sets the stock_note of this PackageTypeByQuantityProduct.

        Description of Digi-Key's current stocking status for the product. Possible values include: In Stock, Temporarily  Out of Stock, and Limited Supply - Call.  # noqa: E501

        :param stock_note: The stock_note of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: str
        """

        self._stock_note = stock_note

    @property
    def package_types(self):
        """Gets the package_types of this PackageTypeByQuantityProduct.  # noqa: E501


        :return: The package_types of this PackageTypeByQuantityProduct.  # noqa: E501
        :rtype: list[str]
        """
        return self._package_types

    @package_types.setter
    def package_types(self, package_types):
        """Sets the package_types of this PackageTypeByQuantityProduct.


        :param package_types: The package_types of this PackageTypeByQuantityProduct.  # noqa: E501
        :type: list[str]
        """

        self._package_types = package_types

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
        if issubclass(PackageTypeByQuantityProduct, dict):
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
        if not isinstance(other, PackageTypeByQuantityProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageTypeByQuantityProduct):
            return True

        return self.to_dict() != other.to_dict()
