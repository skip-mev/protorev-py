"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....osmosis.valset_pref.v1beta1 import state_pb2 as osmosis_dot_valset__pref_dot_v1beta1_dot_state__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'osmosis/valset-pref/v1beta1/query.proto\x12\x1aosmosis.valsetpref.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\'osmosis/valset-pref/v1beta1/state.proto"2\n\x1fUserValidatorPreferencesRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"n\n UserValidatorPreferencesResponse\x12J\n\x0bpreferences\x18\x01 \x03(\x0b2/.osmosis.valsetpref.v1beta1.ValidatorPreferenceB\x04\xc8\xde\x1f\x002\xcf\x01\n\x05Query\x12\xc5\x01\n\x18UserValidatorPreferences\x12;.osmosis.valsetpref.v1beta1.UserValidatorPreferencesRequest\x1a<.osmosis.valsetpref.v1beta1.UserValidatorPreferencesResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/valset-pref/v1beta1/{address}BIZCgithub.com/osmosis-labs/osmosis/v14/x/valset-pref/client/queryproto\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.valset_pref.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZCgithub.com/osmosis-labs/osmosis/v14/x/valset-pref/client/queryproto\xc8\xe1\x1e\x00'
    _USERVALIDATORPREFERENCESRESPONSE.fields_by_name['preferences']._options = None
    _USERVALIDATORPREFERENCESRESPONSE.fields_by_name['preferences']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['UserValidatorPreferences']._options = None
    _QUERY.methods_by_name['UserValidatorPreferences']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/valset-pref/v1beta1/{address}'
    _USERVALIDATORPREFERENCESREQUEST._serialized_start = 164
    _USERVALIDATORPREFERENCESREQUEST._serialized_end = 214
    _USERVALIDATORPREFERENCESRESPONSE._serialized_start = 216
    _USERVALIDATORPREFERENCESRESPONSE._serialized_end = 326
    _QUERY._serialized_start = 329
    _QUERY._serialized_end = 536