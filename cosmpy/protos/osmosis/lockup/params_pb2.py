"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bosmosis/lockup/params.proto\x12\x0eosmosis.lockup\x1a\x14gogoproto/gogo.proto"Y\n\x06Params\x12O\n\x1eforce_unlock_allowed_addresses\x18\x01 \x03(\tB\'\xf2\xde\x1f#yaml:"force_unlock_allowed_address"B4Z2github.com/osmosis-labs/osmosis/v14/x/lockup/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.lockup.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v14/x/lockup/types'
    _PARAMS.fields_by_name['force_unlock_allowed_addresses']._options = None
    _PARAMS.fields_by_name['force_unlock_allowed_addresses']._serialized_options = b'\xf2\xde\x1f#yaml:"force_unlock_allowed_address"'
    _PARAMS._serialized_start = 69
    _PARAMS._serialized_end = 158