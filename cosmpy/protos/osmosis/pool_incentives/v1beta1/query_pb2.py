"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
from ....osmosis.pool_incentives.v1beta1 import incentives_pb2 as osmosis_dot_pool__incentives_dot_v1beta1_dot_incentives__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+osmosis/pool-incentives/v1beta1/query.proto\x12\x1eosmosis.poolincentives.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1eosmosis/incentives/gauge.proto\x1a0osmosis/pool-incentives/v1beta1/incentives.proto";\n\x14QueryGaugeIdsRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""\xc2\x02\n\x15QueryGaugeIdsResponse\x12\x8e\x01\n\x17gauge_ids_with_duration\x18\x01 \x03(\x0b2I.osmosis.poolincentives.v1beta1.QueryGaugeIdsResponse.GaugeIdWithDurationB"\xf2\xde\x1f\x1eyaml:"gauge_ids_with_duration"\x1a\x97\x01\n\x13GaugeIdWithDuration\x12%\n\x08gauge_id\x18\x01 \x01(\x04B\x13\xf2\xde\x1f\x0fyaml:"gauge_id"\x125\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12"\n\x1agauge_incentive_percentage\x18\x03 \x01(\t"\x17\n\x15QueryDistrInfoRequest"r\n\x16QueryDistrInfoResponse\x12X\n\ndistr_info\x18\x01 \x01(\x0b2).osmosis.poolincentives.v1beta1.DistrInfoB\x19\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"distr_info""\x14\n\x12QueryParamsRequest"S\n\x13QueryParamsResponse\x12<\n\x06params\x18\x01 \x01(\x0b2&.osmosis.poolincentives.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\x1f\n\x1dQueryLockableDurationsRequest"~\n\x1eQueryLockableDurationsResponse\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations""\x1f\n\x1dQueryIncentivizedPoolsRequest"\xba\x01\n\x10IncentivizedPool\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12Z\n\x11lockable_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB$\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x18yaml:"lockable_duration"\x12%\n\x08gauge_id\x18\x03 \x01(\x04B\x13\xf2\xde\x1f\x0fyaml:"gauge_id""\x91\x01\n\x1eQueryIncentivizedPoolsResponse\x12o\n\x12incentivized_pools\x18\x01 \x03(\x0b20.osmosis.poolincentives.v1beta1.IncentivizedPoolB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"incentivized_pools""%\n#QueryExternalIncentiveGaugesRequest"U\n$QueryExternalIncentiveGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x002\xa5\t\n\x05Query\x12\xb5\x01\n\x08GaugeIds\x124.osmosis.poolincentives.v1beta1.QueryGaugeIdsRequest\x1a5.osmosis.poolincentives.v1beta1.QueryGaugeIdsResponse"<\x82\xd3\xe4\x93\x026\x124/osmosis/pool-incentives/v1beta1/gauge-ids/{pool_id}\x12\xaf\x01\n\tDistrInfo\x125.osmosis.poolincentives.v1beta1.QueryDistrInfoRequest\x1a6.osmosis.poolincentives.v1beta1.QueryDistrInfoResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/pool-incentives/v1beta1/distr_info\x12\xa2\x01\n\x06Params\x122.osmosis.poolincentives.v1beta1.QueryParamsRequest\x1a3.osmosis.poolincentives.v1beta1.QueryParamsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/osmosis/pool-incentives/v1beta1/params\x12\xcf\x01\n\x11LockableDurations\x12=.osmosis.poolincentives.v1beta1.QueryLockableDurationsRequest\x1a>.osmosis.poolincentives.v1beta1.QueryLockableDurationsResponse";\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/lockable_durations\x12\xcf\x01\n\x11IncentivizedPools\x12=.osmosis.poolincentives.v1beta1.QueryIncentivizedPoolsRequest\x1a>.osmosis.poolincentives.v1beta1.QueryIncentivizedPoolsResponse";\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/incentivized_pools\x12\xe8\x01\n\x17ExternalIncentiveGauges\x12C.osmosis.poolincentives.v1beta1.QueryExternalIncentiveGaugesRequest\x1aD.osmosis.poolincentives.v1beta1.QueryExternalIncentiveGaugesResponse"B\x82\xd3\xe4\x93\x02<\x12:/osmosis/pool-incentives/v1beta1/external_incentive_gaugesB=Z;github.com/osmosis-labs/osmosis/v14/x/pool-incentives/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.pool_incentives.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/osmosis-labs/osmosis/v14/x/pool-incentives/types'
    _QUERYGAUGEIDSREQUEST.fields_by_name['pool_id']._options = None
    _QUERYGAUGEIDSREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['gauge_id']._options = None
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['gauge_id']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"gauge_id"'
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['duration']._options = None
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _QUERYGAUGEIDSRESPONSE.fields_by_name['gauge_ids_with_duration']._options = None
    _QUERYGAUGEIDSRESPONSE.fields_by_name['gauge_ids_with_duration']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"gauge_ids_with_duration"'
    _QUERYDISTRINFORESPONSE.fields_by_name['distr_info']._options = None
    _QUERYDISTRINFORESPONSE.fields_by_name['distr_info']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"distr_info"'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._options = None
    _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"'
    _INCENTIVIZEDPOOL.fields_by_name['pool_id']._options = None
    _INCENTIVIZEDPOOL.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _INCENTIVIZEDPOOL.fields_by_name['lockable_duration']._options = None
    _INCENTIVIZEDPOOL.fields_by_name['lockable_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x18yaml:"lockable_duration"'
    _INCENTIVIZEDPOOL.fields_by_name['gauge_id']._options = None
    _INCENTIVIZEDPOOL.fields_by_name['gauge_id']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"gauge_id"'
    _QUERYINCENTIVIZEDPOOLSRESPONSE.fields_by_name['incentivized_pools']._options = None
    _QUERYINCENTIVIZEDPOOLSRESPONSE.fields_by_name['incentivized_pools']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"incentivized_pools"'
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE.fields_by_name['data']._options = None
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['GaugeIds']._options = None
    _QUERY.methods_by_name['GaugeIds']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/osmosis/pool-incentives/v1beta1/gauge-ids/{pool_id}'
    _QUERY.methods_by_name['DistrInfo']._options = None
    _QUERY.methods_by_name['DistrInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/pool-incentives/v1beta1/distr_info'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/osmosis/pool-incentives/v1beta1/params"
    _QUERY.methods_by_name['LockableDurations']._options = None
    _QUERY.methods_by_name['LockableDurations']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/lockable_durations'
    _QUERY.methods_by_name['IncentivizedPools']._options = None
    _QUERY.methods_by_name['IncentivizedPools']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/incentivized_pools'
    _QUERY.methods_by_name['ExternalIncentiveGauges']._options = None
    _QUERY.methods_by_name['ExternalIncentiveGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/osmosis/pool-incentives/v1beta1/external_incentive_gauges'
    _QUERYGAUGEIDSREQUEST._serialized_start = 245
    _QUERYGAUGEIDSREQUEST._serialized_end = 304
    _QUERYGAUGEIDSRESPONSE._serialized_start = 307
    _QUERYGAUGEIDSRESPONSE._serialized_end = 629
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION._serialized_start = 478
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION._serialized_end = 629
    _QUERYDISTRINFOREQUEST._serialized_start = 631
    _QUERYDISTRINFOREQUEST._serialized_end = 654
    _QUERYDISTRINFORESPONSE._serialized_start = 656
    _QUERYDISTRINFORESPONSE._serialized_end = 770
    _QUERYPARAMSREQUEST._serialized_start = 772
    _QUERYPARAMSREQUEST._serialized_end = 792
    _QUERYPARAMSRESPONSE._serialized_start = 794
    _QUERYPARAMSRESPONSE._serialized_end = 877
    _QUERYLOCKABLEDURATIONSREQUEST._serialized_start = 879
    _QUERYLOCKABLEDURATIONSREQUEST._serialized_end = 910
    _QUERYLOCKABLEDURATIONSRESPONSE._serialized_start = 912
    _QUERYLOCKABLEDURATIONSRESPONSE._serialized_end = 1038
    _QUERYINCENTIVIZEDPOOLSREQUEST._serialized_start = 1040
    _QUERYINCENTIVIZEDPOOLSREQUEST._serialized_end = 1071
    _INCENTIVIZEDPOOL._serialized_start = 1074
    _INCENTIVIZEDPOOL._serialized_end = 1260
    _QUERYINCENTIVIZEDPOOLSRESPONSE._serialized_start = 1263
    _QUERYINCENTIVIZEDPOOLSRESPONSE._serialized_end = 1408
    _QUERYEXTERNALINCENTIVEGAUGESREQUEST._serialized_start = 1410
    _QUERYEXTERNALINCENTIVEGAUGESREQUEST._serialized_end = 1447
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE._serialized_start = 1449
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE._serialized_end = 1534
    _QUERY._serialized_start = 1537
    _QUERY._serialized_end = 2726