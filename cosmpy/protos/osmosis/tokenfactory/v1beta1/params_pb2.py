"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.tokenfactory.v1beta1 import authorityMetadata_pb2 as osmosis_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)osmosis/tokenfactory/v1beta1/params.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a4osmosis/tokenfactory/v1beta1/authorityMetadata.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x8f\x01\n\x06Params\x12\x84\x01\n\x12denom_creation_fee\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBM\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x19yaml:"denom_creation_fee"\xc8\xde\x1f\x00B:Z8github.com/osmosis-labs/osmosis/v14/x/tokenfactory/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.tokenfactory.v1beta1.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/osmosis-labs/osmosis/v14/x/tokenfactory/types'
    _PARAMS.fields_by_name['denom_creation_fee']._options = None
    _PARAMS.fields_by_name['denom_creation_fee']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x19yaml:"denom_creation_fee"\xc8\xde\x1f\x00'
    _PARAMS._serialized_start = 211
    _PARAMS._serialized_end = 354