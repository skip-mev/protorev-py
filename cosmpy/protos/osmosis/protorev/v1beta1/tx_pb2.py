"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....osmosis.protorev.v1beta1 import protorev_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_protorev__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!osmosis/protorev/v1beta1/tx.proto\x12\x18osmosis.protorev.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\'osmosis/protorev/v1beta1/protorev.proto"b\n\x0fMsgSetHotRoutes\x12\r\n\x05admin\x18\x01 \x01(\t\x12@\n\nhot_routes\x18\x02 \x03(\x0b2,.osmosis.protorev.v1beta1.TokenPairArbRoutes"\x19\n\x17MsgSetHotRoutesResponse"B\n\x16MsgSetDeveloperAccount\x12\r\n\x05admin\x18\x01 \x01(\t\x12\x19\n\x11developer_account\x18\x02 \x01(\t" \n\x1eMsgSetDeveloperAccountResponse"_\n\x11MsgSetPoolWeights\x12\r\n\x05admin\x18\x01 \x01(\t\x12;\n\x0cpool_weights\x18\x02 \x01(\x0b2%.osmosis.protorev.v1beta1.PoolWeights"\x1b\n\x19MsgSetPoolWeightsResponse"I\n\x18MsgSetMaxPoolPointsPerTx\x12\r\n\x05admin\x18\x01 \x01(\t\x12\x1e\n\x16max_pool_points_per_tx\x18\x02 \x01(\x04""\n MsgSetMaxPoolPointsPerTxResponse"O\n\x1bMsgSetMaxPoolPointsPerBlock\x12\r\n\x05admin\x18\x01 \x01(\t\x12!\n\x19max_pool_points_per_block\x18\x02 \x01(\x04"%\n#MsgSetMaxPoolPointsPerBlockResponse"[\n\x10MsgSetBaseDenoms\x12\r\n\x05admin\x18\x01 \x01(\t\x128\n\x0bbase_denoms\x18\x02 \x03(\x0b2#.osmosis.protorev.v1beta1.BaseDenom"\x1a\n\x18MsgSetBaseDenomsResponse2\xb5\x08\n\x03Msg\x12\x9a\x01\n\x0cSetHotRoutes\x12).osmosis.protorev.v1beta1.MsgSetHotRoutes\x1a1.osmosis.protorev.v1beta1.MsgSetHotRoutesResponse",\x82\xd3\xe4\x93\x02&"$/osmosis/v14/protorev/set_hot_routes\x12\xb6\x01\n\x13SetDeveloperAccount\x120.osmosis.protorev.v1beta1.MsgSetDeveloperAccount\x1a8.osmosis.protorev.v1beta1.MsgSetDeveloperAccountResponse"3\x82\xd3\xe4\x93\x02-"+/osmosis/v14/protorev/set_developer_account\x12\xc1\x01\n\x15SetMaxPoolPointsPerTx\x122.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerTx\x1a:.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerTxResponse"8\x82\xd3\xe4\x93\x022"0/osmosis/v14/protorev/set_max_pool_points_per_tx\x12\xcd\x01\n\x18SetMaxPoolPointsPerBlock\x125.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerBlock\x1a=.osmosis.protorev.v1beta1.MsgSetMaxPoolPointsPerBlockResponse";\x82\xd3\xe4\x93\x025"3/osmosis/v14/protorev/set_max_pool_points_per_block\x12\xa2\x01\n\x0eSetPoolWeights\x12+.osmosis.protorev.v1beta1.MsgSetPoolWeights\x1a3.osmosis.protorev.v1beta1.MsgSetPoolWeightsResponse".\x82\xd3\xe4\x93\x02("&/osmosis/v14/protorev/set_pool_weights\x12\x9e\x01\n\rSetBaseDenoms\x12*.osmosis.protorev.v1beta1.MsgSetBaseDenoms\x1a2.osmosis.protorev.v1beta1.MsgSetBaseDenomsResponse"-\x82\xd3\xe4\x93\x02\'"%/osmosis/v14/protorev/set_base_denomsB6Z4github.com/osmosis-labs/osmosis/v14/x/protorev/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.protorev.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/osmosis-labs/osmosis/v14/x/protorev/types'
    _MSG.methods_by_name['SetHotRoutes']._options = None
    _MSG.methods_by_name['SetHotRoutes']._serialized_options = b'\x82\xd3\xe4\x93\x02&"$/osmosis/v14/protorev/set_hot_routes'
    _MSG.methods_by_name['SetDeveloperAccount']._options = None
    _MSG.methods_by_name['SetDeveloperAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/osmosis/v14/protorev/set_developer_account'
    _MSG.methods_by_name['SetMaxPoolPointsPerTx']._options = None
    _MSG.methods_by_name['SetMaxPoolPointsPerTx']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/osmosis/v14/protorev/set_max_pool_points_per_tx'
    _MSG.methods_by_name['SetMaxPoolPointsPerBlock']._options = None
    _MSG.methods_by_name['SetMaxPoolPointsPerBlock']._serialized_options = b'\x82\xd3\xe4\x93\x025"3/osmosis/v14/protorev/set_max_pool_points_per_block'
    _MSG.methods_by_name['SetPoolWeights']._options = None
    _MSG.methods_by_name['SetPoolWeights']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/osmosis/v14/protorev/set_pool_weights'
    _MSG.methods_by_name['SetBaseDenoms']._options = None
    _MSG.methods_by_name['SetBaseDenoms']._serialized_options = b'\x82\xd3\xe4\x93\x02\'"%/osmosis/v14/protorev/set_base_denoms'
    _MSGSETHOTROUTES._serialized_start = 156
    _MSGSETHOTROUTES._serialized_end = 254
    _MSGSETHOTROUTESRESPONSE._serialized_start = 256
    _MSGSETHOTROUTESRESPONSE._serialized_end = 281
    _MSGSETDEVELOPERACCOUNT._serialized_start = 283
    _MSGSETDEVELOPERACCOUNT._serialized_end = 349
    _MSGSETDEVELOPERACCOUNTRESPONSE._serialized_start = 351
    _MSGSETDEVELOPERACCOUNTRESPONSE._serialized_end = 383
    _MSGSETPOOLWEIGHTS._serialized_start = 385
    _MSGSETPOOLWEIGHTS._serialized_end = 480
    _MSGSETPOOLWEIGHTSRESPONSE._serialized_start = 482
    _MSGSETPOOLWEIGHTSRESPONSE._serialized_end = 509
    _MSGSETMAXPOOLPOINTSPERTX._serialized_start = 511
    _MSGSETMAXPOOLPOINTSPERTX._serialized_end = 584
    _MSGSETMAXPOOLPOINTSPERTXRESPONSE._serialized_start = 586
    _MSGSETMAXPOOLPOINTSPERTXRESPONSE._serialized_end = 620
    _MSGSETMAXPOOLPOINTSPERBLOCK._serialized_start = 622
    _MSGSETMAXPOOLPOINTSPERBLOCK._serialized_end = 701
    _MSGSETMAXPOOLPOINTSPERBLOCKRESPONSE._serialized_start = 703
    _MSGSETMAXPOOLPOINTSPERBLOCKRESPONSE._serialized_end = 740
    _MSGSETBASEDENOMS._serialized_start = 742
    _MSGSETBASEDENOMS._serialized_end = 833
    _MSGSETBASEDENOMSRESPONSE._serialized_start = 835
    _MSGSETBASEDENOMSRESPONSE._serialized_end = 861
    _MSG._serialized_start = 864
    _MSG._serialized_end = 1941