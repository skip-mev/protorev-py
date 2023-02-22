"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)osmosis/concentrated-liquidity/pool.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto"\x82\x05\n\x04Pool\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\n\n\x02id\x18\x02 \x01(\x04\x12U\n\tliquidity\x18\x03 \x01(\tBB\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00\x12\x0e\n\x06token0\x18\x04 \x01(\t\x12\x0e\n\x06token1\x18\x05 \x01(\t\x12_\n\x12current_sqrt_price\x18\x06 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x11yaml:"spot_price"\xc8\xde\x1f\x00\x12[\n\x0ccurrent_tick\x18\x07 \x01(\tBE\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:"current_tick"\xc8\xde\x1f\x00\x12-\n\x0ctick_spacing\x18\x08 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"tick_spacing"\x12}\n\x1dprecision_factor_at_price_one\x18\t \x01(\tBV\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f$yaml:"precision_factor_at_price_one"\xc8\xde\x1f\x00\x12S\n\x08swap_fee\x18\n \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"swap_fee"\xc8\xde\x1f\x00:\x11\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x05PoolIBDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/modelb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.pool_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/model'
    _POOL.fields_by_name['address']._options = None
    _POOL.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _POOL.fields_by_name['liquidity']._options = None
    _POOL.fields_by_name['liquidity']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00'
    _POOL.fields_by_name['current_sqrt_price']._options = None
    _POOL.fields_by_name['current_sqrt_price']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x11yaml:"spot_price"\xc8\xde\x1f\x00'
    _POOL.fields_by_name['current_tick']._options = None
    _POOL.fields_by_name['current_tick']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:"current_tick"\xc8\xde\x1f\x00'
    _POOL.fields_by_name['tick_spacing']._options = None
    _POOL.fields_by_name['tick_spacing']._serialized_options = b'\xf2\xde\x1f\x13yaml:"tick_spacing"'
    _POOL.fields_by_name['precision_factor_at_price_one']._options = None
    _POOL.fields_by_name['precision_factor_at_price_one']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f$yaml:"precision_factor_at_price_one"\xc8\xde\x1f\x00'
    _POOL.fields_by_name['swap_fee']._options = None
    _POOL.fields_by_name['swap_fee']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"swap_fee"\xc8\xde\x1f\x00'
    _POOL._options = None
    _POOL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x05PoolI'
    _POOL._serialized_start = 134
    _POOL._serialized_end = 776