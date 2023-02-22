"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+osmosis/ibc-rate-limit/v1beta1/params.proto\x12\x1cosmosis.ibcratelimit.v1beta1\x1a\x14gogoproto/gogo.proto"?\n\x06Params\x125\n\x10contract_address\x18\x01 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"contract_address"B<Z:github.com/osmosis-labs/osmosis/v14/x/ibc-rate-limit/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.ibc_rate_limit.v1beta1.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z:github.com/osmosis-labs/osmosis/v14/x/ibc-rate-limit/types'
    _PARAMS.fields_by_name['contract_address']._options = None
    _PARAMS.fields_by_name['contract_address']._serialized_options = b'\xf2\xde\x1f\x17yaml:"contract_address"'
    _PARAMS._serialized_start = 99
    _PARAMS._serialized_end = 162