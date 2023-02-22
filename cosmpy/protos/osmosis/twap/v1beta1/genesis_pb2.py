"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.twap.v1beta1 import twap_record_pb2 as osmosis_dot_twap_dot_v1beta1_dot_twap__record__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"osmosis/twap/v1beta1/genesis.proto\x12\x14osmosis.twap.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&osmosis/twap/v1beta1/twap_record.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto"\x96\x01\n\x06Params\x12\x1e\n\x16prune_epoch_identifier\x18\x01 \x01(\t\x12l\n\x1arecord_history_keep_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB-\xf2\xde\x1f!yaml:"record_history_keep_period"\x98\xdf\x1f\x01\xc8\xde\x1f\x00"y\n\x0cGenesisState\x125\n\x05twaps\x18\x01 \x03(\x0b2 .osmosis.twap.v1beta1.TwapRecordB\x04\xc8\xde\x1f\x00\x122\n\x06params\x18\x02 \x01(\x0b2\x1c.osmosis.twap.v1beta1.ParamsB\x04\xc8\xde\x1f\x00B2Z0github.com/osmosis-labs/osmosis/v14/x/twap/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.twap.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/osmosis-labs/osmosis/v14/x/twap/types'
    _PARAMS.fields_by_name['record_history_keep_period']._options = None
    _PARAMS.fields_by_name['record_history_keep_period']._serialized_options = b'\xf2\xde\x1f!yaml:"record_history_keep_period"\x98\xdf\x1f\x01\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['twaps']._options = None
    _GENESISSTATE.fields_by_name['twaps']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS._serialized_start = 209
    _PARAMS._serialized_end = 359
    _GENESISSTATE._serialized_start = 361
    _GENESISSTATE._serialized_end = 482