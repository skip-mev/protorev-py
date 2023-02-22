"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....osmosis.pool_incentives.v1beta1 import incentives_pb2 as osmosis_dot_pool__incentives_dot_v1beta1_dot_incentives__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-osmosis/pool-incentives/v1beta1/genesis.proto\x12\x1eosmosis.poolincentives.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a0osmosis/pool-incentives/v1beta1/incentives.proto"\xe9\x02\n\x0cGenesisState\x12<\n\x06params\x18\x01 \x01(\x0b2&.osmosis.poolincentives.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\\\n\x12lockable_durations\x18\x02 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"\x12X\n\ndistr_info\x18\x03 \x01(\x0b2).osmosis.poolincentives.v1beta1.DistrInfoB\x19\xc8\xde\x1f\x01\xf2\xde\x1f\x11yaml:"distr_info"\x12c\n\x0epool_to_gauges\x18\x04 \x01(\x0b2,.osmosis.poolincentives.v1beta1.PoolToGaugesB\x1d\xc8\xde\x1f\x01\xf2\xde\x1f\x15yaml:"pool_to_gauges"B=Z;github.com/osmosis-labs/osmosis/v14/x/pool-incentives/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.pool_incentives.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/osmosis-labs/osmosis/v14/x/pool-incentives/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['lockable_durations']._options = None
    _GENESISSTATE.fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"'
    _GENESISSTATE.fields_by_name['distr_info']._options = None
    _GENESISSTATE.fields_by_name['distr_info']._serialized_options = b'\xc8\xde\x1f\x01\xf2\xde\x1f\x11yaml:"distr_info"'
    _GENESISSTATE.fields_by_name['pool_to_gauges']._options = None
    _GENESISSTATE.fields_by_name['pool_to_gauges']._serialized_options = b'\xc8\xde\x1f\x01\xf2\xde\x1f\x15yaml:"pool_to_gauges"'
    _GENESISSTATE._serialized_start = 186
    _GENESISSTATE._serialized_end = 547