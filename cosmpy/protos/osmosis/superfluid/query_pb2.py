"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2
from ...osmosis.superfluid import params_pb2 as osmosis_dot_superfluid_dot_params__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ...cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/superfluid/query.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a#osmosis/superfluid/superfluid.proto\x1a\x1fosmosis/superfluid/params.proto\x1a\x19osmosis/lockup/lock.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a$cosmos/staking/v1beta1/staking.proto"\x14\n\x12QueryParamsRequest"G\n\x13QueryParamsResponse\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.osmosis.superfluid.ParamsB\x04\xc8\xde\x1f\x00"!\n\x10AssetTypeRequest\x12\r\n\x05denom\x18\x01 \x01(\t"P\n\x11AssetTypeResponse\x12;\n\nasset_type\x18\x01 \x01(\x0e2\'.osmosis.superfluid.SuperfluidAssetType"\x12\n\x10AllAssetsRequest"N\n\x11AllAssetsResponse\x129\n\x06assets\x18\x01 \x03(\x0b2#.osmosis.superfluid.SuperfluidAssetB\x04\xc8\xde\x1f\x00"\'\n\x16AssetMultiplierRequest\x12\r\n\x05denom\x18\x01 \x01(\t"q\n\x17AssetMultiplierResponse\x12V\n\x1aosmo_equivalent_multiplier\x18\x01 \x01(\x0b22.osmosis.superfluid.OsmoEquivalentMultiplierRecord"g\n!SuperfluidIntermediaryAccountInfo\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x10\n\x08val_addr\x18\x02 \x01(\t\x12\x10\n\x08gauge_id\x18\x03 \x01(\x04\x12\x0f\n\x07address\x18\x04 \x01(\t"\\\n\x1eAllIntermediaryAccountsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xad\x01\n\x1fAllIntermediaryAccountsResponse\x12M\n\x08accounts\x18\x01 \x03(\x0b25.osmosis.superfluid.SuperfluidIntermediaryAccountInfoB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"6\n#ConnectedIntermediaryAccountRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04"n\n$ConnectedIntermediaryAccountResponse\x12F\n\x07account\x18\x01 \x01(\x0b25.osmosis.superfluid.SuperfluidIntermediaryAccountInfo"?\n.QueryTotalDelegationByValidatorForDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t"h\n/QueryTotalDelegationByValidatorForDenomResponse\x125\n\x06assets\x18\x01 \x03(\x0b2\x1f.osmosis.superfluid.DelegationsB\x04\xc8\xde\x1f\x00"\xdd\x01\n\x0bDelegations\x12\x10\n\x08val_addr\x18\x01 \x01(\t\x12Y\n\x0bamount_sfsd\x18\x02 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x12yaml:"amount_sfsd"\xc8\xde\x1f\x00\x12a\n\x0fosmo_equivalent\x18\x03 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"osmo_equivalent"\xc8\xde\x1f\x00"#\n!TotalSuperfluidDelegationsRequest"\x96\x01\n"TotalSuperfluidDelegationsResponse\x12p\n\x11total_delegations\x18\x01 \x01(\tBU\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f#yaml:"total_superfluid_delegations"\xc8\xde\x1f\x00"h\n!SuperfluidDelegationAmountRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\r\n\x05denom\x18\x03 \x01(\t"\x81\x01\n"SuperfluidDelegationAmountResponse\x12[\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"D\n\'SuperfluidDelegationsByDelegatorRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t"\xe7\x02\n(SuperfluidDelegationsByDelegatorResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00\x12j\n\x15total_delegated_coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12r\n\x1etotal_equivalent_staked_amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin"U\n)SuperfluidUndelegationsByDelegatorRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"\xb5\x02\n*SuperfluidUndelegationsByDelegatorResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00\x12l\n\x17total_undelegated_coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12<\n\x0fsynthetic_locks\x18\x03 \x03(\x0b2\x1d.osmosis.lockup.SyntheticLockB\x04\xc8\xde\x1f\x00"X\n,SuperfluidDelegationsByValidatorDenomRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"\x8c\x01\n-SuperfluidDelegationsByValidatorDenomResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00"d\n8EstimateSuperfluidDelegatedAmountByValidatorDenomRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"\xa7\x01\n9EstimateSuperfluidDelegatedAmountByValidatorDenomResponse\x12j\n\x15total_delegated_coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"C\n&QueryTotalDelegationByDelegatorRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t"\xb5\x03\n\'QueryTotalDelegationByDelegatorResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00\x12M\n\x13delegation_response\x18\x02 \x03(\x0b2*.cosmos.staking.v1beta1.DelegationResponseB\x04\xc8\xde\x1f\x00\x12j\n\x15total_delegated_coins\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12r\n\x1etotal_equivalent_staked_amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin"\x1d\n\x1bQueryUnpoolWhitelistRequest"0\n\x1cQueryUnpoolWhitelistResponse\x12\x10\n\x08pool_ids\x18\x01 \x03(\x042\xfe\x17\n\x05Query\x12\x85\x01\n\x06Params\x12&.osmosis.superfluid.QueryParamsRequest\x1a\'.osmosis.superfluid.QueryParamsResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/superfluid/v1beta1/params\x12\x88\x01\n\tAssetType\x12$.osmosis.superfluid.AssetTypeRequest\x1a%.osmosis.superfluid.AssetTypeResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/asset_type\x12\x88\x01\n\tAllAssets\x12$.osmosis.superfluid.AllAssetsRequest\x1a%.osmosis.superfluid.AllAssetsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/all_assets\x12\xa0\x01\n\x0fAssetMultiplier\x12*.osmosis.superfluid.AssetMultiplierRequest\x1a+.osmosis.superfluid.AssetMultiplierResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/superfluid/v1beta1/asset_multiplier\x12\xc1\x01\n\x17AllIntermediaryAccounts\x122.osmosis.superfluid.AllIntermediaryAccountsRequest\x1a3.osmosis.superfluid.AllIntermediaryAccountsResponse"=\x82\xd3\xe4\x93\x027\x125/osmosis/superfluid/v1beta1/all_intermediary_accounts\x12\xdf\x01\n\x1cConnectedIntermediaryAccount\x127.osmosis.superfluid.ConnectedIntermediaryAccountRequest\x1a8.osmosis.superfluid.ConnectedIntermediaryAccountResponse"L\x82\xd3\xe4\x93\x02F\x12D/osmosis/superfluid/v1beta1/connected_intermediary_account/{lock_id}\x12\xaf\x01\n"TotalDelegationByValidatorForDenom\x12B.osmosis.superfluid.QueryTotalDelegationByValidatorForDenomRequest\x1aC.osmosis.superfluid.QueryTotalDelegationByValidatorForDenomResponse"\x00\x12\xcb\x01\n\x1aTotalSuperfluidDelegations\x125.osmosis.superfluid.TotalSuperfluidDelegationsRequest\x1a6.osmosis.superfluid.TotalSuperfluidDelegationsResponse">\x82\xd3\xe4\x93\x028\x126/osmosis/superfluid/v1beta1/all_superfluid_delegations\x12\xcd\x01\n\x1aSuperfluidDelegationAmount\x125.osmosis.superfluid.SuperfluidDelegationAmountRequest\x1a6.osmosis.superfluid.SuperfluidDelegationAmountResponse"@\x82\xd3\xe4\x93\x02:\x128/osmosis/superfluid/v1beta1/superfluid_delegation_amount\x12\xed\x01\n SuperfluidDelegationsByDelegator\x12;.osmosis.superfluid.SuperfluidDelegationsByDelegatorRequest\x1a<.osmosis.superfluid.SuperfluidDelegationsByDelegatorResponse"N\x82\xd3\xe4\x93\x02H\x12F/osmosis/superfluid/v1beta1/superfluid_delegations/{delegator_address}\x12\x82\x02\n"SuperfluidUndelegationsByDelegator\x12=.osmosis.superfluid.SuperfluidUndelegationsByDelegatorRequest\x1a>.osmosis.superfluid.SuperfluidUndelegationsByDelegatorResponse"]\x82\xd3\xe4\x93\x02W\x12U/osmosis/superfluid/v1beta1/superfluid_undelegations_by_delegator/{delegator_address}\x12\xfb\x01\n%SuperfluidDelegationsByValidatorDenom\x12@.osmosis.superfluid.SuperfluidDelegationsByValidatorDenomRequest\x1aA.osmosis.superfluid.SuperfluidDelegationsByValidatorDenomResponse"M\x82\xd3\xe4\x93\x02G\x12E/osmosis/superfluid/v1beta1/superfluid_delegations_by_validator_denom\x12\xae\x02\n1EstimateSuperfluidDelegatedAmountByValidatorDenom\x12L.osmosis.superfluid.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest\x1aM.osmosis.superfluid.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse"\\\x82\xd3\xe4\x93\x02V\x12T/osmosis/superfluid/v1beta1/estimate_superfluid_delegation_amount_by_validator_denom\x12\xec\x01\n\x1aTotalDelegationByDelegator\x12:.osmosis.superfluid.QueryTotalDelegationByDelegatorRequest\x1a;.osmosis.superfluid.QueryTotalDelegationByDelegatorResponse"U\x82\xd3\xe4\x93\x02O\x12M/osmosis/superfluid/v1beta1/total_delegation_by_delegator/{delegator_address}\x12\xaa\x01\n\x0fUnpoolWhitelist\x12/.osmosis.superfluid.QueryUnpoolWhitelistRequest\x1a0.osmosis.superfluid.QueryUnpoolWhitelistResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/superfluid/v1beta1/unpool_whitelistB8Z6github.com/osmosis-labs/osmosis/v14/x/superfluid/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.superfluid.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v14/x/superfluid/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _ALLASSETSRESPONSE.fields_by_name['assets']._options = None
    _ALLASSETSRESPONSE.fields_by_name['assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _ALLINTERMEDIARYACCOUNTSRESPONSE.fields_by_name['accounts']._options = None
    _ALLINTERMEDIARYACCOUNTSRESPONSE.fields_by_name['accounts']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALDELEGATIONBYVALIDATORFORDENOMRESPONSE.fields_by_name['assets']._options = None
    _QUERYTOTALDELEGATIONBYVALIDATORFORDENOMRESPONSE.fields_by_name['assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _DELEGATIONS.fields_by_name['amount_sfsd']._options = None
    _DELEGATIONS.fields_by_name['amount_sfsd']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x12yaml:"amount_sfsd"\xc8\xde\x1f\x00'
    _DELEGATIONS.fields_by_name['osmo_equivalent']._options = None
    _DELEGATIONS.fields_by_name['osmo_equivalent']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"osmo_equivalent"\xc8\xde\x1f\x00'
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE.fields_by_name['total_delegations']._options = None
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE.fields_by_name['total_delegations']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f#yaml:"total_superfluid_delegations"\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE.fields_by_name['amount']._options = None
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_delegated_coins']._options = None
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_delegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_equivalent_staked_amount']._options = None
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_equivalent_staked_amount']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_undelegated_coins']._options = None
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_undelegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['synthetic_locks']._options = None
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['synthetic_locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE.fields_by_name['total_delegated_coins']._options = None
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE.fields_by_name['total_delegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['delegation_response']._options = None
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['delegation_response']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['total_delegated_coins']._options = None
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['total_delegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['total_equivalent_staked_amount']._options = None
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE.fields_by_name['total_equivalent_staked_amount']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/superfluid/v1beta1/params'
    _QUERY.methods_by_name['AssetType']._options = None
    _QUERY.methods_by_name['AssetType']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/asset_type'
    _QUERY.methods_by_name['AllAssets']._options = None
    _QUERY.methods_by_name['AllAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/all_assets'
    _QUERY.methods_by_name['AssetMultiplier']._options = None
    _QUERY.methods_by_name['AssetMultiplier']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/superfluid/v1beta1/asset_multiplier'
    _QUERY.methods_by_name['AllIntermediaryAccounts']._options = None
    _QUERY.methods_by_name['AllIntermediaryAccounts']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/osmosis/superfluid/v1beta1/all_intermediary_accounts'
    _QUERY.methods_by_name['ConnectedIntermediaryAccount']._options = None
    _QUERY.methods_by_name['ConnectedIntermediaryAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/osmosis/superfluid/v1beta1/connected_intermediary_account/{lock_id}'
    _QUERY.methods_by_name['TotalSuperfluidDelegations']._options = None
    _QUERY.methods_by_name['TotalSuperfluidDelegations']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/osmosis/superfluid/v1beta1/all_superfluid_delegations'
    _QUERY.methods_by_name['SuperfluidDelegationAmount']._options = None
    _QUERY.methods_by_name['SuperfluidDelegationAmount']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/osmosis/superfluid/v1beta1/superfluid_delegation_amount'
    _QUERY.methods_by_name['SuperfluidDelegationsByDelegator']._options = None
    _QUERY.methods_by_name['SuperfluidDelegationsByDelegator']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/osmosis/superfluid/v1beta1/superfluid_delegations/{delegator_address}'
    _QUERY.methods_by_name['SuperfluidUndelegationsByDelegator']._options = None
    _QUERY.methods_by_name['SuperfluidUndelegationsByDelegator']._serialized_options = b'\x82\xd3\xe4\x93\x02W\x12U/osmosis/superfluid/v1beta1/superfluid_undelegations_by_delegator/{delegator_address}'
    _QUERY.methods_by_name['SuperfluidDelegationsByValidatorDenom']._options = None
    _QUERY.methods_by_name['SuperfluidDelegationsByValidatorDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02G\x12E/osmosis/superfluid/v1beta1/superfluid_delegations_by_validator_denom'
    _QUERY.methods_by_name['EstimateSuperfluidDelegatedAmountByValidatorDenom']._options = None
    _QUERY.methods_by_name['EstimateSuperfluidDelegatedAmountByValidatorDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02V\x12T/osmosis/superfluid/v1beta1/estimate_superfluid_delegation_amount_by_validator_denom'
    _QUERY.methods_by_name['TotalDelegationByDelegator']._options = None
    _QUERY.methods_by_name['TotalDelegationByDelegator']._serialized_options = b'\x82\xd3\xe4\x93\x02O\x12M/osmosis/superfluid/v1beta1/total_delegation_by_delegator/{delegator_address}'
    _QUERY.methods_by_name['UnpoolWhitelist']._options = None
    _QUERY.methods_by_name['UnpoolWhitelist']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/superfluid/v1beta1/unpool_whitelist'
    _QUERYPARAMSREQUEST._serialized_start = 382
    _QUERYPARAMSREQUEST._serialized_end = 402
    _QUERYPARAMSRESPONSE._serialized_start = 404
    _QUERYPARAMSRESPONSE._serialized_end = 475
    _ASSETTYPEREQUEST._serialized_start = 477
    _ASSETTYPEREQUEST._serialized_end = 510
    _ASSETTYPERESPONSE._serialized_start = 512
    _ASSETTYPERESPONSE._serialized_end = 592
    _ALLASSETSREQUEST._serialized_start = 594
    _ALLASSETSREQUEST._serialized_end = 612
    _ALLASSETSRESPONSE._serialized_start = 614
    _ALLASSETSRESPONSE._serialized_end = 692
    _ASSETMULTIPLIERREQUEST._serialized_start = 694
    _ASSETMULTIPLIERREQUEST._serialized_end = 733
    _ASSETMULTIPLIERRESPONSE._serialized_start = 735
    _ASSETMULTIPLIERRESPONSE._serialized_end = 848
    _SUPERFLUIDINTERMEDIARYACCOUNTINFO._serialized_start = 850
    _SUPERFLUIDINTERMEDIARYACCOUNTINFO._serialized_end = 953
    _ALLINTERMEDIARYACCOUNTSREQUEST._serialized_start = 955
    _ALLINTERMEDIARYACCOUNTSREQUEST._serialized_end = 1047
    _ALLINTERMEDIARYACCOUNTSRESPONSE._serialized_start = 1050
    _ALLINTERMEDIARYACCOUNTSRESPONSE._serialized_end = 1223
    _CONNECTEDINTERMEDIARYACCOUNTREQUEST._serialized_start = 1225
    _CONNECTEDINTERMEDIARYACCOUNTREQUEST._serialized_end = 1279
    _CONNECTEDINTERMEDIARYACCOUNTRESPONSE._serialized_start = 1281
    _CONNECTEDINTERMEDIARYACCOUNTRESPONSE._serialized_end = 1391
    _QUERYTOTALDELEGATIONBYVALIDATORFORDENOMREQUEST._serialized_start = 1393
    _QUERYTOTALDELEGATIONBYVALIDATORFORDENOMREQUEST._serialized_end = 1456
    _QUERYTOTALDELEGATIONBYVALIDATORFORDENOMRESPONSE._serialized_start = 1458
    _QUERYTOTALDELEGATIONBYVALIDATORFORDENOMRESPONSE._serialized_end = 1562
    _DELEGATIONS._serialized_start = 1565
    _DELEGATIONS._serialized_end = 1786
    _TOTALSUPERFLUIDDELEGATIONSREQUEST._serialized_start = 1788
    _TOTALSUPERFLUIDDELEGATIONSREQUEST._serialized_end = 1823
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE._serialized_start = 1826
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE._serialized_end = 1976
    _SUPERFLUIDDELEGATIONAMOUNTREQUEST._serialized_start = 1978
    _SUPERFLUIDDELEGATIONAMOUNTREQUEST._serialized_end = 2082
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE._serialized_start = 2085
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE._serialized_end = 2214
    _SUPERFLUIDDELEGATIONSBYDELEGATORREQUEST._serialized_start = 2216
    _SUPERFLUIDDELEGATIONSBYDELEGATORREQUEST._serialized_end = 2284
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE._serialized_start = 2287
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE._serialized_end = 2646
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORREQUEST._serialized_start = 2648
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORREQUEST._serialized_end = 2733
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE._serialized_start = 2736
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE._serialized_end = 3045
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMREQUEST._serialized_start = 3047
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMREQUEST._serialized_end = 3135
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE._serialized_start = 3138
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE._serialized_end = 3278
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMREQUEST._serialized_start = 3280
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMREQUEST._serialized_end = 3380
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE._serialized_start = 3383
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE._serialized_end = 3550
    _QUERYTOTALDELEGATIONBYDELEGATORREQUEST._serialized_start = 3552
    _QUERYTOTALDELEGATIONBYDELEGATORREQUEST._serialized_end = 3619
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE._serialized_start = 3622
    _QUERYTOTALDELEGATIONBYDELEGATORRESPONSE._serialized_end = 4059
    _QUERYUNPOOLWHITELISTREQUEST._serialized_start = 4061
    _QUERYUNPOOLWHITELISTREQUEST._serialized_end = 4090
    _QUERYUNPOOLWHITELISTRESPONSE._serialized_start = 4092
    _QUERYUNPOOLWHITELISTRESPONSE._serialized_end = 4140
    _QUERY._serialized_start = 4143
    _QUERY._serialized_end = 7213