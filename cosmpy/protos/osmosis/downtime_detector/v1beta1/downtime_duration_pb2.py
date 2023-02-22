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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9osmosis/downtime-detector/v1beta1/downtime_duration.proto\x12 osmosis.downtimedetector.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto*\xc2\x03\n\x08Downtime\x12\x10\n\x0cDURATION_30S\x10\x00\x12\x0f\n\x0bDURATION_1M\x10\x01\x12\x0f\n\x0bDURATION_2M\x10\x02\x12\x0f\n\x0bDURATION_3M\x10\x03\x12\x0f\n\x0bDURATION_4M\x10\x04\x12\x0f\n\x0bDURATION_5M\x10\x05\x12\x10\n\x0cDURATION_10M\x10\x06\x12\x10\n\x0cDURATION_20M\x10\x07\x12\x10\n\x0cDURATION_30M\x10\x08\x12\x10\n\x0cDURATION_40M\x10\t\x12\x10\n\x0cDURATION_50M\x10\n\x12\x0f\n\x0bDURATION_1H\x10\x0b\x12\x11\n\rDURATION_1_5H\x10\x0c\x12\x0f\n\x0bDURATION_2H\x10\r\x12\x11\n\rDURATION_2_5H\x10\x0e\x12\x0f\n\x0bDURATION_3H\x10\x0f\x12\x0f\n\x0bDURATION_4H\x10\x10\x12\x0f\n\x0bDURATION_5H\x10\x11\x12\x0f\n\x0bDURATION_6H\x10\x12\x12\x0f\n\x0bDURATION_9H\x10\x13\x12\x10\n\x0cDURATION_12H\x10\x14\x12\x10\n\x0cDURATION_18H\x10\x15\x12\x10\n\x0cDURATION_24H\x10\x16\x12\x10\n\x0cDURATION_36H\x10\x17\x12\x10\n\x0cDURATION_48H\x10\x18B?Z=github.com/osmosis-labs/osmosis/v14/x/downtime-detector/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.downtime_detector.v1beta1.downtime_duration_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/osmosis-labs/osmosis/v14/x/downtime-detector/types'
    _DOWNTIME._serialized_start = 237
    _DOWNTIME._serialized_end = 687