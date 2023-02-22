"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.protorev.v1beta1 import protorev_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_protorev__pb2
from ....osmosis.protorev.v1beta1 import params_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&osmosis/protorev/v1beta1/genesis.proto\x12\x18osmosis.protorev.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\'osmosis/protorev/v1beta1/protorev.proto\x1a%osmosis/protorev/v1beta1/params.proto"F\n\x0cGenesisState\x126\n\x06params\x18\x01 \x01(\x0b2 .osmosis.protorev.v1beta1.ParamsB\x04\xc8\xde\x1f\x00B6Z4github.com/osmosis-labs/osmosis/v14/x/protorev/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.protorev.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/osmosis-labs/osmosis/v14/x/protorev/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 170
    _GENESISSTATE._serialized_end = 240