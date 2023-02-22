"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....osmosis.downtime_detector.v1beta1 import downtime_duration_pb2 as osmosis_dot_downtime__detector_dot_v1beta1_dot_downtime__duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/osmosis/downtime-detector/v1beta1/genesis.proto\x12 osmosis.downtimedetector.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a9osmosis/downtime-detector/v1beta1/downtime_duration.proto"\xbe\x01\n\x14GenesisDowntimeEntry\x12Q\n\x08duration\x18\x01 \x01(\x0e2*.osmosis.downtimedetector.v1beta1.DowntimeB\x13\xf2\xde\x1f\x0fyaml:"duration"\x12S\n\rlast_downtime\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB \xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x14yaml:"last_downtime""\xb8\x01\n\x0cGenesisState\x12O\n\tdowntimes\x18\x01 \x03(\x0b26.osmosis.downtimedetector.v1beta1.GenesisDowntimeEntryB\x04\xc8\xde\x1f\x00\x12W\n\x0flast_block_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB"\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x16yaml:"last_block_time"B?Z=github.com/osmosis-labs/osmosis/v14/x/downtime-detector/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.downtime_detector.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/osmosis-labs/osmosis/v14/x/downtime-detector/types'
    _GENESISDOWNTIMEENTRY.fields_by_name['duration']._options = None
    _GENESISDOWNTIMEENTRY.fields_by_name['duration']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"duration"'
    _GENESISDOWNTIMEENTRY.fields_by_name['last_downtime']._options = None
    _GENESISDOWNTIMEENTRY.fields_by_name['last_downtime']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x14yaml:"last_downtime"'
    _GENESISSTATE.fields_by_name['downtimes']._options = None
    _GENESISSTATE.fields_by_name['downtimes']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['last_block_time']._options = None
    _GENESISSTATE.fields_by_name['last_block_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x16yaml:"last_block_time"'
    _GENESISDOWNTIMEENTRY._serialized_start = 286
    _GENESISDOWNTIMEENTRY._serialized_end = 476
    _GENESISSTATE._serialized_start = 479
    _GENESISSTATE._serialized_end = 663