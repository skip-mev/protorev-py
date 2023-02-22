"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+osmosis/concentrated-liquidity/params.proto\x12\x1dosmosis.concentratedliquidity\x1a\x14gogoproto/gogo.proto"M\n\x06Params\x12C\n\x17authorized_tick_spacing\x18\x01 \x03(\x04B"\xf2\xde\x1f\x1eyaml:"authorized_tick_spacing"BDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/types'
    _PARAMS.fields_by_name['authorized_tick_spacing']._options = None
    _PARAMS.fields_by_name['authorized_tick_spacing']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"authorized_tick_spacing"'
    _PARAMS._serialized_start = 100
    _PARAMS._serialized_end = 177