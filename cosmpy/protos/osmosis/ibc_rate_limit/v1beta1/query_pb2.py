"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....osmosis.ibc_rate_limit.v1beta1 import params_pb2 as osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*osmosis/ibc-rate-limit/v1beta1/query.proto\x12\x1cosmosis.ibcratelimit.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a+osmosis/ibc-rate-limit/v1beta1/params.proto"\x14\n\x12QueryParamsRequest"Q\n\x13QueryParamsResponse\x12:\n\x06params\x18\x01 \x01(\x0b2$.osmosis.ibcratelimit.v1beta1.ParamsB\x04\xc8\xde\x1f\x002\xa7\x01\n\x05Query\x12\x9d\x01\n\x06Params\x120.osmosis.ibcratelimit.v1beta1.QueryParamsRequest\x1a1.osmosis.ibcratelimit.v1beta1.QueryParamsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/ibc-rate-limit/v1beta1/paramsB<Z:github.com/osmosis-labs/osmosis/v14/x/ibc-rate-limit/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.ibc_rate_limit.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z:github.com/osmosis-labs/osmosis/v14/x/ibc-rate-limit/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/ibc-rate-limit/v1beta1/params'
    _QUERYPARAMSREQUEST._serialized_start = 217
    _QUERYPARAMSREQUEST._serialized_end = 237
    _QUERYPARAMSRESPONSE._serialized_start = 239
    _QUERYPARAMSRESPONSE._serialized_end = 320
    _QUERY._serialized_start = 323
    _QUERY._serialized_end = 490