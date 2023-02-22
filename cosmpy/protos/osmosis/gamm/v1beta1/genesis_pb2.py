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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"osmosis/gamm/v1beta1/genesis.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x8d\x01\n\x06Params\x12\x82\x01\n\x11pool_creation_fee\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBL\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:"pool_creation_fee"\xc8\xde\x1f\x00"\xcf\x01\n\x0cGenesisState\x12.\n\x05pools\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\x12\x18\n\x10next_pool_number\x18\x02 \x01(\x04\x122\n\x06params\x18\x03 \x01(\x0b2\x1c.osmosis.gamm.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12A\n\x11migration_records\x18\x04 \x01(\x0b2&.osmosis.gamm.v1beta1.MigrationRecords"{\n\x10MigrationRecords\x12g\n#balancer_to_concentrated_pool_links\x18\x01 \x03(\x0b24.osmosis.gamm.v1beta1.BalancerToConcentratedPoolLinkB\x04\xc8\xde\x1f\x00"T\n\x1eBalancerToConcentratedPoolLink\x12\x18\n\x10balancer_pool_id\x18\x01 \x01(\x04\x12\x12\n\ncl_pool_id\x18\x02 \x01(\x04:\x04\xe8\xa0\x1f\x01B2Z0github.com/osmosis-labs/osmosis/v14/x/gamm/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/osmosis-labs/osmosis/v14/x/gamm/types'
    _PARAMS.fields_by_name['pool_creation_fee']._options = None
    _PARAMS.fields_by_name['pool_creation_fee']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:"pool_creation_fee"\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['pools']._options = None
    _GENESISSTATE.fields_by_name['pools']._serialized_options = b'\xca\xb4-\x05PoolI'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _MIGRATIONRECORDS.fields_by_name['balancer_to_concentrated_pool_links']._options = None
    _MIGRATIONRECORDS.fields_by_name['balancer_to_concentrated_pool_links']._serialized_options = b'\xc8\xde\x1f\x00'
    _BALANCERTOCONCENTRATEDPOOLLINK._options = None
    _BALANCERTOCONCENTRATEDPOOLLINK._serialized_options = b'\xe8\xa0\x1f\x01'
    _PARAMS._serialized_start = 169
    _PARAMS._serialized_end = 310
    _GENESISSTATE._serialized_start = 313
    _GENESISSTATE._serialized_end = 520
    _MIGRATIONRECORDS._serialized_start = 522
    _MIGRATIONRECORDS._serialized_end = 645
    _BALANCERTOCONCENTRATEDPOOLLINK._serialized_start = 647
    _BALANCERTOCONCENTRATEDPOOLLINK._serialized_end = 731