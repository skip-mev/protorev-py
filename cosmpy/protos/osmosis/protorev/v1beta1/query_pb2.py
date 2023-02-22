"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....osmosis.protorev.v1beta1 import params_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_params__pb2
from ....osmosis.protorev.v1beta1 import protorev_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_protorev__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$osmosis/protorev/v1beta1/query.proto\x12\x18osmosis.protorev.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a%osmosis/protorev/v1beta1/params.proto\x1a\'osmosis/protorev/v1beta1/protorev.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x14\n\x12QueryParamsRequest"M\n\x13QueryParamsResponse\x126\n\x06params\x18\x01 \x01(\x0b2 .osmosis.protorev.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\'\n%QueryGetProtoRevNumberOfTradesRequest"r\n&QueryGetProtoRevNumberOfTradesResponse\x12H\n\x10number_of_trades\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"6\n%QueryGetProtoRevProfitsByDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t"S\n&QueryGetProtoRevProfitsByDenomResponse\x12)\n\x06profit\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.Coin"#\n!QueryGetProtoRevAllProfitsRequest"P\n"QueryGetProtoRevAllProfitsResponse\x12*\n\x07profits\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.Coin"9\n(QueryGetProtoRevStatisticsByRouteRequest\x12\r\n\x05route\x18\x01 \x03(\x04"j\n)QueryGetProtoRevStatisticsByRouteResponse\x12=\n\nstatistics\x18\x01 \x01(\x0b2).osmosis.protorev.v1beta1.RouteStatistics"+\n)QueryGetProtoRevAllRouteStatisticsRequest"q\n*QueryGetProtoRevAllRouteStatisticsResponse\x12C\n\nstatistics\x18\x01 \x03(\x0b2).osmosis.protorev.v1beta1.RouteStatisticsB\x04\xc8\xde\x1f\x00"+\n)QueryGetProtoRevTokenPairArbRoutesRequest"j\n*QueryGetProtoRevTokenPairArbRoutesResponse\x12<\n\x06routes\x18\x01 \x03(\x0b2,.osmosis.protorev.v1beta1.TokenPairArbRoutes"%\n#QueryGetProtoRevAdminAccountRequest"=\n$QueryGetProtoRevAdminAccountResponse\x12\x15\n\radmin_account\x18\x01 \x01(\t")\n\'QueryGetProtoRevDeveloperAccountRequest"E\n(QueryGetProtoRevDeveloperAccountResponse\x12\x19\n\x11developer_account\x18\x01 \x01(\t"$\n"QueryGetProtoRevPoolWeightsRequest"b\n#QueryGetProtoRevPoolWeightsResponse\x12;\n\x0cpool_weights\x18\x01 \x01(\x0b2%.osmosis.protorev.v1beta1.PoolWeights".\n,QueryGetProtoRevMaxPoolPointsPerBlockRequest"R\n-QueryGetProtoRevMaxPoolPointsPerBlockResponse\x12!\n\x19max_pool_points_per_block\x18\x01 \x01(\x04"+\n)QueryGetProtoRevMaxPoolPointsPerTxRequest"L\n*QueryGetProtoRevMaxPoolPointsPerTxResponse\x12\x1e\n\x16max_pool_points_per_tx\x18\x01 \x01(\x04"#\n!QueryGetProtoRevBaseDenomsRequest"^\n"QueryGetProtoRevBaseDenomsResponse\x128\n\x0bbase_denoms\x18\x01 \x03(\x0b2#.osmosis.protorev.v1beta1.BaseDenom" \n\x1eQueryGetProtoRevEnabledRequest"2\n\x1fQueryGetProtoRevEnabledResponse\x12\x0f\n\x07enabled\x18\x01 \x01(\x082\xc0\x16\n\x05Query\x12\x8b\x01\n\x06Params\x12,.osmosis.protorev.v1beta1.QueryParamsRequest\x1a-.osmosis.protorev.v1beta1.QueryParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/v14/protorev/params\x12\xce\x01\n\x19GetProtoRevNumberOfTrades\x12?.osmosis.protorev.v1beta1.QueryGetProtoRevNumberOfTradesRequest\x1a@.osmosis.protorev.v1beta1.QueryGetProtoRevNumberOfTradesResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/v14/protorev/number_of_trades\x12\xce\x01\n\x19GetProtoRevProfitsByDenom\x12?.osmosis.protorev.v1beta1.QueryGetProtoRevProfitsByDenomRequest\x1a@.osmosis.protorev.v1beta1.QueryGetProtoRevProfitsByDenomResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/v14/protorev/profits_by_denom\x12\xbd\x01\n\x15GetProtoRevAllProfits\x12;.osmosis.protorev.v1beta1.QueryGetProtoRevAllProfitsRequest\x1a<.osmosis.protorev.v1beta1.QueryGetProtoRevAllProfitsResponse")\x82\xd3\xe4\x93\x02#\x12!/osmosis/v14/protorev/all_profits\x12\xda\x01\n\x1cGetProtoRevStatisticsByRoute\x12B.osmosis.protorev.v1beta1.QueryGetProtoRevStatisticsByRouteRequest\x1aC.osmosis.protorev.v1beta1.QueryGetProtoRevStatisticsByRouteResponse"1\x82\xd3\xe4\x93\x02+\x12)/osmosis/v14/protorev/statistics_by_route\x12\xde\x01\n\x1dGetProtoRevAllRouteStatistics\x12C.osmosis.protorev.v1beta1.QueryGetProtoRevAllRouteStatisticsRequest\x1aD.osmosis.protorev.v1beta1.QueryGetProtoRevAllRouteStatisticsResponse"2\x82\xd3\xe4\x93\x02,\x12*/osmosis/v14/protorev/all_route_statistics\x12\xdf\x01\n\x1dGetProtoRevTokenPairArbRoutes\x12C.osmosis.protorev.v1beta1.QueryGetProtoRevTokenPairArbRoutesRequest\x1aD.osmosis.protorev.v1beta1.QueryGetProtoRevTokenPairArbRoutesResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/v14/protorev/token_pair_arb_routes\x12\xc5\x01\n\x17GetProtoRevAdminAccount\x12=.osmosis.protorev.v1beta1.QueryGetProtoRevAdminAccountRequest\x1a>.osmosis.protorev.v1beta1.QueryGetProtoRevAdminAccountResponse"+\x82\xd3\xe4\x93\x02%\x12#/osmosis/v14/protorev/admin_account\x12\xd5\x01\n\x1bGetProtoRevDeveloperAccount\x12A.osmosis.protorev.v1beta1.QueryGetProtoRevDeveloperAccountRequest\x1aB.osmosis.protorev.v1beta1.QueryGetProtoRevDeveloperAccountResponse"/\x82\xd3\xe4\x93\x02)\x12\'/osmosis/v14/protorev/developer_account\x12\xc1\x01\n\x16GetProtoRevPoolWeights\x12<.osmosis.protorev.v1beta1.QueryGetProtoRevPoolWeightsRequest\x1a=.osmosis.protorev.v1beta1.QueryGetProtoRevPoolWeightsResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/v14/protorev/pool_weights\x12\xe0\x01\n\x1dGetProtoRevMaxPoolPointsPerTx\x12C.osmosis.protorev.v1beta1.QueryGetProtoRevMaxPoolPointsPerTxRequest\x1aD.osmosis.protorev.v1beta1.QueryGetProtoRevMaxPoolPointsPerTxResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/v14/protorev/max_pool_points_per_tx\x12\xec\x01\n GetProtoRevMaxPoolPointsPerBlock\x12F.osmosis.protorev.v1beta1.QueryGetProtoRevMaxPoolPointsPerBlockRequest\x1aG.osmosis.protorev.v1beta1.QueryGetProtoRevMaxPoolPointsPerBlockResponse"7\x82\xd3\xe4\x93\x021\x12//osmosis/v14/protorev/max_pool_points_per_block\x12\xbd\x01\n\x15GetProtoRevBaseDenoms\x12;.osmosis.protorev.v1beta1.QueryGetProtoRevBaseDenomsRequest\x1a<.osmosis.protorev.v1beta1.QueryGetProtoRevBaseDenomsResponse")\x82\xd3\xe4\x93\x02#\x12!/osmosis/v14/protorev/base_denoms\x12\xb0\x01\n\x12GetProtoRevEnabled\x128.osmosis.protorev.v1beta1.QueryGetProtoRevEnabledRequest\x1a9.osmosis.protorev.v1beta1.QueryGetProtoRevEnabledResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/osmosis/v14/protorev/enabledB6Z4github.com/osmosis-labs/osmosis/v14/x/protorev/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.protorev.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/osmosis-labs/osmosis/v14/x/protorev/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYGETPROTOREVNUMBEROFTRADESRESPONSE.fields_by_name['number_of_trades']._options = None
    _QUERYGETPROTOREVNUMBEROFTRADESRESPONSE.fields_by_name['number_of_trades']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERYGETPROTOREVALLROUTESTATISTICSRESPONSE.fields_by_name['statistics']._options = None
    _QUERYGETPROTOREVALLROUTESTATISTICSRESPONSE.fields_by_name['statistics']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/v14/protorev/params'
    _QUERY.methods_by_name['GetProtoRevNumberOfTrades']._options = None
    _QUERY.methods_by_name['GetProtoRevNumberOfTrades']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/v14/protorev/number_of_trades'
    _QUERY.methods_by_name['GetProtoRevProfitsByDenom']._options = None
    _QUERY.methods_by_name['GetProtoRevProfitsByDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/v14/protorev/profits_by_denom'
    _QUERY.methods_by_name['GetProtoRevAllProfits']._options = None
    _QUERY.methods_by_name['GetProtoRevAllProfits']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/osmosis/v14/protorev/all_profits'
    _QUERY.methods_by_name['GetProtoRevStatisticsByRoute']._options = None
    _QUERY.methods_by_name['GetProtoRevStatisticsByRoute']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/osmosis/v14/protorev/statistics_by_route'
    _QUERY.methods_by_name['GetProtoRevAllRouteStatistics']._options = None
    _QUERY.methods_by_name['GetProtoRevAllRouteStatistics']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/osmosis/v14/protorev/all_route_statistics'
    _QUERY.methods_by_name['GetProtoRevTokenPairArbRoutes']._options = None
    _QUERY.methods_by_name['GetProtoRevTokenPairArbRoutes']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/v14/protorev/token_pair_arb_routes'
    _QUERY.methods_by_name['GetProtoRevAdminAccount']._options = None
    _QUERY.methods_by_name['GetProtoRevAdminAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/osmosis/v14/protorev/admin_account'
    _QUERY.methods_by_name['GetProtoRevDeveloperAccount']._options = None
    _QUERY.methods_by_name['GetProtoRevDeveloperAccount']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/osmosis/v14/protorev/developer_account"
    _QUERY.methods_by_name['GetProtoRevPoolWeights']._options = None
    _QUERY.methods_by_name['GetProtoRevPoolWeights']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/v14/protorev/pool_weights'
    _QUERY.methods_by_name['GetProtoRevMaxPoolPointsPerTx']._options = None
    _QUERY.methods_by_name['GetProtoRevMaxPoolPointsPerTx']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/v14/protorev/max_pool_points_per_tx'
    _QUERY.methods_by_name['GetProtoRevMaxPoolPointsPerBlock']._options = None
    _QUERY.methods_by_name['GetProtoRevMaxPoolPointsPerBlock']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//osmosis/v14/protorev/max_pool_points_per_block'
    _QUERY.methods_by_name['GetProtoRevBaseDenoms']._options = None
    _QUERY.methods_by_name['GetProtoRevBaseDenoms']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/osmosis/v14/protorev/base_denoms'
    _QUERY.methods_by_name['GetProtoRevEnabled']._options = None
    _QUERY.methods_by_name['GetProtoRevEnabled']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/osmosis/v14/protorev/enabled'
    _QUERYPARAMSREQUEST._serialized_start = 274
    _QUERYPARAMSREQUEST._serialized_end = 294
    _QUERYPARAMSRESPONSE._serialized_start = 296
    _QUERYPARAMSRESPONSE._serialized_end = 373
    _QUERYGETPROTOREVNUMBEROFTRADESREQUEST._serialized_start = 375
    _QUERYGETPROTOREVNUMBEROFTRADESREQUEST._serialized_end = 414
    _QUERYGETPROTOREVNUMBEROFTRADESRESPONSE._serialized_start = 416
    _QUERYGETPROTOREVNUMBEROFTRADESRESPONSE._serialized_end = 530
    _QUERYGETPROTOREVPROFITSBYDENOMREQUEST._serialized_start = 532
    _QUERYGETPROTOREVPROFITSBYDENOMREQUEST._serialized_end = 586
    _QUERYGETPROTOREVPROFITSBYDENOMRESPONSE._serialized_start = 588
    _QUERYGETPROTOREVPROFITSBYDENOMRESPONSE._serialized_end = 671
    _QUERYGETPROTOREVALLPROFITSREQUEST._serialized_start = 673
    _QUERYGETPROTOREVALLPROFITSREQUEST._serialized_end = 708
    _QUERYGETPROTOREVALLPROFITSRESPONSE._serialized_start = 710
    _QUERYGETPROTOREVALLPROFITSRESPONSE._serialized_end = 790
    _QUERYGETPROTOREVSTATISTICSBYROUTEREQUEST._serialized_start = 792
    _QUERYGETPROTOREVSTATISTICSBYROUTEREQUEST._serialized_end = 849
    _QUERYGETPROTOREVSTATISTICSBYROUTERESPONSE._serialized_start = 851
    _QUERYGETPROTOREVSTATISTICSBYROUTERESPONSE._serialized_end = 957
    _QUERYGETPROTOREVALLROUTESTATISTICSREQUEST._serialized_start = 959
    _QUERYGETPROTOREVALLROUTESTATISTICSREQUEST._serialized_end = 1002
    _QUERYGETPROTOREVALLROUTESTATISTICSRESPONSE._serialized_start = 1004
    _QUERYGETPROTOREVALLROUTESTATISTICSRESPONSE._serialized_end = 1117
    _QUERYGETPROTOREVTOKENPAIRARBROUTESREQUEST._serialized_start = 1119
    _QUERYGETPROTOREVTOKENPAIRARBROUTESREQUEST._serialized_end = 1162
    _QUERYGETPROTOREVTOKENPAIRARBROUTESRESPONSE._serialized_start = 1164
    _QUERYGETPROTOREVTOKENPAIRARBROUTESRESPONSE._serialized_end = 1270
    _QUERYGETPROTOREVADMINACCOUNTREQUEST._serialized_start = 1272
    _QUERYGETPROTOREVADMINACCOUNTREQUEST._serialized_end = 1309
    _QUERYGETPROTOREVADMINACCOUNTRESPONSE._serialized_start = 1311
    _QUERYGETPROTOREVADMINACCOUNTRESPONSE._serialized_end = 1372
    _QUERYGETPROTOREVDEVELOPERACCOUNTREQUEST._serialized_start = 1374
    _QUERYGETPROTOREVDEVELOPERACCOUNTREQUEST._serialized_end = 1415
    _QUERYGETPROTOREVDEVELOPERACCOUNTRESPONSE._serialized_start = 1417
    _QUERYGETPROTOREVDEVELOPERACCOUNTRESPONSE._serialized_end = 1486
    _QUERYGETPROTOREVPOOLWEIGHTSREQUEST._serialized_start = 1488
    _QUERYGETPROTOREVPOOLWEIGHTSREQUEST._serialized_end = 1524
    _QUERYGETPROTOREVPOOLWEIGHTSRESPONSE._serialized_start = 1526
    _QUERYGETPROTOREVPOOLWEIGHTSRESPONSE._serialized_end = 1624
    _QUERYGETPROTOREVMAXPOOLPOINTSPERBLOCKREQUEST._serialized_start = 1626
    _QUERYGETPROTOREVMAXPOOLPOINTSPERBLOCKREQUEST._serialized_end = 1672
    _QUERYGETPROTOREVMAXPOOLPOINTSPERBLOCKRESPONSE._serialized_start = 1674
    _QUERYGETPROTOREVMAXPOOLPOINTSPERBLOCKRESPONSE._serialized_end = 1756
    _QUERYGETPROTOREVMAXPOOLPOINTSPERTXREQUEST._serialized_start = 1758
    _QUERYGETPROTOREVMAXPOOLPOINTSPERTXREQUEST._serialized_end = 1801
    _QUERYGETPROTOREVMAXPOOLPOINTSPERTXRESPONSE._serialized_start = 1803
    _QUERYGETPROTOREVMAXPOOLPOINTSPERTXRESPONSE._serialized_end = 1879
    _QUERYGETPROTOREVBASEDENOMSREQUEST._serialized_start = 1881
    _QUERYGETPROTOREVBASEDENOMSREQUEST._serialized_end = 1916
    _QUERYGETPROTOREVBASEDENOMSRESPONSE._serialized_start = 1918
    _QUERYGETPROTOREVBASEDENOMSRESPONSE._serialized_end = 2012
    _QUERYGETPROTOREVENABLEDREQUEST._serialized_start = 2014
    _QUERYGETPROTOREVENABLEDREQUEST._serialized_end = 2046
    _QUERYGETPROTOREVENABLEDRESPONSE._serialized_start = 2048
    _QUERYGETPROTOREVENABLEDRESPONSE._serialized_end = 2098
    _QUERY._serialized_start = 2101
    _QUERY._serialized_end = 4981