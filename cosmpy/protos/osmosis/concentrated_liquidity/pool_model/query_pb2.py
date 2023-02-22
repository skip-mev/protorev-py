"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.concentrated_liquidity import params_pb2 as osmosis_dot_concentrated__liquidity_dot_params__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5osmosis/concentrated-liquidity/pool-model/query.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto\x1a+osmosis/concentrated-liquidity/params.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto"@\n\x19QueryUserPositionsRequest\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address""w\n\x1aQueryUserPositionsResponse\x12Y\n\tpositions\x18\x01 \x03(\x0b2@.osmosis.concentratedliquidity.v1beta1.FullPositionByOwnerResultB\x04\xc8\xde\x1f\x00"\x92\x02\n\x19FullPositionByOwnerResult\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12\x12\n\nlower_tick\x18\x02 \x01(\x03\x12\x12\n\nupper_tick\x18\x03 \x01(\x03\x12Q\n\x0cfrozen_until\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1f\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until"\x12U\n\tliquidity\x18\x05 \x01(\tBB\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00"7\n\x10QueryPoolRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""B\n\x11QueryPoolResponse\x12-\n\x04pool\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI"O\n\x11QueryPoolsRequest\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x81\x01\n\x12QueryPoolsResponse\x12.\n\x05pools\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x14\n\x12QueryParamsRequest"R\n\x13QueryParamsResponse\x12;\n\x06params\x18\x01 \x01(\x0b2%.osmosis.concentratedliquidity.ParamsB\x04\xc8\xde\x1f\x00"\xfc\x01\n#QueryLiquidityDepthsForRangeRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12W\n\nlower_tick\x18\x02 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"lower_tick"\xc8\xde\x1f\x00\x12W\n\nupper_tick\x18\x03 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"upper_tick"\xc8\xde\x1f\x00"}\n$QueryLiquidityDepthsForRangeResponse\x12U\n\x10liquidity_depths\x18\x01 \x03(\x0b25.osmosis.concentratedliquidity.v1beta1.LiquidityDepthB\x04\xc8\xde\x1f\x00"\xc2\x01\n\x0eLiquidityDepth\x12]\n\rliquidity_net\x18\x01 \x01(\tBF\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x14yaml:"liquidity_net"\xc8\xde\x1f\x00\x12Q\n\ntick_index\x18\x02 \x01(\tB=\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0byaml:"tick"\xc8\xde\x1f\x002\x8c\x08\n\x05Query\x12\xb2\x01\n\x05Pools\x128.osmosis.concentratedliquidity.v1beta1.QueryPoolsRequest\x1a9.osmosis.concentratedliquidity.v1beta1.QueryPoolsResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/concentratedliquidity/v1beta1/pools\x12\xb9\x01\n\x04Pool\x127.osmosis.concentratedliquidity.v1beta1.QueryPoolRequest\x1a8.osmosis.concentratedliquidity.v1beta1.QueryPoolResponse">\x82\xd3\xe4\x93\x028\x126/osmosis/concentratedliquidity/v1beta1/pools/{pool_id}\x12\xb6\x01\n\x06Params\x129.osmosis.concentratedliquidity.v1beta1.QueryParamsRequest\x1a:.osmosis.concentratedliquidity.v1beta1.QueryParamsResponse"5\x82\xd3\xe4\x93\x02/\x12-/osmosis/concentratedliquidity/v1beta1/params\x12\xfd\x01\n\x17LiquidityDepthsForRange\x12J.osmosis.concentratedliquidity.v1beta1.QueryLiquidityDepthsForRangeRequest\x1aK.osmosis.concentratedliquidity.v1beta1.QueryLiquidityDepthsForRangeResponse"I\x82\xd3\xe4\x93\x02C\x12A/osmosis/concentratedliquidity/v1beta1/liquidity_depths_for_range\x12\xd8\x01\n\rUserPositions\x12@.osmosis.concentratedliquidity.v1beta1.QueryUserPositionsRequest\x1aA.osmosis.concentratedliquidity.v1beta1.QueryUserPositionsResponse"B\x82\xd3\xe4\x93\x02<\x12:/osmosis/concentratedliquidity/v1beta1/positions/{address}BDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.pool_model.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/types'
    _QUERYUSERPOSITIONSREQUEST.fields_by_name['address']._options = None
    _QUERYUSERPOSITIONSREQUEST.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _QUERYUSERPOSITIONSRESPONSE.fields_by_name['positions']._options = None
    _QUERYUSERPOSITIONSRESPONSE.fields_by_name['positions']._serialized_options = b'\xc8\xde\x1f\x00'
    _FULLPOSITIONBYOWNERRESULT.fields_by_name['pool_id']._options = None
    _FULLPOSITIONBYOWNERRESULT.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _FULLPOSITIONBYOWNERRESULT.fields_by_name['frozen_until']._options = None
    _FULLPOSITIONBYOWNERRESULT.fields_by_name['frozen_until']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until"'
    _FULLPOSITIONBYOWNERRESULT.fields_by_name['liquidity']._options = None
    _FULLPOSITIONBYOWNERRESULT.fields_by_name['liquidity']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00'
    _QUERYPOOLREQUEST.fields_by_name['pool_id']._options = None
    _QUERYPOOLREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYPOOLRESPONSE.fields_by_name['pool']._options = None
    _QUERYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\xca\xb4-\x05PoolI'
    _QUERYPOOLSRESPONSE.fields_by_name['pools']._options = None
    _QUERYPOOLSRESPONSE.fields_by_name['pools']._serialized_options = b'\xca\xb4-\x05PoolI'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST.fields_by_name['pool_id']._options = None
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST.fields_by_name['lower_tick']._options = None
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST.fields_by_name['lower_tick']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"lower_tick"\xc8\xde\x1f\x00'
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST.fields_by_name['upper_tick']._options = None
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST.fields_by_name['upper_tick']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"upper_tick"\xc8\xde\x1f\x00'
    _QUERYLIQUIDITYDEPTHSFORRANGERESPONSE.fields_by_name['liquidity_depths']._options = None
    _QUERYLIQUIDITYDEPTHSFORRANGERESPONSE.fields_by_name['liquidity_depths']._serialized_options = b'\xc8\xde\x1f\x00'
    _LIQUIDITYDEPTH.fields_by_name['liquidity_net']._options = None
    _LIQUIDITYDEPTH.fields_by_name['liquidity_net']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x14yaml:"liquidity_net"\xc8\xde\x1f\x00'
    _LIQUIDITYDEPTH.fields_by_name['tick_index']._options = None
    _LIQUIDITYDEPTH.fields_by_name['tick_index']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0byaml:"tick"\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Pools']._options = None
    _QUERY.methods_by_name['Pools']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/concentratedliquidity/v1beta1/pools'
    _QUERY.methods_by_name['Pool']._options = None
    _QUERY.methods_by_name['Pool']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/osmosis/concentratedliquidity/v1beta1/pools/{pool_id}'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/osmosis/concentratedliquidity/v1beta1/params'
    _QUERY.methods_by_name['LiquidityDepthsForRange']._options = None
    _QUERY.methods_by_name['LiquidityDepthsForRange']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/osmosis/concentratedliquidity/v1beta1/liquidity_depths_for_range'
    _QUERY.methods_by_name['UserPositions']._options = None
    _QUERY.methods_by_name['UserPositions']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/osmosis/concentratedliquidity/v1beta1/positions/{address}'
    _QUERYUSERPOSITIONSREQUEST._serialized_start = 356
    _QUERYUSERPOSITIONSREQUEST._serialized_end = 420
    _QUERYUSERPOSITIONSRESPONSE._serialized_start = 422
    _QUERYUSERPOSITIONSRESPONSE._serialized_end = 541
    _FULLPOSITIONBYOWNERRESULT._serialized_start = 544
    _FULLPOSITIONBYOWNERRESULT._serialized_end = 818
    _QUERYPOOLREQUEST._serialized_start = 820
    _QUERYPOOLREQUEST._serialized_end = 875
    _QUERYPOOLRESPONSE._serialized_start = 877
    _QUERYPOOLRESPONSE._serialized_end = 943
    _QUERYPOOLSREQUEST._serialized_start = 945
    _QUERYPOOLSREQUEST._serialized_end = 1024
    _QUERYPOOLSRESPONSE._serialized_start = 1027
    _QUERYPOOLSRESPONSE._serialized_end = 1156
    _QUERYPARAMSREQUEST._serialized_start = 1158
    _QUERYPARAMSREQUEST._serialized_end = 1178
    _QUERYPARAMSRESPONSE._serialized_start = 1180
    _QUERYPARAMSRESPONSE._serialized_end = 1262
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST._serialized_start = 1265
    _QUERYLIQUIDITYDEPTHSFORRANGEREQUEST._serialized_end = 1517
    _QUERYLIQUIDITYDEPTHSFORRANGERESPONSE._serialized_start = 1519
    _QUERYLIQUIDITYDEPTHSFORRANGERESPONSE._serialized_end = 1644
    _LIQUIDITYDEPTH._serialized_start = 1647
    _LIQUIDITYDEPTH._serialized_end = 1841
    _QUERY._serialized_start = 1844
    _QUERY._serialized_end = 2880