"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....osmosis.poolmanager.v1beta1 import swap_route_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_swap__route__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$osmosis/poolmanager/v1beta1/tx.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a,osmosis/poolmanager/v1beta1/swap_route.proto"\xb2\x02\n\x14MsgSwapExactAmountIn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12D\n\x06routes\x18\x02 \x03(\x0b2..osmosis.poolmanager.v1beta1.SwapAmountInRouteB\x04\xc8\xde\x1f\x00\x12D\n\x08token_in\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"token_in"\xc8\xde\x1f\x00\x12k\n\x14token_out_min_amount\x18\x04 \x01(\tBM\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"token_out_min_amount"\xc8\xde\x1f\x00"\x83\x01\n\x1cMsgSwapExactAmountInResponse\x12c\n\x10token_out_amount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00"\xb4\x02\n\x15MsgSwapExactAmountOut\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12E\n\x06routes\x18\x02 \x03(\x0b2/.osmosis.poolmanager.v1beta1.SwapAmountOutRouteB\x04\xc8\xde\x1f\x00\x12i\n\x13token_in_max_amount\x18\x03 \x01(\tBL\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"token_in_max_amount"\xc8\xde\x1f\x00\x12F\n\ttoken_out\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x18\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00"\x82\x01\n\x1dMsgSwapExactAmountOutResponse\x12a\n\x0ftoken_in_amount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x002\x90\x02\n\x03Msg\x12\x81\x01\n\x11SwapExactAmountIn\x121.osmosis.poolmanager.v1beta1.MsgSwapExactAmountIn\x1a9.osmosis.poolmanager.v1beta1.MsgSwapExactAmountInResponse\x12\x84\x01\n\x12SwapExactAmountOut\x122.osmosis.poolmanager.v1beta1.MsgSwapExactAmountOut\x1a:.osmosis.poolmanager.v1beta1.MsgSwapExactAmountOutResponseB9Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/types'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['sender']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['routes']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['routes']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['token_in']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['token_in']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['token_out_min_amount']._options = None
    _MSGSWAPEXACTAMOUNTIN.fields_by_name['token_out_min_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:"token_out_min_amount"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTINRESPONSE.fields_by_name['token_out_amount']._options = None
    _MSGSWAPEXACTAMOUNTINRESPONSE.fields_by_name['token_out_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['sender']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['routes']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['routes']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['token_in_max_amount']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['token_in_max_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"token_in_max_amount"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['token_out']._options = None
    _MSGSWAPEXACTAMOUNTOUT.fields_by_name['token_out']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['token_in_amount']._options = None
    _MSGSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['token_in_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00'
    _MSGSWAPEXACTAMOUNTIN._serialized_start = 170
    _MSGSWAPEXACTAMOUNTIN._serialized_end = 476
    _MSGSWAPEXACTAMOUNTINRESPONSE._serialized_start = 479
    _MSGSWAPEXACTAMOUNTINRESPONSE._serialized_end = 610
    _MSGSWAPEXACTAMOUNTOUT._serialized_start = 613
    _MSGSWAPEXACTAMOUNTOUT._serialized_end = 921
    _MSGSWAPEXACTAMOUNTOUTRESPONSE._serialized_start = 924
    _MSGSWAPEXACTAMOUNTOUTRESPONSE._serialized_end = 1054
    _MSG._serialized_start = 1057
    _MSG._serialized_end = 1329