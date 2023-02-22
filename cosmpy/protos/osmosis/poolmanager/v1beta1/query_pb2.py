"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.poolmanager.v1beta1 import genesis_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_genesis__pb2
from ....osmosis.poolmanager.v1beta1 import tx_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_tx__pb2
from ....osmosis.poolmanager.v1beta1 import swap_route_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_swap__route__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'osmosis/poolmanager/v1beta1/query.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto\x1a)osmosis/poolmanager/v1beta1/genesis.proto\x1a$osmosis/poolmanager/v1beta1/tx.proto\x1a,osmosis/poolmanager/v1beta1/swap_route.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x0f\n\rParamsRequest"K\n\x0eParamsResponse\x129\n\x06params\x18\x01 \x01(\x0b2#.osmosis.poolmanager.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\xe8\x01\n EstimateSwapExactAmountInRequest\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12#\n\x07pool_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12%\n\x08token_in\x18\x03 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"token_in"\x12U\n\x06routes\x18\x04 \x03(\x0b2..osmosis.poolmanager.v1beta1.SwapAmountInRouteB\x15\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00"\x88\x01\n!EstimateSwapExactAmountInResponse\x12c\n\x10token_out_amount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00"\xec\x01\n!EstimateSwapExactAmountOutRequest\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12#\n\x07pool_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12V\n\x06routes\x18\x03 \x03(\x0b2/.osmosis.poolmanager.v1beta1.SwapAmountOutRouteB\x15\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00\x12\'\n\ttoken_out\x18\x04 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"token_out""\x87\x01\n"EstimateSwapExactAmountOutResponse\x12a\n\x0ftoken_in_amount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00"\x11\n\x0fNumPoolsRequest";\n\x10NumPoolsResponse\x12\'\n\tnum_pools\x18\x01 \x01(\x04B\x14\xf2\xde\x1f\x10yaml:"num_pools"2\xfe\x05\n\x05Query\x12\x8e\x01\n\x06Params\x12*.osmosis.poolmanager.v1beta1.ParamsRequest\x1a+.osmosis.poolmanager.v1beta1.ParamsResponse"+\x82\xd3\xe4\x93\x02%\x12#/osmosis/poolmanager/v1beta1/Params\x12\xe1\x01\n\x19EstimateSwapExactAmountIn\x12=.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInRequest\x1a>.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInResponse"E\x82\xd3\xe4\x93\x02?\x12=/osmosis/gamm/v1beta1/{pool_id}/estimate/swap_exact_amount_in\x12\xe5\x01\n\x1aEstimateSwapExactAmountOut\x12>.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutRequest\x1a?.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutResponse"F\x82\xd3\xe4\x93\x02@\x12>/osmosis/gamm/v1beta1/{pool_id}/estimate/swap_exact_amount_out\x12\x97\x01\n\x08NumPools\x12,.osmosis.poolmanager.v1beta1.NumPoolsRequest\x1a-.osmosis.poolmanager.v1beta1.NumPoolsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/poolmanager/v1beta1/num_poolsBEZCgithub.com/osmosis-labs/osmosis/v14/x/poolmanager/client/queryprotob\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZCgithub.com/osmosis-labs/osmosis/v14/x/poolmanager/client/queryproto'
    _PARAMSRESPONSE.fields_by_name['params']._options = None
    _PARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['sender']._options = None
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['pool_id']._options = None
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['token_in']._options = None
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['token_in']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"'
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['routes']._options = None
    _ESTIMATESWAPEXACTAMOUNTINREQUEST.fields_by_name['routes']._serialized_options = b'\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00'
    _ESTIMATESWAPEXACTAMOUNTINRESPONSE.fields_by_name['token_out_amount']._options = None
    _ESTIMATESWAPEXACTAMOUNTINRESPONSE.fields_by_name['token_out_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00'
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['sender']._options = None
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['pool_id']._options = None
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['routes']._options = None
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['routes']._serialized_options = b'\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00'
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['token_out']._options = None
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST.fields_by_name['token_out']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"'
    _ESTIMATESWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['token_in_amount']._options = None
    _ESTIMATESWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['token_in_amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00'
    _NUMPOOLSRESPONSE.fields_by_name['num_pools']._options = None
    _NUMPOOLSRESPONSE.fields_by_name['num_pools']._serialized_options = b'\xf2\xde\x1f\x10yaml:"num_pools"'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/osmosis/poolmanager/v1beta1/Params'
    _QUERY.methods_by_name['EstimateSwapExactAmountIn']._options = None
    _QUERY.methods_by_name['EstimateSwapExactAmountIn']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/osmosis/gamm/v1beta1/{pool_id}/estimate/swap_exact_amount_in'
    _QUERY.methods_by_name['EstimateSwapExactAmountOut']._options = None
    _QUERY.methods_by_name['EstimateSwapExactAmountOut']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/osmosis/gamm/v1beta1/{pool_id}/estimate/swap_exact_amount_out'
    _QUERY.methods_by_name['NumPools']._options = None
    _QUERY.methods_by_name['NumPools']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/poolmanager/v1beta1/num_pools'
    _PARAMSREQUEST._serialized_start = 414
    _PARAMSREQUEST._serialized_end = 429
    _PARAMSRESPONSE._serialized_start = 431
    _PARAMSRESPONSE._serialized_end = 506
    _ESTIMATESWAPEXACTAMOUNTINREQUEST._serialized_start = 509
    _ESTIMATESWAPEXACTAMOUNTINREQUEST._serialized_end = 741
    _ESTIMATESWAPEXACTAMOUNTINRESPONSE._serialized_start = 744
    _ESTIMATESWAPEXACTAMOUNTINRESPONSE._serialized_end = 880
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST._serialized_start = 883
    _ESTIMATESWAPEXACTAMOUNTOUTREQUEST._serialized_end = 1119
    _ESTIMATESWAPEXACTAMOUNTOUTRESPONSE._serialized_start = 1122
    _ESTIMATESWAPEXACTAMOUNTOUTRESPONSE._serialized_end = 1257
    _NUMPOOLSREQUEST._serialized_start = 1259
    _NUMPOOLSREQUEST._serialized_end = 1276
    _NUMPOOLSRESPONSE._serialized_start = 1278
    _NUMPOOLSRESPONSE._serialized_end = 1337
    _QUERY._serialized_start = 1340
    _QUERY._serialized_end = 2106