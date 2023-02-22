"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.gamm.v1beta1 import genesis_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_genesis__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/gamm/v1beta1/gov.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a"osmosis/gamm/v1beta1/genesis.proto"\xa0\x01\n\x1fReplaceMigrationRecordsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12K\n\x07records\x18\x03 \x03(\x0b24.osmosis.gamm.v1beta1.BalancerToConcentratedPoolLinkB\x04\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\x9f\x01\n\x1eUpdateMigrationRecordsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12K\n\x07records\x18\x03 \x03(\x0b24.osmosis.gamm.v1beta1.BalancerToConcentratedPoolLinkB\x04\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00B2Z0github.com/osmosis-labs/osmosis/v14/x/gamm/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.v1beta1.gov_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/osmosis-labs/osmosis/v14/x/gamm/types'
    _REPLACEMIGRATIONRECORDSPROPOSAL.fields_by_name['records']._options = None
    _REPLACEMIGRATIONRECORDSPROPOSAL.fields_by_name['records']._serialized_options = b'\xc8\xde\x1f\x00'
    _REPLACEMIGRATIONRECORDSPROPOSAL._options = None
    _REPLACEMIGRATIONRECORDSPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _UPDATEMIGRATIONRECORDSPROPOSAL.fields_by_name['records']._options = None
    _UPDATEMIGRATIONRECORDSPROPOSAL.fields_by_name['records']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPDATEMIGRATIONRECORDSPROPOSAL._options = None
    _UPDATEMIGRATIONRECORDSPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _REPLACEMIGRATIONRECORDSPROPOSAL._serialized_start = 115
    _REPLACEMIGRATIONRECORDSPROPOSAL._serialized_end = 275
    _UPDATEMIGRATIONRECORDSPROPOSAL._serialized_start = 278
    _UPDATEMIGRATIONRECORDSPROPOSAL._serialized_end = 437