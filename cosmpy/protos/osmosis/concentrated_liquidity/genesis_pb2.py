"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ...osmosis.concentrated_liquidity import params_pb2 as osmosis_dot_concentrated__liquidity_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,osmosis/concentrated-liquidity/genesis.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a+osmosis/concentrated-liquidity/params.proto"{\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b2%.osmosis.concentratedliquidity.ParamsB\x04\xc8\xde\x1f\x00\x12.\n\x05pools\x18\x02 \x03(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolIBDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['pools']._options = None
    _GENESISSTATE.fields_by_name['pools']._serialized_options = b'\xca\xb4-\x05PoolI'
    _GENESISSTATE._serialized_start = 208
    _GENESISSTATE._serialized_end = 331