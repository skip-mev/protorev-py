"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....osmosis.gamm.pool_models.stableswap import stableswap_pool_pb2 as osmosis_dot_gamm_dot_pool__models_dot_stableswap_dot_stableswap__pool__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,osmosis/gamm/pool-models/stableswap/tx.proto\x12*osmosis.gamm.poolmodels.stableswap.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a9osmosis/gamm/pool-models/stableswap/stableswap_pool.proto"\xd5\x03\n\x17MsgCreateStableswapPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12c\n\x0bpool_params\x18\x02 \x01(\x0b26.osmosis.gamm.poolmodels.stableswap.v1beta1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:"pool_params"\x12k\n\x16initial_pool_liquidity\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12=\n\x0fscaling_factors\x18\x04 \x03(\x04B$\xf2\xde\x1f yaml:"stableswap_scaling_factor"\x12=\n\x14future_pool_governor\x18\x05 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor"\x12G\n\x19scaling_factor_controller\x18\x06 \x01(\tB$\xf2\xde\x1f yaml:"scaling_factor_controller"">\n\x1fMsgCreateStableswapPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID"\xa2\x01\n!MsgStableSwapAdjustScalingFactors\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x1b\n\x07pool_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PoolID\x12=\n\x0fscaling_factors\x18\x03 \x03(\x04B$\xf2\xde\x1f yaml:"stableswap_scaling_factor""+\n)MsgStableSwapAdjustScalingFactorsResponse2\xf9\x02\n\x03Msg\x12\xa8\x01\n\x14CreateStableswapPool\x12C.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgCreateStableswapPool\x1aK.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgCreateStableswapPoolResponse\x12\xc6\x01\n\x1eStableSwapAdjustScalingFactors\x12M.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgStableSwapAdjustScalingFactors\x1aU.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgStableSwapAdjustScalingFactorsResponseBCZAgithub.com/osmosis-labs/osmosis/v14/x/gamm/pool-models/stableswapb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.pool_models.stableswap.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZAgithub.com/osmosis-labs/osmosis/v14/x/gamm/pool-models/stableswap'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['sender']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['pool_params']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['pool_params']._serialized_options = b'\xf2\xde\x1f\x12yaml:"pool_params"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['initial_pool_liquidity']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['initial_pool_liquidity']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['scaling_factors']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['scaling_factors']._serialized_options = b'\xf2\xde\x1f yaml:"stableswap_scaling_factor"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['future_pool_governor']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['scaling_factor_controller']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['scaling_factor_controller']._serialized_options = b'\xf2\xde\x1f yaml:"scaling_factor_controller"'
    _MSGCREATESTABLESWAPPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATESTABLESWAPPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['sender']._options = None
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['pool_id']._options = None
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['scaling_factors']._options = None
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['scaling_factors']._serialized_options = b'\xf2\xde\x1f yaml:"stableswap_scaling_factor"'
    _MSGCREATESTABLESWAPPOOL._serialized_start = 206
    _MSGCREATESTABLESWAPPOOL._serialized_end = 675
    _MSGCREATESTABLESWAPPOOLRESPONSE._serialized_start = 677
    _MSGCREATESTABLESWAPPOOLRESPONSE._serialized_end = 739
    _MSGSTABLESWAPADJUSTSCALINGFACTORS._serialized_start = 742
    _MSGSTABLESWAPADJUSTSCALINGFACTORS._serialized_end = 904
    _MSGSTABLESWAPADJUSTSCALINGFACTORSRESPONSE._serialized_start = 906
    _MSGSTABLESWAPADJUSTSCALINGFACTORSRESPONSE._serialized_end = 949
    _MSG._serialized_start = 952
    _MSG._serialized_end = 1329