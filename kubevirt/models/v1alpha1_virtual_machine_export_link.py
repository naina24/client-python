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


class V1alpha1VirtualMachineExportLink(object):
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
        'cert': 'str',
        'manifests': 'list[V1alpha1VirtualMachineExportManifest]',
        'volumes': 'list[V1alpha1VirtualMachineExportVolume]'
    }

    attribute_map = {
        'cert': 'cert',
        'manifests': 'manifests',
        'volumes': 'volumes'
    }

    def __init__(self, cert=None, manifests=None, volumes=None):
        """
        V1alpha1VirtualMachineExportLink - a model defined in Swagger
        """

        self._cert = None
        self._manifests = None
        self._volumes = None

        self.cert = cert
        if manifests is not None:
          self.manifests = manifests
        if volumes is not None:
          self.volumes = volumes

    @property
    def cert(self):
        """
        Gets the cert of this V1alpha1VirtualMachineExportLink.
        Cert is the public CA certificate base64 encoded

        :return: The cert of this V1alpha1VirtualMachineExportLink.
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """
        Sets the cert of this V1alpha1VirtualMachineExportLink.
        Cert is the public CA certificate base64 encoded

        :param cert: The cert of this V1alpha1VirtualMachineExportLink.
        :type: str
        """
        if cert is None:
            raise ValueError("Invalid value for `cert`, must not be `None`")

        self._cert = cert

    @property
    def manifests(self):
        """
        Gets the manifests of this V1alpha1VirtualMachineExportLink.
        Manifests is a list of available manifests for the export

        :return: The manifests of this V1alpha1VirtualMachineExportLink.
        :rtype: list[V1alpha1VirtualMachineExportManifest]
        """
        return self._manifests

    @manifests.setter
    def manifests(self, manifests):
        """
        Sets the manifests of this V1alpha1VirtualMachineExportLink.
        Manifests is a list of available manifests for the export

        :param manifests: The manifests of this V1alpha1VirtualMachineExportLink.
        :type: list[V1alpha1VirtualMachineExportManifest]
        """

        self._manifests = manifests

    @property
    def volumes(self):
        """
        Gets the volumes of this V1alpha1VirtualMachineExportLink.
        Volumes is a list of available volumes to export

        :return: The volumes of this V1alpha1VirtualMachineExportLink.
        :rtype: list[V1alpha1VirtualMachineExportVolume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1alpha1VirtualMachineExportLink.
        Volumes is a list of available volumes to export

        :param volumes: The volumes of this V1alpha1VirtualMachineExportLink.
        :type: list[V1alpha1VirtualMachineExportVolume]
        """

        self._volumes = volumes

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
        if not isinstance(other, V1alpha1VirtualMachineExportLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
