"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.twap.v1beta1 import twap_record_pb2 as osmosis_dot_twap_dot_v1beta1_dot_twap__record__pb2
from ....osmosis.twap.v1beta1 import genesis_pb2 as osmosis_dot_twap_dot_v1beta1_dot_genesis__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/twap/v1beta1/query.proto\x12\x14osmosis.twap.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&osmosis/twap/v1beta1/twap_record.proto\x1a"osmosis/twap/v1beta1/genesis.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xeb\x01\n\x15ArithmeticTwapRequest\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x12\n\nbase_asset\x18\x02 \x01(\t\x12\x13\n\x0bquote_asset\x18\x03 \x01(\t\x12M\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1d\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time"\x12I\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1b\xc8\xde\x1f\x01\x90\xdf\x1f\x01\xf2\xde\x1f\x0fyaml:"end_time""{\n\x16ArithmeticTwapResponse\x12a\n\x0farithmetic_twap\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"arithmetic_twap"\xc8\xde\x1f\x00"\xa5\x01\n\x1aArithmeticTwapToNowRequest\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x12\n\nbase_asset\x18\x02 \x01(\t\x12\x13\n\x0bquote_asset\x18\x03 \x01(\t\x12M\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1d\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time""\x80\x01\n\x1bArithmeticTwapToNowResponse\x12a\n\x0farithmetic_twap\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"arithmetic_twap"\xc8\xde\x1f\x00"\xea\x01\n\x14GeometricTwapRequest\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x12\n\nbase_asset\x18\x02 \x01(\t\x12\x13\n\x0bquote_asset\x18\x03 \x01(\t\x12M\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1d\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time"\x12I\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1b\xc8\xde\x1f\x01\x90\xdf\x1f\x01\xf2\xde\x1f\x0fyaml:"end_time""x\n\x15GeometricTwapResponse\x12_\n\x0egeometric_twap\x18\x01 \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"geometric_twap"\xc8\xde\x1f\x00"\xa4\x01\n\x19GeometricTwapToNowRequest\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x12\n\nbase_asset\x18\x02 \x01(\t\x12\x13\n\x0bquote_asset\x18\x03 \x01(\t\x12M\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1d\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time""}\n\x1aGeometricTwapToNowResponse\x12_\n\x0egeometric_twap\x18\x01 \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"geometric_twap"\xc8\xde\x1f\x00"\x0f\n\rParamsRequest"D\n\x0eParamsResponse\x122\n\x06params\x18\x01 \x01(\x0b2\x1c.osmosis.twap.v1beta1.ParamsB\x04\xc8\xde\x1f\x002\x92\x06\n\x05Query\x12y\n\x06Params\x12#.osmosis.twap.v1beta1.ParamsRequest\x1a$.osmosis.twap.v1beta1.ParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/twap/v1beta1/Params\x12\x99\x01\n\x0eArithmeticTwap\x12+.osmosis.twap.v1beta1.ArithmeticTwapRequest\x1a,.osmosis.twap.v1beta1.ArithmeticTwapResponse",\x82\xd3\xe4\x93\x02&\x12$/osmosis/twap/v1beta1/ArithmeticTwap\x12\xad\x01\n\x13ArithmeticTwapToNow\x120.osmosis.twap.v1beta1.ArithmeticTwapToNowRequest\x1a1.osmosis.twap.v1beta1.ArithmeticTwapToNowResponse"1\x82\xd3\xe4\x93\x02+\x12)/osmosis/twap/v1beta1/ArithmeticTwapToNow\x12\x95\x01\n\rGeometricTwap\x12*.osmosis.twap.v1beta1.GeometricTwapRequest\x1a+.osmosis.twap.v1beta1.GeometricTwapResponse"+\x82\xd3\xe4\x93\x02%\x12#/osmosis/twap/v1beta1/GeometricTwap\x12\xa9\x01\n\x12GeometricTwapToNow\x12/.osmosis.twap.v1beta1.GeometricTwapToNowRequest\x1a0.osmosis.twap.v1beta1.GeometricTwapToNowResponse"0\x82\xd3\xe4\x93\x02*\x12(/osmosis/twap/v1beta1/GeometricTwapToNowB>Z<github.com/osmosis-labs/osmosis/v14/x/twap/client/queryprotob\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.twap.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/osmosis-labs/osmosis/v14/x/twap/client/queryproto'
    _ARITHMETICTWAPREQUEST.fields_by_name['start_time']._options = None
    _ARITHMETICTWAPREQUEST.fields_by_name['start_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time"'
    _ARITHMETICTWAPREQUEST.fields_by_name['end_time']._options = None
    _ARITHMETICTWAPREQUEST.fields_by_name['end_time']._serialized_options = b'\xc8\xde\x1f\x01\x90\xdf\x1f\x01\xf2\xde\x1f\x0fyaml:"end_time"'
    _ARITHMETICTWAPRESPONSE.fields_by_name['arithmetic_twap']._options = None
    _ARITHMETICTWAPRESPONSE.fields_by_name['arithmetic_twap']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"arithmetic_twap"\xc8\xde\x1f\x00'
    _ARITHMETICTWAPTONOWREQUEST.fields_by_name['start_time']._options = None
    _ARITHMETICTWAPTONOWREQUEST.fields_by_name['start_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time"'
    _ARITHMETICTWAPTONOWRESPONSE.fields_by_name['arithmetic_twap']._options = None
    _ARITHMETICTWAPTONOWRESPONSE.fields_by_name['arithmetic_twap']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"arithmetic_twap"\xc8\xde\x1f\x00'
    _GEOMETRICTWAPREQUEST.fields_by_name['start_time']._options = None
    _GEOMETRICTWAPREQUEST.fields_by_name['start_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time"'
    _GEOMETRICTWAPREQUEST.fields_by_name['end_time']._options = None
    _GEOMETRICTWAPREQUEST.fields_by_name['end_time']._serialized_options = b'\xc8\xde\x1f\x01\x90\xdf\x1f\x01\xf2\xde\x1f\x0fyaml:"end_time"'
    _GEOMETRICTWAPRESPONSE.fields_by_name['geometric_twap']._options = None
    _GEOMETRICTWAPRESPONSE.fields_by_name['geometric_twap']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"geometric_twap"\xc8\xde\x1f\x00'
    _GEOMETRICTWAPTONOWREQUEST.fields_by_name['start_time']._options = None
    _GEOMETRICTWAPTONOWREQUEST.fields_by_name['start_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x11yaml:"start_time"'
    _GEOMETRICTWAPTONOWRESPONSE.fields_by_name['geometric_twap']._options = None
    _GEOMETRICTWAPTONOWRESPONSE.fields_by_name['geometric_twap']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"geometric_twap"\xc8\xde\x1f\x00'
    _PARAMSRESPONSE.fields_by_name['params']._options = None
    _PARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/twap/v1beta1/Params'
    _QUERY.methods_by_name['ArithmeticTwap']._options = None
    _QUERY.methods_by_name['ArithmeticTwap']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/osmosis/twap/v1beta1/ArithmeticTwap'
    _QUERY.methods_by_name['ArithmeticTwapToNow']._options = None
    _QUERY.methods_by_name['ArithmeticTwapToNow']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/osmosis/twap/v1beta1/ArithmeticTwapToNow'
    _QUERY.methods_by_name['GeometricTwap']._options = None
    _QUERY.methods_by_name['GeometricTwap']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/osmosis/twap/v1beta1/GeometricTwap'
    _QUERY.methods_by_name['GeometricTwapToNow']._options = None
    _QUERY.methods_by_name['GeometricTwapToNow']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/osmosis/twap/v1beta1/GeometricTwapToNow'
    _ARITHMETICTWAPREQUEST._serialized_start = 350
    _ARITHMETICTWAPREQUEST._serialized_end = 585
    _ARITHMETICTWAPRESPONSE._serialized_start = 587
    _ARITHMETICTWAPRESPONSE._serialized_end = 710
    _ARITHMETICTWAPTONOWREQUEST._serialized_start = 713
    _ARITHMETICTWAPTONOWREQUEST._serialized_end = 878
    _ARITHMETICTWAPTONOWRESPONSE._serialized_start = 881
    _ARITHMETICTWAPTONOWRESPONSE._serialized_end = 1009
    _GEOMETRICTWAPREQUEST._serialized_start = 1012
    _GEOMETRICTWAPREQUEST._serialized_end = 1246
    _GEOMETRICTWAPRESPONSE._serialized_start = 1248
    _GEOMETRICTWAPRESPONSE._serialized_end = 1368
    _GEOMETRICTWAPTONOWREQUEST._serialized_start = 1371
    _GEOMETRICTWAPTONOWREQUEST._serialized_end = 1535
    _GEOMETRICTWAPTONOWRESPONSE._serialized_start = 1537
    _GEOMETRICTWAPTONOWRESPONSE._serialized_end = 1662
    _PARAMSREQUEST._serialized_start = 1664
    _PARAMSREQUEST._serialized_end = 1679
    _PARAMSRESPONSE._serialized_start = 1681
    _PARAMSRESPONSE._serialized_end = 1749
    _QUERY._serialized_start = 1752
    _QUERY._serialized_end = 2538