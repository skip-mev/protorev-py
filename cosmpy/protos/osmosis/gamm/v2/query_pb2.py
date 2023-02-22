"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.gamm.v1beta1 import tx_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bosmosis/gamm/v2/query.proto\x12\x0fosmosis.gamm.v2\x1a\x14gogoproto/gogo.proto\x1a\x1dosmosis/gamm/v1beta1/tx.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto"\xac\x01\n\x15QuerySpotPriceRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x125\n\x10base_asset_denom\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"base_asset_denom"\x127\n\x11quote_asset_denom\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"quote_asset_denom""C\n\x16QuerySpotPriceResponse\x12)\n\nspot_price\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"spot_price"2\x97\x01\n\x05Query\x12\x8d\x01\n\tSpotPrice\x12&.osmosis.gamm.v2.QuerySpotPriceRequest\x1a\'.osmosis.gamm.v2.QuerySpotPriceResponse"/\x82\xd3\xe4\x93\x02)\x12\'/osmosis/gamm/v2/pools/{pool_id}/pricesB4Z2github.com/osmosis-labs/osmosis/v14/x/gamm/v2typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.v2.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v14/x/gamm/v2types'
    _QUERYSPOTPRICEREQUEST.fields_by_name['pool_id']._options = None
    _QUERYSPOTPRICEREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYSPOTPRICEREQUEST.fields_by_name['base_asset_denom']._options = None
    _QUERYSPOTPRICEREQUEST.fields_by_name['base_asset_denom']._serialized_options = b'\xf2\xde\x1f\x17yaml:"base_asset_denom"'
    _QUERYSPOTPRICEREQUEST.fields_by_name['quote_asset_denom']._options = None
    _QUERYSPOTPRICEREQUEST.fields_by_name['quote_asset_denom']._serialized_options = b'\xf2\xde\x1f\x18yaml:"quote_asset_denom"'
    _QUERYSPOTPRICERESPONSE.fields_by_name['spot_price']._options = None
    _QUERYSPOTPRICERESPONSE.fields_by_name['spot_price']._serialized_options = b'\xf2\xde\x1f\x11yaml:"spot_price"'
    _QUERY.methods_by_name['SpotPrice']._options = None
    _QUERY.methods_by_name['SpotPrice']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/osmosis/gamm/v2/pools/{pool_id}/prices"
    _QUERYSPOTPRICEREQUEST._serialized_start = 262
    _QUERYSPOTPRICEREQUEST._serialized_end = 434
    _QUERYSPOTPRICERESPONSE._serialized_start = 436
    _QUERYSPOTPRICERESPONSE._serialized_end = 503
    _QUERY._serialized_start = 506
    _QUERY._serialized_end = 657