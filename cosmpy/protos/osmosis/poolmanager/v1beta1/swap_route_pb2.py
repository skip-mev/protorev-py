"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,osmosis/poolmanager/v1beta1/swap_route.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto"m\n\x11SwapAmountInRoute\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x123\n\x0ftoken_out_denom\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"token_out_denom""m\n\x12SwapAmountOutRoute\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x122\n\x0etoken_in_denom\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"token_out_denom"B9Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.swap_route_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/types'
    _SWAPAMOUNTINROUTE.fields_by_name['pool_id']._options = None
    _SWAPAMOUNTINROUTE.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _SWAPAMOUNTINROUTE.fields_by_name['token_out_denom']._options = None
    _SWAPAMOUNTINROUTE.fields_by_name['token_out_denom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"token_out_denom"'
    _SWAPAMOUNTOUTROUTE.fields_by_name['pool_id']._options = None
    _SWAPAMOUNTOUTROUTE.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _SWAPAMOUNTOUTROUTE.fields_by_name['token_in_denom']._options = None
    _SWAPAMOUNTOUTROUTE.fields_by_name['token_in_denom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"token_out_denom"'
    _SWAPAMOUNTINROUTE._serialized_start = 99
    _SWAPAMOUNTINROUTE._serialized_end = 208
    _SWAPAMOUNTOUTROUTE._serialized_start = 210
    _SWAPAMOUNTOUTROUTE._serialized_end = 319