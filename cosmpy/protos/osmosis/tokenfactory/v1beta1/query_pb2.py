"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....osmosis.tokenfactory.v1beta1 import authorityMetadata_pb2 as osmosis_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from ....osmosis.tokenfactory.v1beta1 import params_pb2 as osmosis_dot_tokenfactory_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(osmosis/tokenfactory/v1beta1/query.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a4osmosis/tokenfactory/v1beta1/authorityMetadata.proto\x1a)osmosis/tokenfactory/v1beta1/params.proto"\x14\n\x12QueryParamsRequest"Q\n\x13QueryParamsResponse\x12:\n\x06params\x18\x01 \x01(\x0b2$.osmosis.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"E\n"QueryDenomAuthorityMetadataRequest\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom""\x9a\x01\n#QueryDenomAuthorityMetadataResponse\x12s\n\x12authority_metadata\x18\x01 \x01(\x0b24.osmosis.tokenfactory.v1beta1.DenomAuthorityMetadataB!\xf2\xde\x1f\x19yaml:"authority_metadata"\xc8\xde\x1f\x00"D\n\x1dQueryDenomsFromCreatorRequest\x12#\n\x07creator\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"creator""C\n\x1eQueryDenomsFromCreatorResponse\x12!\n\x06denoms\x18\x01 \x03(\tB\x11\xf2\xde\x1f\ryaml:"denoms"2\xe4\x04\n\x05Query\x12\x9b\x01\n\x06Params\x120.osmosis.tokenfactory.v1beta1.QueryParamsRequest\x1a1.osmosis.tokenfactory.v1beta1.QueryParamsResponse",\x82\xd3\xe4\x93\x02&\x12$/osmosis/tokenfactory/v1beta1/params\x12\xe6\x01\n\x16DenomAuthorityMetadata\x12@.osmosis.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest\x1aA.osmosis.tokenfactory.v1beta1.QueryDenomAuthorityMetadataResponse"G\x82\xd3\xe4\x93\x02A\x12?/osmosis/tokenfactory/v1beta1/denoms/{denom}/authority_metadata\x12\xd3\x01\n\x11DenomsFromCreator\x12;.osmosis.tokenfactory.v1beta1.QueryDenomsFromCreatorRequest\x1a<.osmosis.tokenfactory.v1beta1.QueryDenomsFromCreatorResponse"C\x82\xd3\xe4\x93\x02=\x12;/osmosis/tokenfactory/v1beta1/denoms_from_creator/{creator}B:Z8github.com/osmosis-labs/osmosis/v14/x/tokenfactory/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.tokenfactory.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/osmosis-labs/osmosis/v14/x/tokenfactory/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['denom']._options = None
    _QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _QUERYDENOMAUTHORITYMETADATARESPONSE.fields_by_name['authority_metadata']._options = None
    _QUERYDENOMAUTHORITYMETADATARESPONSE.fields_by_name['authority_metadata']._serialized_options = b'\xf2\xde\x1f\x19yaml:"authority_metadata"\xc8\xde\x1f\x00'
    _QUERYDENOMSFROMCREATORREQUEST.fields_by_name['creator']._options = None
    _QUERYDENOMSFROMCREATORREQUEST.fields_by_name['creator']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"creator"'
    _QUERYDENOMSFROMCREATORRESPONSE.fields_by_name['denoms']._options = None
    _QUERYDENOMSFROMCREATORRESPONSE.fields_by_name['denoms']._serialized_options = b'\xf2\xde\x1f\ryaml:"denoms"'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/osmosis/tokenfactory/v1beta1/params'
    _QUERY.methods_by_name['DenomAuthorityMetadata']._options = None
    _QUERY.methods_by_name['DenomAuthorityMetadata']._serialized_options = b'\x82\xd3\xe4\x93\x02A\x12?/osmosis/tokenfactory/v1beta1/denoms/{denom}/authority_metadata'
    _QUERY.methods_by_name['DenomsFromCreator']._options = None
    _QUERY.methods_by_name['DenomsFromCreator']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/osmosis/tokenfactory/v1beta1/denoms_from_creator/{creator}'
    _QUERYPARAMSREQUEST._serialized_start = 267
    _QUERYPARAMSREQUEST._serialized_end = 287
    _QUERYPARAMSRESPONSE._serialized_start = 289
    _QUERYPARAMSRESPONSE._serialized_end = 370
    _QUERYDENOMAUTHORITYMETADATAREQUEST._serialized_start = 372
    _QUERYDENOMAUTHORITYMETADATAREQUEST._serialized_end = 441
    _QUERYDENOMAUTHORITYMETADATARESPONSE._serialized_start = 444
    _QUERYDENOMAUTHORITYMETADATARESPONSE._serialized_end = 598
    _QUERYDENOMSFROMCREATORREQUEST._serialized_start = 600
    _QUERYDENOMSFROMCREATORREQUEST._serialized_end = 668
    _QUERYDENOMSFROMCREATORRESPONSE._serialized_start = 670
    _QUERYDENOMSFROMCREATORRESPONSE._serialized_end = 737
    _QUERY._serialized_start = 740
    _QUERY._serialized_end = 1352