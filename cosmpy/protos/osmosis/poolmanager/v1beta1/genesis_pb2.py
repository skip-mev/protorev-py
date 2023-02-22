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
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)osmosis/poolmanager/v1beta1/genesis.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x8d\x01\n\x06Params\x12\x82\x01\n\x11pool_creation_fee\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBL\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:"pool_creation_fee"\xc8\xde\x1f\x00"_\n\x0cGenesisState\x12\x14\n\x0cnext_pool_id\x18\x01 \x01(\x04\x129\n\x06params\x18\x02 \x01(\x0b2#.osmosis.poolmanager.v1beta1.ParamsB\x04\xc8\xde\x1f\x00B9Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/types'
    _PARAMS.fields_by_name['pool_creation_fee']._options = None
    _PARAMS.fields_by_name['pool_creation_fee']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:"pool_creation_fee"\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS._serialized_start = 215
    _PARAMS._serialized_end = 356
    _GENESISSTATE._serialized_start = 358
    _GENESISSTATE._serialized_end = 453