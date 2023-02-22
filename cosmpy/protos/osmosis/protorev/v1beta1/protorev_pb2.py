"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'osmosis/protorev/v1beta1/protorev.proto\x12\x18osmosis.protorev.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"t\n\x12TokenPairArbRoutes\x123\n\narb_routes\x18\x01 \x03(\x0b2\x1f.osmosis.protorev.v1beta1.Route\x12\x10\n\x08token_in\x18\x02 \x01(\t\x12\x11\n\ttoken_out\x18\x03 \x01(\t:\x04\xe8\xa0\x1f\x01"\x81\x01\n\x05Route\x12/\n\x06trades\x18\x01 \x03(\x0b2\x1f.osmosis.protorev.v1beta1.Trade\x12A\n\tstep_size\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01:\x04\xe8\xa0\x1f\x01"@\n\x05Trade\x12\x0c\n\x04pool\x18\x01 \x01(\x04\x12\x10\n\x08token_in\x18\x02 \x01(\t\x12\x11\n\ttoken_out\x18\x03 \x01(\t:\x04\xe8\xa0\x1f\x01"\x96\x01\n\x0fRouteStatistics\x12*\n\x07profits\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.Coin\x12H\n\x10number_of_trades\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\r\n\x05route\x18\x03 \x03(\x04"Z\n\x0bPoolWeights\x12\x15\n\rstable_weight\x18\x01 \x01(\x04\x12\x17\n\x0fbalancer_weight\x18\x02 \x01(\x04\x12\x1b\n\x13concentrated_weight\x18\x03 \x01(\x04"]\n\tBaseDenom\x12\r\n\x05denom\x18\x01 \x01(\t\x12A\n\tstep_size\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00B6Z4github.com/osmosis-labs/osmosis/v14/x/protorev/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.protorev.v1beta1.protorev_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/osmosis-labs/osmosis/v14/x/protorev/types'
    _TOKENPAIRARBROUTES._options = None
    _TOKENPAIRARBROUTES._serialized_options = b'\xe8\xa0\x1f\x01'
    _ROUTE.fields_by_name['step_size']._options = None
    _ROUTE.fields_by_name['step_size']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01'
    _ROUTE._options = None
    _ROUTE._serialized_options = b'\xe8\xa0\x1f\x01'
    _TRADE._options = None
    _TRADE._serialized_options = b'\xe8\xa0\x1f\x01'
    _ROUTESTATISTICS.fields_by_name['number_of_trades']._options = None
    _ROUTESTATISTICS.fields_by_name['number_of_trades']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _BASEDENOM.fields_by_name['step_size']._options = None
    _BASEDENOM.fields_by_name['step_size']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _TOKENPAIRARBROUTES._serialized_start = 150
    _TOKENPAIRARBROUTES._serialized_end = 266
    _ROUTE._serialized_start = 269
    _ROUTE._serialized_end = 398
    _TRADE._serialized_start = 400
    _TRADE._serialized_end = 464
    _ROUTESTATISTICS._serialized_start = 467
    _ROUTESTATISTICS._serialized_end = 617
    _POOLWEIGHTS._serialized_start = 619
    _POOLWEIGHTS._serialized_end = 709
    _BASEDENOM._serialized_start = 711
    _BASEDENOM._serialized_end = 804