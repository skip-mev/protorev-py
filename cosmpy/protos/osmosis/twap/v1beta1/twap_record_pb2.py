"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&osmosis/twap/v1beta1/twap_record.proto\x12\x14osmosis.twap.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc3\x05\n\nTwapRecord\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x14\n\x0casset0_denom\x18\x02 \x01(\t\x12\x14\n\x0casset1_denom\x18\x03 \x01(\t\x129\n\x06height\x18\x04 \x01(\x03B)\xf2\xde\x1f\x14yaml:"record_height"\xea\xde\x1f\rrecord_height\x12H\n\x04time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1e\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x12yaml:"record_time"\x12J\n\x12p0_last_spot_price\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12J\n\x12p1_last_spot_price\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12V\n\x1ep0_arithmetic_twap_accumulator\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12V\n\x1ep1_arithmetic_twap_accumulator\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12R\n\x1ageometric_twap_accumulator\x18\n \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12W\n\x0flast_error_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB"\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x16yaml:"last_error_time"B2Z0github.com/osmosis-labs/osmosis/v14/x/twap/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.twap.v1beta1.twap_record_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/osmosis-labs/osmosis/v14/x/twap/types'
    _TWAPRECORD.fields_by_name['height']._options = None
    _TWAPRECORD.fields_by_name['height']._serialized_options = b'\xf2\xde\x1f\x14yaml:"record_height"\xea\xde\x1f\rrecord_height'
    _TWAPRECORD.fields_by_name['time']._options = None
    _TWAPRECORD.fields_by_name['time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x12yaml:"record_time"'
    _TWAPRECORD.fields_by_name['p0_last_spot_price']._options = None
    _TWAPRECORD.fields_by_name['p0_last_spot_price']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _TWAPRECORD.fields_by_name['p1_last_spot_price']._options = None
    _TWAPRECORD.fields_by_name['p1_last_spot_price']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _TWAPRECORD.fields_by_name['p0_arithmetic_twap_accumulator']._options = None
    _TWAPRECORD.fields_by_name['p0_arithmetic_twap_accumulator']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _TWAPRECORD.fields_by_name['p1_arithmetic_twap_accumulator']._options = None
    _TWAPRECORD.fields_by_name['p1_arithmetic_twap_accumulator']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _TWAPRECORD.fields_by_name['geometric_twap_accumulator']._options = None
    _TWAPRECORD.fields_by_name['geometric_twap_accumulator']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _TWAPRECORD.fields_by_name['last_error_time']._options = None
    _TWAPRECORD.fields_by_name['last_error_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x16yaml:"last_error_time"'
    _TWAPRECORD._serialized_start = 206
    _TWAPRECORD._serialized_end = 913