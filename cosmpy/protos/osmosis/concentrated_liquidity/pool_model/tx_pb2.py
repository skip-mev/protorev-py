"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2osmosis/concentrated-liquidity/pool-model/tx.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x87\x03\n\x19MsgCreateConcentratedPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12!\n\x06denom0\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"denom0"\x12!\n\x06denom1\x18\x03 \x01(\tB\x11\xf2\xde\x1f\ryaml:"denom1"\x12-\n\x0ctick_spacing\x18\x04 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"tick_spacing"\x12}\n\x1dprecision_factor_at_price_one\x18\x05 \x01(\tBV\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f$yaml:"precision_factor_at_price_one"\xc8\xde\x1f\x00\x12S\n\x08swap_fee\x18\t \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"swap_fee"\xc8\xde\x1f\x00"@\n!MsgCreateConcentratedPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID2\xb3\x01\n\nMsgCreator\x12\xa4\x01\n\x16CreateConcentratedPool\x12@.osmosis.concentratedliquidity.v1beta1.MsgCreateConcentratedPool\x1aH.osmosis.concentratedliquidity.v1beta1.MsgCreateConcentratedPoolResponseBDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/modelb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.pool_model.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/model'
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['sender']._options = None
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['denom0']._options = None
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['denom0']._serialized_options = b'\xf2\xde\x1f\ryaml:"denom0"'
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['denom1']._options = None
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['denom1']._serialized_options = b'\xf2\xde\x1f\ryaml:"denom1"'
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['tick_spacing']._options = None
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['tick_spacing']._serialized_options = b'\xf2\xde\x1f\x13yaml:"tick_spacing"'
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['precision_factor_at_price_one']._options = None
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['precision_factor_at_price_one']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f$yaml:"precision_factor_at_price_one"\xc8\xde\x1f\x00'
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['swap_fee']._options = None
    _MSGCREATECONCENTRATEDPOOL.fields_by_name['swap_fee']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"swap_fee"\xc8\xde\x1f\x00'
    _MSGCREATECONCENTRATEDPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATECONCENTRATEDPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGCREATECONCENTRATEDPOOL._serialized_start = 148
    _MSGCREATECONCENTRATEDPOOL._serialized_end = 539
    _MSGCREATECONCENTRATEDPOOLRESPONSE._serialized_start = 541
    _MSGCREATECONCENTRATEDPOOLRESPONSE._serialized_end = 605
    _MSGCREATOR._serialized_start = 608
    _MSGCREATOR._serialized_end = 787