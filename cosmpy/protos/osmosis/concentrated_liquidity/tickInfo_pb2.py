"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-osmosis/concentrated-liquidity/tickInfo.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xbb\x02\n\x08TickInfo\x12a\n\x0fliquidity_gross\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"liquidity_gross"\xc8\xde\x1f\x00\x12]\n\rliquidity_net\x18\x02 \x01(\tBF\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x14yaml:"liquidity_net"\xc8\xde\x1f\x00\x12m\n\x12fee_growth_outside\x18\x03 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00BDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/modelb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.tickInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/model'
    _TICKINFO.fields_by_name['liquidity_gross']._options = None
    _TICKINFO.fields_by_name['liquidity_gross']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"liquidity_gross"\xc8\xde\x1f\x00'
    _TICKINFO.fields_by_name['liquidity_net']._options = None
    _TICKINFO.fields_by_name['liquidity_net']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x14yaml:"liquidity_net"\xc8\xde\x1f\x00'
    _TICKINFO.fields_by_name['fee_growth_outside']._options = None
    _TICKINFO.fields_by_name['fee_growth_outside']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _TICKINFO._serialized_start = 170
    _TICKINFO._serialized_end = 485