"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-osmosis/concentrated-liquidity/position.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto"\xb4\x01\n\x08Position\x12U\n\tliquidity\x18\x01 \x01(\tBB\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00\x12Q\n\x0cfrozen_until\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1f\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until"BDZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/modelb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentrated_liquidity.position_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v14/x/concentrated-liquidity/model'
    _POSITION.fields_by_name['liquidity']._options = None
    _POSITION.fields_by_name['liquidity']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00'
    _POSITION.fields_by_name['frozen_until']._options = None
    _POSITION.fields_by_name['frozen_until']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x13yaml:"frozen_until"'
    _POSITION._serialized_start = 171
    _POSITION._serialized_end = 351