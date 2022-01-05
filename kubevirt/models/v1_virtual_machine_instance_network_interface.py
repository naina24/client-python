# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1VirtualMachineInstanceNetworkInterface(object):
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
        'info_source': 'str',
        'interface_name': 'str',
        'ip_address': 'str',
        'ip_addresses': 'list[str]',
        'mac': 'str',
        'name': 'str'
    }

    attribute_map = {
        'info_source': 'infoSource',
        'interface_name': 'interfaceName',
        'ip_address': 'ipAddress',
        'ip_addresses': 'ipAddresses',
        'mac': 'mac',
        'name': 'name'
    }

    def __init__(self, info_source=None, interface_name=None, ip_address=None, ip_addresses=None, mac=None, name=None):
        """
        V1VirtualMachineInstanceNetworkInterface - a model defined in Swagger
        """

        self._info_source = None
        self._interface_name = None
        self._ip_address = None
        self._ip_addresses = None
        self._mac = None
        self._name = None

        if info_source is not None:
          self.info_source = info_source
        if interface_name is not None:
          self.interface_name = interface_name
        if ip_address is not None:
          self.ip_address = ip_address
        if ip_addresses is not None:
          self.ip_addresses = ip_addresses
        if mac is not None:
          self.mac = mac
        if name is not None:
          self.name = name

    @property
    def info_source(self):
        """
        Gets the info_source of this V1VirtualMachineInstanceNetworkInterface.
        Specifies the origin of the interface data collected. values: domain, guest-agent, or both

        :return: The info_source of this V1VirtualMachineInstanceNetworkInterface.
        :rtype: str
        """
        return self._info_source

    @info_source.setter
    def info_source(self, info_source):
        """
        Sets the info_source of this V1VirtualMachineInstanceNetworkInterface.
        Specifies the origin of the interface data collected. values: domain, guest-agent, or both

        :param info_source: The info_source of this V1VirtualMachineInstanceNetworkInterface.
        :type: str
        """

        self._info_source = info_source

    @property
    def interface_name(self):
        """
        Gets the interface_name of this V1VirtualMachineInstanceNetworkInterface.
        The interface name inside the Virtual Machine

        :return: The interface_name of this V1VirtualMachineInstanceNetworkInterface.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """
        Sets the interface_name of this V1VirtualMachineInstanceNetworkInterface.
        The interface name inside the Virtual Machine

        :param interface_name: The interface_name of this V1VirtualMachineInstanceNetworkInterface.
        :type: str
        """

        self._interface_name = interface_name

    @property
    def ip_address(self):
        """
        Gets the ip_address of this V1VirtualMachineInstanceNetworkInterface.
        IP address of a Virtual Machine interface. It is always the first item of IPs

        :return: The ip_address of this V1VirtualMachineInstanceNetworkInterface.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this V1VirtualMachineInstanceNetworkInterface.
        IP address of a Virtual Machine interface. It is always the first item of IPs

        :param ip_address: The ip_address of this V1VirtualMachineInstanceNetworkInterface.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this V1VirtualMachineInstanceNetworkInterface.
        List of all IP addresses of a Virtual Machine interface

        :return: The ip_addresses of this V1VirtualMachineInstanceNetworkInterface.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this V1VirtualMachineInstanceNetworkInterface.
        List of all IP addresses of a Virtual Machine interface

        :param ip_addresses: The ip_addresses of this V1VirtualMachineInstanceNetworkInterface.
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def mac(self):
        """
        Gets the mac of this V1VirtualMachineInstanceNetworkInterface.
        Hardware address of a Virtual Machine interface

        :return: The mac of this V1VirtualMachineInstanceNetworkInterface.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """
        Sets the mac of this V1VirtualMachineInstanceNetworkInterface.
        Hardware address of a Virtual Machine interface

        :param mac: The mac of this V1VirtualMachineInstanceNetworkInterface.
        :type: str
        """

        self._mac = mac

    @property
    def name(self):
        """
        Gets the name of this V1VirtualMachineInstanceNetworkInterface.
        Name of the interface, corresponds to name of the network assigned to the interface

        :return: The name of this V1VirtualMachineInstanceNetworkInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1VirtualMachineInstanceNetworkInterface.
        Name of the interface, corresponds to name of the network assigned to the interface

        :param name: The name of this V1VirtualMachineInstanceNetworkInterface.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, V1VirtualMachineInstanceNetworkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
