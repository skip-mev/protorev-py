"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.downtime_detector.v1beta1 import genesis_pb2 as osmosis_dot_downtime__detector_dot_v1beta1_dot_genesis__pb2
from ....osmosis.downtime_detector.v1beta1 import downtime_duration_pb2 as osmosis_dot_downtime__detector_dot_v1beta1_dot_downtime__duration__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-osmosis/downtime-detector/v1beta1/query.proto\x12 osmosis.downtimedetector.v1beta1\x1a\x14gogoproto/gogo.proto\x1a/osmosis/downtime-detector/v1beta1/genesis.proto\x1a9osmosis/downtime-detector/v1beta1/downtime_duration.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcd\x01\n%RecoveredSinceDowntimeOfLengthRequest\x12Q\n\x08downtime\x18\x01 \x01(\x0e2*.osmosis.downtimedetector.v1beta1.DowntimeB\x13\xf2\xde\x1f\x0fyaml:"downtime"\x12Q\n\x08recovery\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB$\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x18yaml:"recovery_duration""G\n&RecoveredSinceDowntimeOfLengthResponse\x12\x1d\n\x15succesfully_recovered\x18\x01 \x01(\x082\x88\x02\n\x05Query\x12\xfe\x01\n\x1eRecoveredSinceDowntimeOfLength\x12G.osmosis.downtimedetector.v1beta1.RecoveredSinceDowntimeOfLengthRequest\x1aH.osmosis.downtimedetector.v1beta1.RecoveredSinceDowntimeOfLengthResponse"I\x82\xd3\xe4\x93\x02C\x12A/osmosis/downtime-detector/v1beta1/RecoveredSinceDowntimeOfLengthBKZIgithub.com/osmosis-labs/osmosis/v14/x/downtime-detector/client/queryprotob\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.downtime_detector.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZIgithub.com/osmosis-labs/osmosis/v14/x/downtime-detector/client/queryproto'
    _RECOVEREDSINCEDOWNTIMEOFLENGTHREQUEST.fields_by_name['downtime']._options = None
    _RECOVEREDSINCEDOWNTIMEOFLENGTHREQUEST.fields_by_name['downtime']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"downtime"'
    _RECOVEREDSINCEDOWNTIMEOFLENGTHREQUEST.fields_by_name['recovery']._options = None
    _RECOVEREDSINCEDOWNTIMEOFLENGTHREQUEST.fields_by_name['recovery']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x18yaml:"recovery_duration"'
    _QUERY.methods_by_name['RecoveredSinceDowntimeOfLength']._options = None
    _QUERY.methods_by_name['RecoveredSinceDowntimeOfLength']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/osmosis/downtime-detector/v1beta1/RecoveredSinceDowntimeOfLength'
    _RECOVEREDSINCEDOWNTIMEOFLENGTHREQUEST._serialized_start = 439
    _RECOVEREDSINCEDOWNTIMEOFLENGTHREQUEST._serialized_end = 644
    _RECOVEREDSINCEDOWNTIMEOFLENGTHRESPONSE._serialized_start = 646
    _RECOVEREDSINCEDOWNTIMEOFLENGTHRESPONSE._serialized_end = 717
    _QUERY._serialized_start = 720
    _QUERY._serialized_end = 984