"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ......osmosis.gamm.pool_models.balancer import balancerPool_pb2 as osmosis_dot_gamm_dot_pool__models_dot_balancer_dot_balancerPool__pb2
from ......cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-osmosis/gamm/pool-models/balancer/tx/tx.proto\x12(osmosis.gamm.poolmodels.balancer.v1beta1\x1a\x14gogoproto/gogo.proto\x1a4osmosis/gamm/pool-models/balancer/balancerPool.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x84\x02\n\x15MsgCreateBalancerPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12M\n\x0bpool_params\x18\x02 \x01(\x0b2 .osmosis.gamm.v1beta1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:"pool_params"\x12:\n\x0bpool_assets\x18\x03 \x03(\x0b2\x1f.osmosis.gamm.v1beta1.PoolAssetB\x04\xc8\xde\x1f\x00\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor""<\n\x1dMsgCreateBalancerPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID"\xac\x01\n/MsgMigrateSharesToFullRangeConcentratedPosition\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12V\n\x11shares_to_migrate\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB \xf2\xde\x1f\x18yaml:"shares_to_migrate"\xc8\xde\x1f\x00"\xc6\x02\n7MsgMigrateSharesToFullRangeConcentratedPositionResponse\x12Q\n\x07amount0\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount0"\xc8\xde\x1f\x00\x12Q\n\x07amount1\x18\x02 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount1"\xc8\xde\x1f\x00\x12e\n\x11liquidity_created\x18\x03 \x01(\tBJ\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x18yaml:"liquidity_created"\xc8\xde\x1f\x002\x95\x03\n\x03Msg\x12\x9e\x01\n\x12CreateBalancerPool\x12?.osmosis.gamm.poolmodels.balancer.v1beta1.MsgCreateBalancerPool\x1aG.osmosis.gamm.poolmodels.balancer.v1beta1.MsgCreateBalancerPoolResponse\x12\xec\x01\n,MigrateSharesToFullRangeConcentratedPosition\x12Y.osmosis.gamm.poolmodels.balancer.v1beta1.MsgMigrateSharesToFullRangeConcentratedPosition\x1aa.osmosis.gamm.poolmodels.balancer.v1beta1.MsgMigrateSharesToFullRangeConcentratedPositionResponseBAZ?github.com/osmosis-labs/osmosis/v14/x/gamm/pool-models/balancerb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.pool_models.balancer.tx.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z?github.com/osmosis-labs/osmosis/v14/x/gamm/pool-models/balancer'
    _MSGCREATEBALANCERPOOL.fields_by_name['sender']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_params']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_params']._serialized_options = b'\xf2\xde\x1f\x12yaml:"pool_params"'
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_assets']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEBALANCERPOOL.fields_by_name['future_pool_governor']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _MSGCREATEBALANCERPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATEBALANCERPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITION.fields_by_name['sender']._options = None
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITION.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITION.fields_by_name['shares_to_migrate']._options = None
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITION.fields_by_name['shares_to_migrate']._serialized_options = b'\xf2\xde\x1f\x18yaml:"shares_to_migrate"\xc8\xde\x1f\x00'
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE.fields_by_name['amount0']._options = None
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE.fields_by_name['amount0']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount0"\xc8\xde\x1f\x00'
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE.fields_by_name['amount1']._options = None
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE.fields_by_name['amount1']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x0eyaml:"amount1"\xc8\xde\x1f\x00'
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE.fields_by_name['liquidity_created']._options = None
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE.fields_by_name['liquidity_created']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x18yaml:"liquidity_created"\xc8\xde\x1f\x00'
    _MSGCREATEBALANCERPOOL._serialized_start = 200
    _MSGCREATEBALANCERPOOL._serialized_end = 460
    _MSGCREATEBALANCERPOOLRESPONSE._serialized_start = 462
    _MSGCREATEBALANCERPOOLRESPONSE._serialized_end = 522
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITION._serialized_start = 525
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITION._serialized_end = 697
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE._serialized_start = 700
    _MSGMIGRATESHARESTOFULLRANGECONCENTRATEDPOSITIONRESPONSE._serialized_end = 1026
    _MSG._serialized_start = 1029
    _MSG._serialized_end = 1434