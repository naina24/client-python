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


class V1Devices(object):
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
        'autoattach_graphics_device': 'bool',
        'autoattach_mem_balloon': 'bool',
        'autoattach_pod_interface': 'bool',
        'autoattach_serial_console': 'bool',
        'block_multi_queue': 'bool',
        'disks': 'list[V1Disk]',
        'filesystems': 'list[V1Filesystem]',
        'gpus': 'list[V1GPU]',
        'host_devices': 'list[V1HostDevice]',
        'inputs': 'list[V1Input]',
        'interfaces': 'list[V1Interface]',
        'network_interface_multiqueue': 'bool',
        'rng': 'V1Rng',
        'watchdog': 'V1Watchdog'
    }

    attribute_map = {
        'autoattach_graphics_device': 'autoattachGraphicsDevice',
        'autoattach_mem_balloon': 'autoattachMemBalloon',
        'autoattach_pod_interface': 'autoattachPodInterface',
        'autoattach_serial_console': 'autoattachSerialConsole',
        'block_multi_queue': 'blockMultiQueue',
        'disks': 'disks',
        'filesystems': 'filesystems',
        'gpus': 'gpus',
        'host_devices': 'hostDevices',
        'inputs': 'inputs',
        'interfaces': 'interfaces',
        'network_interface_multiqueue': 'networkInterfaceMultiqueue',
        'rng': 'rng',
        'watchdog': 'watchdog'
    }

    def __init__(self, autoattach_graphics_device=None, autoattach_mem_balloon=None, autoattach_pod_interface=None, autoattach_serial_console=None, block_multi_queue=None, disks=None, filesystems=None, gpus=None, host_devices=None, inputs=None, interfaces=None, network_interface_multiqueue=None, rng=None, watchdog=None):
        """
        V1Devices - a model defined in Swagger
        """

        self._autoattach_graphics_device = None
        self._autoattach_mem_balloon = None
        self._autoattach_pod_interface = None
        self._autoattach_serial_console = None
        self._block_multi_queue = None
        self._disks = None
        self._filesystems = None
        self._gpus = None
        self._host_devices = None
        self._inputs = None
        self._interfaces = None
        self._network_interface_multiqueue = None
        self._rng = None
        self._watchdog = None

        if autoattach_graphics_device is not None:
          self.autoattach_graphics_device = autoattach_graphics_device
        if autoattach_mem_balloon is not None:
          self.autoattach_mem_balloon = autoattach_mem_balloon
        if autoattach_pod_interface is not None:
          self.autoattach_pod_interface = autoattach_pod_interface
        if autoattach_serial_console is not None:
          self.autoattach_serial_console = autoattach_serial_console
        if block_multi_queue is not None:
          self.block_multi_queue = block_multi_queue
        if disks is not None:
          self.disks = disks
        if filesystems is not None:
          self.filesystems = filesystems
        if gpus is not None:
          self.gpus = gpus
        if host_devices is not None:
          self.host_devices = host_devices
        if inputs is not None:
          self.inputs = inputs
        if interfaces is not None:
          self.interfaces = interfaces
        if network_interface_multiqueue is not None:
          self.network_interface_multiqueue = network_interface_multiqueue
        if rng is not None:
          self.rng = rng
        if watchdog is not None:
          self.watchdog = watchdog

    @property
    def autoattach_graphics_device(self):
        """
        Gets the autoattach_graphics_device of this V1Devices.
        Whether to attach the default graphics device or not. VNC will not be available if set to false. Defaults to true.

        :return: The autoattach_graphics_device of this V1Devices.
        :rtype: bool
        """
        return self._autoattach_graphics_device

    @autoattach_graphics_device.setter
    def autoattach_graphics_device(self, autoattach_graphics_device):
        """
        Sets the autoattach_graphics_device of this V1Devices.
        Whether to attach the default graphics device or not. VNC will not be available if set to false. Defaults to true.

        :param autoattach_graphics_device: The autoattach_graphics_device of this V1Devices.
        :type: bool
        """

        self._autoattach_graphics_device = autoattach_graphics_device

    @property
    def autoattach_mem_balloon(self):
        """
        Gets the autoattach_mem_balloon of this V1Devices.
        Whether to attach the Memory balloon device with default period. Period can be adjusted in virt-config. Defaults to true.

        :return: The autoattach_mem_balloon of this V1Devices.
        :rtype: bool
        """
        return self._autoattach_mem_balloon

    @autoattach_mem_balloon.setter
    def autoattach_mem_balloon(self, autoattach_mem_balloon):
        """
        Sets the autoattach_mem_balloon of this V1Devices.
        Whether to attach the Memory balloon device with default period. Period can be adjusted in virt-config. Defaults to true.

        :param autoattach_mem_balloon: The autoattach_mem_balloon of this V1Devices.
        :type: bool
        """

        self._autoattach_mem_balloon = autoattach_mem_balloon

    @property
    def autoattach_pod_interface(self):
        """
        Gets the autoattach_pod_interface of this V1Devices.
        Whether to attach a pod network interface. Defaults to true.

        :return: The autoattach_pod_interface of this V1Devices.
        :rtype: bool
        """
        return self._autoattach_pod_interface

    @autoattach_pod_interface.setter
    def autoattach_pod_interface(self, autoattach_pod_interface):
        """
        Sets the autoattach_pod_interface of this V1Devices.
        Whether to attach a pod network interface. Defaults to true.

        :param autoattach_pod_interface: The autoattach_pod_interface of this V1Devices.
        :type: bool
        """

        self._autoattach_pod_interface = autoattach_pod_interface

    @property
    def autoattach_serial_console(self):
        """
        Gets the autoattach_serial_console of this V1Devices.
        Whether to attach the default serial console or not. Serial console access will not be available if set to false. Defaults to true.

        :return: The autoattach_serial_console of this V1Devices.
        :rtype: bool
        """
        return self._autoattach_serial_console

    @autoattach_serial_console.setter
    def autoattach_serial_console(self, autoattach_serial_console):
        """
        Sets the autoattach_serial_console of this V1Devices.
        Whether to attach the default serial console or not. Serial console access will not be available if set to false. Defaults to true.

        :param autoattach_serial_console: The autoattach_serial_console of this V1Devices.
        :type: bool
        """

        self._autoattach_serial_console = autoattach_serial_console

    @property
    def block_multi_queue(self):
        """
        Gets the block_multi_queue of this V1Devices.
        Whether or not to enable virtio multi-queue for block devices

        :return: The block_multi_queue of this V1Devices.
        :rtype: bool
        """
        return self._block_multi_queue

    @block_multi_queue.setter
    def block_multi_queue(self, block_multi_queue):
        """
        Sets the block_multi_queue of this V1Devices.
        Whether or not to enable virtio multi-queue for block devices

        :param block_multi_queue: The block_multi_queue of this V1Devices.
        :type: bool
        """

        self._block_multi_queue = block_multi_queue

    @property
    def disks(self):
        """
        Gets the disks of this V1Devices.
        Disks describes disks, cdroms, floppy and luns which are connected to the vmi.

        :return: The disks of this V1Devices.
        :rtype: list[V1Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """
        Sets the disks of this V1Devices.
        Disks describes disks, cdroms, floppy and luns which are connected to the vmi.

        :param disks: The disks of this V1Devices.
        :type: list[V1Disk]
        """

        self._disks = disks

    @property
    def filesystems(self):
        """
        Gets the filesystems of this V1Devices.
        Filesystems describes filesystem which is connected to the vmi.

        :return: The filesystems of this V1Devices.
        :rtype: list[V1Filesystem]
        """
        return self._filesystems

    @filesystems.setter
    def filesystems(self, filesystems):
        """
        Sets the filesystems of this V1Devices.
        Filesystems describes filesystem which is connected to the vmi.

        :param filesystems: The filesystems of this V1Devices.
        :type: list[V1Filesystem]
        """

        self._filesystems = filesystems

    @property
    def gpus(self):
        """
        Gets the gpus of this V1Devices.
        Whether to attach a GPU device to the vmi.

        :return: The gpus of this V1Devices.
        :rtype: list[V1GPU]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """
        Sets the gpus of this V1Devices.
        Whether to attach a GPU device to the vmi.

        :param gpus: The gpus of this V1Devices.
        :type: list[V1GPU]
        """

        self._gpus = gpus

    @property
    def host_devices(self):
        """
        Gets the host_devices of this V1Devices.
        Whether to attach a host device to the vmi.

        :return: The host_devices of this V1Devices.
        :rtype: list[V1HostDevice]
        """
        return self._host_devices

    @host_devices.setter
    def host_devices(self, host_devices):
        """
        Sets the host_devices of this V1Devices.
        Whether to attach a host device to the vmi.

        :param host_devices: The host_devices of this V1Devices.
        :type: list[V1HostDevice]
        """

        self._host_devices = host_devices

    @property
    def inputs(self):
        """
        Gets the inputs of this V1Devices.
        Inputs describe input devices

        :return: The inputs of this V1Devices.
        :rtype: list[V1Input]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this V1Devices.
        Inputs describe input devices

        :param inputs: The inputs of this V1Devices.
        :type: list[V1Input]
        """

        self._inputs = inputs

    @property
    def interfaces(self):
        """
        Gets the interfaces of this V1Devices.
        Interfaces describe network interfaces which are added to the vmi.

        :return: The interfaces of this V1Devices.
        :rtype: list[V1Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this V1Devices.
        Interfaces describe network interfaces which are added to the vmi.

        :param interfaces: The interfaces of this V1Devices.
        :type: list[V1Interface]
        """

        self._interfaces = interfaces

    @property
    def network_interface_multiqueue(self):
        """
        Gets the network_interface_multiqueue of this V1Devices.
        If specified, virtual network interfaces configured with a virtio bus will also enable the vhost multiqueue feature for network devices. The number of queues created depends on additional factors of the VirtualMachineInstance, like the number of guest CPUs.

        :return: The network_interface_multiqueue of this V1Devices.
        :rtype: bool
        """
        return self._network_interface_multiqueue

    @network_interface_multiqueue.setter
    def network_interface_multiqueue(self, network_interface_multiqueue):
        """
        Sets the network_interface_multiqueue of this V1Devices.
        If specified, virtual network interfaces configured with a virtio bus will also enable the vhost multiqueue feature for network devices. The number of queues created depends on additional factors of the VirtualMachineInstance, like the number of guest CPUs.

        :param network_interface_multiqueue: The network_interface_multiqueue of this V1Devices.
        :type: bool
        """

        self._network_interface_multiqueue = network_interface_multiqueue

    @property
    def rng(self):
        """
        Gets the rng of this V1Devices.
        Whether to have random number generator from host

        :return: The rng of this V1Devices.
        :rtype: V1Rng
        """
        return self._rng

    @rng.setter
    def rng(self, rng):
        """
        Sets the rng of this V1Devices.
        Whether to have random number generator from host

        :param rng: The rng of this V1Devices.
        :type: V1Rng
        """

        self._rng = rng

    @property
    def watchdog(self):
        """
        Gets the watchdog of this V1Devices.
        Watchdog describes a watchdog device which can be added to the vmi.

        :return: The watchdog of this V1Devices.
        :rtype: V1Watchdog
        """
        return self._watchdog

    @watchdog.setter
    def watchdog(self, watchdog):
        """
        Sets the watchdog of this V1Devices.
        Watchdog describes a watchdog device which can be added to the vmi.

        :param watchdog: The watchdog of this V1Devices.
        :type: V1Watchdog
        """

        self._watchdog = watchdog

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
        if not isinstance(other, V1Devices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
