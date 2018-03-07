# kubevirt-py
This is KubeVirt API an add-on for Kubernetes.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: v0.2.0-400-gbc77bb2e
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/kubevirt/kubevirt](https://github.com/kubevirt/kubevirt)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/kubevirt/client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kubevirt/client-python.git`)

Then import the package:
```python
import kubevirt 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kubevirt
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Health endpoint
    api_instance.check_health()
except ApiException as e:
    print("Exception when calling DefaultApi->check_health: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**check_health**](docs/DefaultApi.md#check_health) | **GET** /apis/kubevirt.io/v1alpha1/healthz | Health endpoint
*DefaultApi* | [**create_namespaced_virtual_machine**](docs/DefaultApi.md#create_namespaced_virtual_machine) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets | Create a VirtualMachine object.
*DefaultApi* | [**create_namespaced_virtual_machine_0**](docs/DefaultApi.md#create_namespaced_virtual_machine_0) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines | Create a VirtualMachine object.
*DefaultApi* | [**create_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#create_namespaced_virtual_machine_replica_set) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets | Create a VirtualMachineReplicaSet object.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets | Delete a collection of VirtualMachine objects.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine_0**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine_0) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines | Delete a collection of VirtualMachine objects.
*DefaultApi* | [**delete_collection_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#delete_collection_namespaced_virtual_machine_replica_set) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets | Delete a collection of VirtualMachineReplicaSet objects.
*DefaultApi* | [**delete_namespaced_virtual_machine**](docs/DefaultApi.md#delete_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets/{name} | Delete a VirtualMachine object.
*DefaultApi* | [**delete_namespaced_virtual_machine_0**](docs/DefaultApi.md#delete_namespaced_virtual_machine_0) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Delete a VirtualMachine object.
*DefaultApi* | [**delete_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#delete_namespaced_virtual_machine_replica_set) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Delete a VirtualMachineReplicaSet object.
*DefaultApi* | [**get_api_group**](docs/DefaultApi.md#get_api_group) | **GET** /apis/kubevirt.io | Get a KubeVirt API group
*DefaultApi* | [**get_api_resources**](docs/DefaultApi.md#get_api_resources) | **GET** /apis/kubevirt.io/v1alpha1 | Get KubeVirt API Resources
*DefaultApi* | [**list_namespaced_virtual_machine**](docs/DefaultApi.md#list_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets | Get a list of VirtualMachine objects.
*DefaultApi* | [**list_namespaced_virtual_machine_0**](docs/DefaultApi.md#list_namespaced_virtual_machine_0) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines | Get a list of VirtualMachine objects.
*DefaultApi* | [**list_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#list_namespaced_virtual_machine_replica_set) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets | Get a list of VirtualMachineReplicaSet objects.
*DefaultApi* | [**list_virtual_machine_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachinepresets | Get a list of all VirtualMachine objects.
*DefaultApi* | [**list_virtual_machine_for_all_namespaces_0**](docs/DefaultApi.md#list_virtual_machine_for_all_namespaces_0) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachines | Get a list of all VirtualMachine objects.
*DefaultApi* | [**list_virtual_machine_replica_set_for_all_namespaces**](docs/DefaultApi.md#list_virtual_machine_replica_set_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachinereplicasets | Get a list of all VirtualMachineReplicaSet objects.
*DefaultApi* | [**patch_namespaced_virtual_machine**](docs/DefaultApi.md#patch_namespaced_virtual_machine) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets/{name} | Patch a VirtualMachine object.
*DefaultApi* | [**patch_namespaced_virtual_machine_0**](docs/DefaultApi.md#patch_namespaced_virtual_machine_0) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Patch a VirtualMachine object.
*DefaultApi* | [**patch_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#patch_namespaced_virtual_machine_replica_set) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Patch a VirtualMachineReplicaSet object.
*DefaultApi* | [**read_namespaced_virtual_machine**](docs/DefaultApi.md#read_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets/{name} | Get a VirtualMachine object.
*DefaultApi* | [**read_namespaced_virtual_machine_0**](docs/DefaultApi.md#read_namespaced_virtual_machine_0) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Get a VirtualMachine object.
*DefaultApi* | [**read_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#read_namespaced_virtual_machine_replica_set) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Get a VirtualMachineReplicaSet object.
*DefaultApi* | [**replace_namespaced_virtual_machine**](docs/DefaultApi.md#replace_namespaced_virtual_machine) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepresets/{name} | Update a VirtualMachine object.
*DefaultApi* | [**replace_namespaced_virtual_machine_0**](docs/DefaultApi.md#replace_namespaced_virtual_machine_0) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Update a VirtualMachine object.
*DefaultApi* | [**replace_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#replace_namespaced_virtual_machine_replica_set) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Update a VirtualMachineReplicaSet object.
*DefaultApi* | [**watch_namespaced_virtual_machine**](docs/DefaultApi.md#watch_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachinepresets | Watch a VirtualMachine object.
*DefaultApi* | [**watch_namespaced_virtual_machine_0**](docs/DefaultApi.md#watch_namespaced_virtual_machine_0) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachines | Watch a VirtualMachine object.
*DefaultApi* | [**watch_namespaced_virtual_machine_replica_set**](docs/DefaultApi.md#watch_namespaced_virtual_machine_replica_set) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachinereplicasets | Watch a VirtualMachineReplicaSet object.
*DefaultApi* | [**watch_virtual_machine_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachinepresets | Watch a VirtualMachineList object.
*DefaultApi* | [**watch_virtual_machine_list_for_all_namespaces_0**](docs/DefaultApi.md#watch_virtual_machine_list_for_all_namespaces_0) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachines | Watch a VirtualMachineList object.
*DefaultApi* | [**watch_virtual_machine_replica_set_list_for_all_namespaces**](docs/DefaultApi.md#watch_virtual_machine_replica_set_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachinereplicasets | Watch a VirtualMachineReplicaSetList object.


## Documentation For Models

 - [V1APIGroup](docs/V1APIGroup.md)
 - [V1APIResource](docs/V1APIResource.md)
 - [V1APIResourceList](docs/V1APIResourceList.md)
 - [V1Affinity](docs/V1Affinity.md)
 - [V1CDRomTarget](docs/V1CDRomTarget.md)
 - [V1CPU](docs/V1CPU.md)
 - [V1Clock](docs/V1Clock.md)
 - [V1ClockOffsetUTC](docs/V1ClockOffsetUTC.md)
 - [V1CloudInitNoCloudSource](docs/V1CloudInitNoCloudSource.md)
 - [V1DeleteOptions](docs/V1DeleteOptions.md)
 - [V1Devices](docs/V1Devices.md)
 - [V1Disk](docs/V1Disk.md)
 - [V1DiskTarget](docs/V1DiskTarget.md)
 - [V1DomainSpec](docs/V1DomainSpec.md)
 - [V1EphemeralVolumeSource](docs/V1EphemeralVolumeSource.md)
 - [V1FeatureAPIC](docs/V1FeatureAPIC.md)
 - [V1FeatureHyperv](docs/V1FeatureHyperv.md)
 - [V1FeatureSpinlocks](docs/V1FeatureSpinlocks.md)
 - [V1FeatureState](docs/V1FeatureState.md)
 - [V1FeatureVendorID](docs/V1FeatureVendorID.md)
 - [V1Features](docs/V1Features.md)
 - [V1Firmware](docs/V1Firmware.md)
 - [V1FloppyTarget](docs/V1FloppyTarget.md)
 - [V1GroupVersionForDiscovery](docs/V1GroupVersionForDiscovery.md)
 - [V1HPETTimer](docs/V1HPETTimer.md)
 - [V1HypervTimer](docs/V1HypervTimer.md)
 - [V1I6300ESBWatchdog](docs/V1I6300ESBWatchdog.md)
 - [V1Initializer](docs/V1Initializer.md)
 - [V1Initializers](docs/V1Initializers.md)
 - [V1KVMTimer](docs/V1KVMTimer.md)
 - [V1LabelSelector](docs/V1LabelSelector.md)
 - [V1LabelSelectorRequirement](docs/V1LabelSelectorRequirement.md)
 - [V1ListMeta](docs/V1ListMeta.md)
 - [V1LocalObjectReference](docs/V1LocalObjectReference.md)
 - [V1LunTarget](docs/V1LunTarget.md)
 - [V1Machine](docs/V1Machine.md)
 - [V1NodeAffinity](docs/V1NodeAffinity.md)
 - [V1NodeSelector](docs/V1NodeSelector.md)
 - [V1NodeSelectorRequirement](docs/V1NodeSelectorRequirement.md)
 - [V1NodeSelectorTerm](docs/V1NodeSelectorTerm.md)
 - [V1ObjectMeta](docs/V1ObjectMeta.md)
 - [V1OwnerReference](docs/V1OwnerReference.md)
 - [V1PITTimer](docs/V1PITTimer.md)
 - [V1PersistentVolumeClaimVolumeSource](docs/V1PersistentVolumeClaimVolumeSource.md)
 - [V1Preconditions](docs/V1Preconditions.md)
 - [V1PreferredSchedulingTerm](docs/V1PreferredSchedulingTerm.md)
 - [V1RTCTimer](docs/V1RTCTimer.md)
 - [V1RegistryDiskSource](docs/V1RegistryDiskSource.md)
 - [V1ResourceRequirements](docs/V1ResourceRequirements.md)
 - [V1ServerAddressByClientCIDR](docs/V1ServerAddressByClientCIDR.md)
 - [V1Status](docs/V1Status.md)
 - [V1StatusCause](docs/V1StatusCause.md)
 - [V1StatusDetails](docs/V1StatusDetails.md)
 - [V1Timer](docs/V1Timer.md)
 - [V1VMReplicaSetCondition](docs/V1VMReplicaSetCondition.md)
 - [V1VMReplicaSetSpec](docs/V1VMReplicaSetSpec.md)
 - [V1VMReplicaSetStatus](docs/V1VMReplicaSetStatus.md)
 - [V1VMTemplateSpec](docs/V1VMTemplateSpec.md)
 - [V1VirtualMachine](docs/V1VirtualMachine.md)
 - [V1VirtualMachineCondition](docs/V1VirtualMachineCondition.md)
 - [V1VirtualMachineList](docs/V1VirtualMachineList.md)
 - [V1VirtualMachineNetworkInterface](docs/V1VirtualMachineNetworkInterface.md)
 - [V1VirtualMachinePreset](docs/V1VirtualMachinePreset.md)
 - [V1VirtualMachinePresetList](docs/V1VirtualMachinePresetList.md)
 - [V1VirtualMachinePresetSpec](docs/V1VirtualMachinePresetSpec.md)
 - [V1VirtualMachineReplicaSet](docs/V1VirtualMachineReplicaSet.md)
 - [V1VirtualMachineReplicaSetList](docs/V1VirtualMachineReplicaSetList.md)
 - [V1VirtualMachineSpec](docs/V1VirtualMachineSpec.md)
 - [V1VirtualMachineStatus](docs/V1VirtualMachineStatus.md)
 - [V1Volume](docs/V1Volume.md)
 - [V1WatchEvent](docs/V1WatchEvent.md)
 - [V1Watchdog](docs/V1Watchdog.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

kubevirt-dev@googlegroups.com

