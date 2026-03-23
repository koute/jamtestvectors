from bin_to_json import StfTestVector
from jam_types import (
    Enum,
    Errno,
    Struct,
    TimeSlot,
    OpaqueHash,
    Entropy,
    ReadyQueue,
    AccumulatedQueue,
    ServiceId,
    ServiceInfo,
    ByteSequence,
    Privileges,
    ServicesStatistics,
    Vec,
    U32
)
from jam_types import class_name as n

class AccumulateStorageMapEntry(Struct):
    type_mapping = [
        ('key', n(ByteSequence)),
        ('value', n(ByteSequence)),
    ]

class AccumulatePreimagesBlobMapEntry(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('blob', n(ByteSequence)),
    ]

class AccumulatePreimagesRequestsMapKey(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('length', n(U32)),
    ]

class AccumulatePreimagesRequestsMapEntry(Struct):
    type_mapping = [
        ('key', n(AccumulatePreimagesRequestsMapKey)),
        ('value', 'Vec<TimeSlot>')
    ]

class AccumulateServiceAccount(Struct):
    type_mapping = [
        ('service', n(ServiceInfo)),
        ('storage', 'Vec<AccumulateStorageMapEntry>'),
        ('preimage_blobs', 'Vec<AccumulatePreimagesBlobMapEntry>'),
        ('preimage_requests', 'Vec<AccumulatePreimagesRequestsMapEntry>')
    ]

class AccumulateServiceAccountMapEntry(Struct):
    type_mapping = [
        ('id', n(ServiceId)),
        ('data', n(AccumulateServiceAccount))
    ]    

class AccumulateServiceAccountMap(Vec):
    sub_type = n(AccumulateServiceAccountMapEntry)

class AccumulateState(Struct):
    type_mapping = [
        ('slot', n(TimeSlot)),
        ('entropy', n(Entropy)),
        ('ready_queue', n(ReadyQueue)),
        ('accumulated', n(AccumulatedQueue)),
        ('privileges', n(Privileges)),
        ('statistics', n(ServicesStatistics)),
        ('accounts', n(AccumulateServiceAccountMap))
    ]  

class AccumulateInput(Struct):
    type_mapping = [
        ('slot', n(TimeSlot)),
        ('reports', 'Vec<WorkReport>'),
    ]

class AccumulateOutput(Enum):
    type_mapping = {
        0: ('ok', n(OpaqueHash)),
        1: ('err', n(Errno))
    }

class AccumulateTestVector(StfTestVector):
    state_class = 'AccumulateState'
    input_class = 'AccumulateInput'
    output_class = 'AccumulateOutput'
