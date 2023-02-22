"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%osmosis/txfees/v1beta1/feetoken.proto\x12\x16osmosis.txfees.v1beta1\x1a\x14gogoproto/gogo.proto"U\n\x08FeeToken\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"\x12"\n\x06poolID\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id":\x04\xe8\xa0\x1f\x01B4Z2github.com/osmosis-labs/osmosis/v14/x/txfees/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.txfees.v1beta1.feetoken_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v14/x/txfees/types'
    _FEETOKEN.fields_by_name['denom']._options = None
    _FEETOKEN.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _FEETOKEN.fields_by_name['poolID']._options = None
    _FEETOKEN.fields_by_name['poolID']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _FEETOKEN._options = None
    _FEETOKEN._serialized_options = b'\xe8\xa0\x1f\x01'
    _FEETOKEN._serialized_start = 87
    _FEETOKEN._serialized_end = 172