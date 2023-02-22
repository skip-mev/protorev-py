"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.osmosis/poolmanager/v1beta1/module_route.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto"G\n\x0bModuleRoute\x128\n\tpool_type\x18\x01 \x01(\x0e2%.osmosis.poolmanager.v1beta1.PoolType*@\n\x08PoolType\x12\x0c\n\x08Balancer\x10\x00\x12\x0e\n\nStableswap\x10\x01\x12\x10\n\x0cConcentrated\x10\x02\x1a\x04\x88\xa3\x1e\x00B9Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.module_route_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v14/x/poolmanager/types'
    _POOLTYPE._options = None
    _POOLTYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _POOLTYPE._serialized_start = 174
    _POOLTYPE._serialized_end = 238
    _MODULEROUTE._serialized_start = 101
    _MODULEROUTE._serialized_end = 172