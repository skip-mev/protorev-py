"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'osmosis/concentrated-liquidity/tx.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xf6\x04\n\x11MsgCreatePosition\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12!\n\x06sender\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12)\n\nlower_tick\x18\x03 \x01(\x03B\x15\xf2\xde\x1f\x11yaml:"lower_tick"\x12)\n\nupper_tick\x18\x04 \x01(\x03B\x15\xf2\xde\x1f\x11yaml:"upper_tick"\x12P\n\x0etoken_desired0\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1d\xf2\xde\x1f\x15yaml:"token_desired0"\xc8\xde\x1f\x00\x12P\n\x0etoken_desired1\x18\x06 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1d\xf2\xde\x1f\x15yaml:"token_desired1"\xc8\xde\x1f\x00\x12e\n\x11token_min_amount0\x18\x07 \x01(\tBJ\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x18yaml:"token_min_amount0"\xc8\xde\x1f\x00\x12e\n\x11token_min_amount1\x18\x08 \x01(\tBJ\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x18yaml:"token_min_amount1"\xc8\xde\x1f\x00\x12Q\n\x0cfrozen_until\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x1f\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until""\xa8\x02\n\x19MsgCreatePositionResponse\x12Q\n\x07amount0\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount0"\xc8\xde\x1f\x00\x12Q\n\x07amount1\x18\x02 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount1"\xc8\xde\x1f\x00\x12e\n\x11liquidity_created\x18\x05 \x01(\tBJ\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x18yaml:"liquidity_created"\xc8\xde\x1f\x00"\xeb\x02\n\x13MsgWithdrawPosition\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12!\n\x06sender\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12)\n\nlower_tick\x18\x03 \x01(\x03B\x15\xf2\xde\x1f\x11yaml:"lower_tick"\x12)\n\nupper_tick\x18\x04 \x01(\x03B\x15\xf2\xde\x1f\x11yaml:"upper_tick"\x12c\n\x10liquidity_amount\x18\x05 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x17yaml:"liquidity_amount"\xc8\xde\x1f\x00\x12Q\n\x0cfrozen_until\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1f\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until""\xc3\x01\n\x1bMsgWithdrawPositionResponse\x12Q\n\x07amount0\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount0"\xc8\xde\x1f\x00\x12Q\n\x07amount1\x18\x02 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount1"\xc8\xde\x1f\x00"\xae\x01\n\x0eMsgCollectFees\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12!\n\x06sender\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12)\n\nlower_tick\x18\x03 \x01(\x03B\x15\xf2\xde\x1f\x11yaml:"lower_tick"\x12)\n\nupper_tick\x18\x04 \x01(\x03B\x15\xf2\xde\x1f\x11yaml:"upper_tick""`\n\x16MsgCollectFeesResponse\x12F\n\ttoken_out\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB\x18\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x002\xaf\x03\n\x03Msg\x12\x8c\x01\n\x0eCreatePosition\x128.osmosis.concentratedliquidity.v1beta1.MsgCreatePosition\x1a@.osmosis.concentratedliquidity.v1beta1.MsgCreatePositionResponse\x12\x92\x01\n\x10WithdrawPosition\x12:.osmosis.concentratedliquidity.v1beta1.MsgWithdrawPosition\x1aB.osmosis.concentratedliquidity.v1beta1.MsgWithdrawPositionResponse\x12\x83\x01\n\x0bCollectFees\x125.osmosis.concentratedliquidity.v1beta1.MsgCollectFees\x1a=.osmosis.concentratedliquidity.v1beta1.MsgCollectFeesResponseBDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/types'
    _MSGCREATEPOSITION.fields_by_name['pool_id']._options = None
    _MSGCREATEPOSITION.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGCREATEPOSITION.fields_by_name['sender']._options = None
    _MSGCREATEPOSITION.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEPOSITION.fields_by_name['lower_tick']._options = None
    _MSGCREATEPOSITION.fields_by_name['lower_tick']._serialized_options = b'\xf2\xde\x1f\x11yaml:"lower_tick"'
    _MSGCREATEPOSITION.fields_by_name['upper_tick']._options = None
    _MSGCREATEPOSITION.fields_by_name['upper_tick']._serialized_options = b'\xf2\xde\x1f\x11yaml:"upper_tick"'
    _MSGCREATEPOSITION.fields_by_name['token_desired0']._options = None
    _MSGCREATEPOSITION.fields_by_name['token_desired0']._serialized_options = b'\xf2\xde\x1f\x15yaml:"token_desired0"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITION.fields_by_name['token_desired1']._options = None
    _MSGCREATEPOSITION.fields_by_name['token_desired1']._serialized_options = b'\xf2\xde\x1f\x15yaml:"token_desired1"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITION.fields_by_name['token_min_amount0']._options = None
    _MSGCREATEPOSITION.fields_by_name['token_min_amount0']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x18yaml:"token_min_amount0"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITION.fields_by_name['token_min_amount1']._options = None
    _MSGCREATEPOSITION.fields_by_name['token_min_amount1']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x18yaml:"token_min_amount1"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITION.fields_by_name['frozen_until']._options = None
    _MSGCREATEPOSITION.fields_by_name['frozen_until']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until"'
    _MSGCREATEPOSITIONRESPONSE.fields_by_name['amount0']._options = None
    _MSGCREATEPOSITIONRESPONSE.fields_by_name['amount0']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount0"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITIONRESPONSE.fields_by_name['amount1']._options = None
    _MSGCREATEPOSITIONRESPONSE.fields_by_name['amount1']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount1"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITIONRESPONSE.fields_by_name['liquidity_created']._options = None
    _MSGCREATEPOSITIONRESPONSE.fields_by_name['liquidity_created']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x18yaml:"liquidity_created"\xc8\xde\x1f\x00'
    _MSGWITHDRAWPOSITION.fields_by_name['pool_id']._options = None
    _MSGWITHDRAWPOSITION.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGWITHDRAWPOSITION.fields_by_name['sender']._options = None
    _MSGWITHDRAWPOSITION.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGWITHDRAWPOSITION.fields_by_name['lower_tick']._options = None
    _MSGWITHDRAWPOSITION.fields_by_name['lower_tick']._serialized_options = b'\xf2\xde\x1f\x11yaml:"lower_tick"'
    _MSGWITHDRAWPOSITION.fields_by_name['upper_tick']._options = None
    _MSGWITHDRAWPOSITION.fields_by_name['upper_tick']._serialized_options = b'\xf2\xde\x1f\x11yaml:"upper_tick"'
    _MSGWITHDRAWPOSITION.fields_by_name['liquidity_amount']._options = None
    _MSGWITHDRAWPOSITION.fields_by_name['liquidity_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x17yaml:"liquidity_amount"\xc8\xde\x1f\x00'
    _MSGWITHDRAWPOSITION.fields_by_name['frozen_until']._options = None
    _MSGWITHDRAWPOSITION.fields_by_name['frozen_until']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until"'
    _MSGWITHDRAWPOSITIONRESPONSE.fields_by_name['amount0']._options = None
    _MSGWITHDRAWPOSITIONRESPONSE.fields_by_name['amount0']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount0"\xc8\xde\x1f\x00'
    _MSGWITHDRAWPOSITIONRESPONSE.fields_by_name['amount1']._options = None
    _MSGWITHDRAWPOSITIONRESPONSE.fields_by_name['amount1']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount1"\xc8\xde\x1f\x00'
    _MSGCOLLECTFEES.fields_by_name['pool_id']._options = None
    _MSGCOLLECTFEES.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _MSGCOLLECTFEES.fields_by_name['sender']._options = None
    _MSGCOLLECTFEES.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCOLLECTFEES.fields_by_name['lower_tick']._options = None
    _MSGCOLLECTFEES.fields_by_name['lower_tick']._serialized_options = b'\xf2\xde\x1f\x11yaml:"lower_tick"'
    _MSGCOLLECTFEES.fields_by_name['upper_tick']._options = None
    _MSGCOLLECTFEES.fields_by_name['upper_tick']._serialized_options = b'\xf2\xde\x1f\x11yaml:"upper_tick"'
    _MSGCOLLECTFEESRESPONSE.fields_by_name['token_out']._options = None
    _MSGCOLLECTFEESRESPONSE.fields_by_name['token_out']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00'
    _MSGCREATEPOSITION._serialized_start = 170
    _MSGCREATEPOSITION._serialized_end = 800
    _MSGCREATEPOSITIONRESPONSE._serialized_start = 803
    _MSGCREATEPOSITIONRESPONSE._serialized_end = 1099
    _MSGWITHDRAWPOSITION._serialized_start = 1102
    _MSGWITHDRAWPOSITION._serialized_end = 1465
    _MSGWITHDRAWPOSITIONRESPONSE._serialized_start = 1468
    _MSGWITHDRAWPOSITIONRESPONSE._serialized_end = 1663
    _MSGCOLLECTFEES._serialized_start = 1666
    _MSGCOLLECTFEES._serialized_end = 1840
    _MSGCOLLECTFEESRESPONSE._serialized_start = 1842
    _MSGCOLLECTFEESRESPONSE._serialized_end = 1938
    _MSG._serialized_start = 1941
    _MSG._serialized_end = 2372