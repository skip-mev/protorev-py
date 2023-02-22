"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#osmosis/superfluid/superfluid.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"g\n\x0fSuperfluidAsset\x12\r\n\x05denom\x18\x01 \x01(\t\x12;\n\nasset_type\x18\x02 \x01(\x0e2\'.osmosis.superfluid.SuperfluidAssetType:\x08\xe8\xa0\x1f\x01\x88\xa0\x1f\x00"R\n\x1dSuperfluidIntermediaryAccount\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x10\n\x08val_addr\x18\x02 \x01(\t\x12\x10\n\x08gauge_id\x18\x03 \x01(\x04"\x9e\x01\n\x1eOsmoEquivalentMultiplierRecord\x12\x14\n\x0cepoch_number\x18\x01 \x01(\x03\x12\r\n\x05denom\x18\x02 \x01(\t\x12W\n\nmultiplier\x18\x03 \x01(\tBC\xf2\xde\x1f\x11yaml:"multiplier"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\xa3\x02\n\x1aSuperfluidDelegationRecord\x12\x19\n\x11delegator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12e\n\x11delegation_amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12h\n\x18equivalent_staked_amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB+\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin"T\n#LockIdIntermediaryAccountConnection\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04\x12\x1c\n\x14intermediary_account\x18\x02 \x01(\t"%\n\x16UnpoolWhitelistedPools\x12\x0b\n\x03ids\x18\x01 \x03(\x04*Z\n\x13SuperfluidAssetType\x12\x1d\n\x19SuperfluidAssetTypeNative\x10\x00\x12\x1e\n\x1aSuperfluidAssetTypeLPShare\x10\x01\x1a\x04\x88\xa3\x1e\x00B8Z6github.com/osmosis-labs/osmosis/v14/x/superfluid/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.superfluid.superfluid_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v14/x/superfluid/types'
    _SUPERFLUIDASSETTYPE._options = None
    _SUPERFLUIDASSETTYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _SUPERFLUIDASSET._options = None
    _SUPERFLUIDASSET._serialized_options = b'\xe8\xa0\x1f\x01\x88\xa0\x1f\x00'
    _OSMOEQUIVALENTMULTIPLIERRECORD.fields_by_name['multiplier']._options = None
    _OSMOEQUIVALENTMULTIPLIERRECORD.fields_by_name['multiplier']._serialized_options = b'\xf2\xde\x1f\x11yaml:"multiplier"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONRECORD.fields_by_name['delegation_amount']._options = None
    _SUPERFLUIDDELEGATIONRECORD.fields_by_name['delegation_amount']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _SUPERFLUIDDELEGATIONRECORD.fields_by_name['equivalent_staked_amount']._options = None
    _SUPERFLUIDDELEGATIONRECORD.fields_by_name['equivalent_staked_amount']._serialized_options = b"\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _SUPERFLUIDASSETTYPE._serialized_start = 947
    _SUPERFLUIDASSETTYPE._serialized_end = 1037
    _SUPERFLUIDASSET._serialized_start = 178
    _SUPERFLUIDASSET._serialized_end = 281
    _SUPERFLUIDINTERMEDIARYACCOUNT._serialized_start = 283
    _SUPERFLUIDINTERMEDIARYACCOUNT._serialized_end = 365
    _OSMOEQUIVALENTMULTIPLIERRECORD._serialized_start = 368
    _OSMOEQUIVALENTMULTIPLIERRECORD._serialized_end = 526
    _SUPERFLUIDDELEGATIONRECORD._serialized_start = 529
    _SUPERFLUIDDELEGATIONRECORD._serialized_end = 820
    _LOCKIDINTERMEDIARYACCOUNTCONNECTION._serialized_start = 822
    _LOCKIDINTERMEDIARYACCOUNTCONNECTION._serialized_end = 906
    _UNPOOLWHITELISTEDPOOLS._serialized_start = 908
    _UNPOOLWHITELISTEDPOOLS._serialized_end = 945