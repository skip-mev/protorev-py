"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....osmosis.valset_pref.v1beta1 import state_pb2 as osmosis_dot_valset__pref_dot_v1beta1_dot_state__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$osmosis/valset-pref/v1beta1/tx.proto\x12\x1aosmosis.valsetpref.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\'osmosis/valset-pref/v1beta1/state.proto"\xa9\x01\n\x1cMsgSetValidatorSetPreference\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12`\n\x0bpreferences\x18\x02 \x03(\x0b2/.osmosis.valsetpref.v1beta1.ValidatorPreferenceB\x1a\xf2\xde\x1f\x12yaml:"preferences"\xc8\xde\x1f\x00"&\n$MsgSetValidatorSetPreferenceResponse"\x9e\x01\n\x19MsgDelegateToValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12X\n\x04coin\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin"#\n!MsgDelegateToValidatorSetResponse"\xa2\x01\n\x1dMsgUndelegateFromValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12X\n\x04coin\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin"\'\n%MsgUndelegateFromValidatorSetResponse"\xa6\x01\n\x19MsgRedelegateValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12`\n\x0bpreferences\x18\x02 \x03(\x0b2/.osmosis.valsetpref.v1beta1.ValidatorPreferenceB\x1a\xf2\xde\x1f\x12yaml:"preferences"\xc8\xde\x1f\x00"#\n!MsgRedelegateValidatorSetResponse"G\n\x1cMsgWithdrawDelegationRewards\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator""&\n$MsgWithdrawDelegationRewardsResponse"R\n\x17MsgDelegateBondedTokens\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12\x0e\n\x06lockID\x18\x02 \x01(\x04"!\n\x1fMsgDelegateBondedTokensResponse2\x83\x07\n\x03Msg\x12\x97\x01\n\x19SetValidatorSetPreference\x128.osmosis.valsetpref.v1beta1.MsgSetValidatorSetPreference\x1a@.osmosis.valsetpref.v1beta1.MsgSetValidatorSetPreferenceResponse\x12\x8e\x01\n\x16DelegateToValidatorSet\x125.osmosis.valsetpref.v1beta1.MsgDelegateToValidatorSet\x1a=.osmosis.valsetpref.v1beta1.MsgDelegateToValidatorSetResponse\x12\x9a\x01\n\x1aUndelegateFromValidatorSet\x129.osmosis.valsetpref.v1beta1.MsgUndelegateFromValidatorSet\x1aA.osmosis.valsetpref.v1beta1.MsgUndelegateFromValidatorSetResponse\x12\x8e\x01\n\x16RedelegateValidatorSet\x125.osmosis.valsetpref.v1beta1.MsgRedelegateValidatorSet\x1a=.osmosis.valsetpref.v1beta1.MsgRedelegateValidatorSetResponse\x12\x97\x01\n\x19WithdrawDelegationRewards\x128.osmosis.valsetpref.v1beta1.MsgWithdrawDelegationRewards\x1a@.osmosis.valsetpref.v1beta1.MsgWithdrawDelegationRewardsResponse\x12\x88\x01\n\x14DelegateBondedTokens\x123.osmosis.valsetpref.v1beta1.MsgDelegateBondedTokens\x1a;.osmosis.valsetpref.v1beta1.MsgDelegateBondedTokensResponseB9Z7github.com/osmosis-labs/osmosis/v14/x/valset-pref/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.valset_pref.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v14/x/valset-pref/types'
    _MSGSETVALIDATORSETPREFERENCE.fields_by_name['delegator']._options = None
    _MSGSETVALIDATORSETPREFERENCE.fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _MSGSETVALIDATORSETPREFERENCE.fields_by_name['preferences']._options = None
    _MSGSETVALIDATORSETPREFERENCE.fields_by_name['preferences']._serialized_options = b'\xf2\xde\x1f\x12yaml:"preferences"\xc8\xde\x1f\x00'
    _MSGDELEGATETOVALIDATORSET.fields_by_name['delegator']._options = None
    _MSGDELEGATETOVALIDATORSET.fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _MSGDELEGATETOVALIDATORSET.fields_by_name['coin']._options = None
    _MSGDELEGATETOVALIDATORSET.fields_by_name['coin']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _MSGUNDELEGATEFROMVALIDATORSET.fields_by_name['delegator']._options = None
    _MSGUNDELEGATEFROMVALIDATORSET.fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _MSGUNDELEGATEFROMVALIDATORSET.fields_by_name['coin']._options = None
    _MSGUNDELEGATEFROMVALIDATORSET.fields_by_name['coin']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _MSGREDELEGATEVALIDATORSET.fields_by_name['delegator']._options = None
    _MSGREDELEGATEVALIDATORSET.fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _MSGREDELEGATEVALIDATORSET.fields_by_name['preferences']._options = None
    _MSGREDELEGATEVALIDATORSET.fields_by_name['preferences']._serialized_options = b'\xf2\xde\x1f\x12yaml:"preferences"\xc8\xde\x1f\x00'
    _MSGWITHDRAWDELEGATIONREWARDS.fields_by_name['delegator']._options = None
    _MSGWITHDRAWDELEGATIONREWARDS.fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _MSGDELEGATEBONDEDTOKENS.fields_by_name['delegator']._options = None
    _MSGDELEGATEBONDEDTOKENS.fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _MSGSETVALIDATORSETPREFERENCE._serialized_start = 197
    _MSGSETVALIDATORSETPREFERENCE._serialized_end = 366
    _MSGSETVALIDATORSETPREFERENCERESPONSE._serialized_start = 368
    _MSGSETVALIDATORSETPREFERENCERESPONSE._serialized_end = 406
    _MSGDELEGATETOVALIDATORSET._serialized_start = 409
    _MSGDELEGATETOVALIDATORSET._serialized_end = 567
    _MSGDELEGATETOVALIDATORSETRESPONSE._serialized_start = 569
    _MSGDELEGATETOVALIDATORSETRESPONSE._serialized_end = 604
    _MSGUNDELEGATEFROMVALIDATORSET._serialized_start = 607
    _MSGUNDELEGATEFROMVALIDATORSET._serialized_end = 769
    _MSGUNDELEGATEFROMVALIDATORSETRESPONSE._serialized_start = 771
    _MSGUNDELEGATEFROMVALIDATORSETRESPONSE._serialized_end = 810
    _MSGREDELEGATEVALIDATORSET._serialized_start = 813
    _MSGREDELEGATEVALIDATORSET._serialized_end = 979
    _MSGREDELEGATEVALIDATORSETRESPONSE._serialized_start = 981
    _MSGREDELEGATEVALIDATORSETRESPONSE._serialized_end = 1016
    _MSGWITHDRAWDELEGATIONREWARDS._serialized_start = 1018
    _MSGWITHDRAWDELEGATIONREWARDS._serialized_end = 1089
    _MSGWITHDRAWDELEGATIONREWARDSRESPONSE._serialized_start = 1091
    _MSGWITHDRAWDELEGATIONREWARDSRESPONSE._serialized_end = 1129
    _MSGDELEGATEBONDEDTOKENS._serialized_start = 1131
    _MSGDELEGATEBONDEDTOKENS._serialized_end = 1213
    _MSGDELEGATEBONDEDTOKENSRESPONSE._serialized_start = 1215
    _MSGDELEGATEBONDEDTOKENSRESPONSE._serialized_end = 1248
    _MSG._serialized_start = 1251
    _MSG._serialized_end = 2150