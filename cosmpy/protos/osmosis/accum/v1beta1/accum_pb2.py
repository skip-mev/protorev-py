"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!osmosis/accum/v1beta1/accum.proto\x12\x15osmosis.accum.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xc2\x01\n\x12AccumulatorContent\x12f\n\x0baccum_value\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12D\n\x0ctotal_shares\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\t\n\x07Options"\xd8\x02\n\x06Record\x12B\n\nnum_shares\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12k\n\x10init_accum_value\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12l\n\x11unclaimed_rewards\x18\x03 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12/\n\x07options\x18\x04 \x01(\x0b2\x1e.osmosis.accum.v1beta1.OptionsB1Z/github.com/osmosis-labs/osmosis/osmoutils/accumb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.accum.v1beta1.accum_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/osmoutils/accum'
    _ACCUMULATORCONTENT.fields_by_name['accum_value']._options = None
    _ACCUMULATORCONTENT.fields_by_name['accum_value']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _ACCUMULATORCONTENT.fields_by_name['total_shares']._options = None
    _ACCUMULATORCONTENT.fields_by_name['total_shares']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _RECORD.fields_by_name['num_shares']._options = None
    _RECORD.fields_by_name['num_shares']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _RECORD.fields_by_name['init_accum_value']._options = None
    _RECORD.fields_by_name['init_accum_value']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _RECORD.fields_by_name['unclaimed_rewards']._options = None
    _RECORD.fields_by_name['unclaimed_rewards']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _ACCUMULATORCONTENT._serialized_start = 115
    _ACCUMULATORCONTENT._serialized_end = 309
    _OPTIONS._serialized_start = 311
    _OPTIONS._serialized_end = 320
    _RECORD._serialized_start = 323
    _RECORD._serialized_end = 667