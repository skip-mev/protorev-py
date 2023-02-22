"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%osmosis/tokenfactory/v1beta1/tx.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto"Z\n\x0eMsgCreateDenom\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12%\n\x08subdenom\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"subdenom""M\n\x16MsgCreateDenomResponse\x123\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"new_token_denom""n\n\x07MsgMint\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12@\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00"\x11\n\x0fMsgMintResponse"n\n\x07MsgBurn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12@\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00"\x11\n\x0fMsgBurnResponse"}\n\x0eMsgChangeAdmin\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x1f\n\x05denom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"\x12\'\n\tnew_admin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"new_admin""\x18\n\x16MsgChangeAdminResponse"\x82\x01\n\x13MsgSetDenomMetadata\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12H\n\x08metadata\x18\x02 \x01(\x0b2\x1d.cosmos.bank.v1beta1.MetadataB\x17\xf2\xde\x1f\x0fyaml:"metadata"\xc8\xde\x1f\x00"\x1d\n\x1bMsgSetDenomMetadataResponse2\xaa\x04\n\x03Msg\x12q\n\x0bCreateDenom\x12,.osmosis.tokenfactory.v1beta1.MsgCreateDenom\x1a4.osmosis.tokenfactory.v1beta1.MsgCreateDenomResponse\x12\\\n\x04Mint\x12%.osmosis.tokenfactory.v1beta1.MsgMint\x1a-.osmosis.tokenfactory.v1beta1.MsgMintResponse\x12\\\n\x04Burn\x12%.osmosis.tokenfactory.v1beta1.MsgBurn\x1a-.osmosis.tokenfactory.v1beta1.MsgBurnResponse\x12q\n\x0bChangeAdmin\x12,.osmosis.tokenfactory.v1beta1.MsgChangeAdmin\x1a4.osmosis.tokenfactory.v1beta1.MsgChangeAdminResponse\x12\x80\x01\n\x10SetDenomMetadata\x121.osmosis.tokenfactory.v1beta1.MsgSetDenomMetadata\x1a9.osmosis.tokenfactory.v1beta1.MsgSetDenomMetadataResponseB:Z8github.com/osmosis-labs/osmosis/v14/x/tokenfactory/typesb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.tokenfactory.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/osmosis-labs/osmosis/v14/x/tokenfactory/types'
    _MSGCREATEDENOM.fields_by_name['sender']._options = None
    _MSGCREATEDENOM.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEDENOM.fields_by_name['subdenom']._options = None
    _MSGCREATEDENOM.fields_by_name['subdenom']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"subdenom"'
    _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._options = None
    _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"new_token_denom"'
    _MSGMINT.fields_by_name['sender']._options = None
    _MSGMINT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGMINT.fields_by_name['amount']._options = None
    _MSGMINT.fields_by_name['amount']._serialized_options = b'\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00'
    _MSGBURN.fields_by_name['sender']._options = None
    _MSGBURN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGBURN.fields_by_name['amount']._options = None
    _MSGBURN.fields_by_name['amount']._serialized_options = b'\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00'
    _MSGCHANGEADMIN.fields_by_name['sender']._options = None
    _MSGCHANGEADMIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCHANGEADMIN.fields_by_name['denom']._options = None
    _MSGCHANGEADMIN.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _MSGCHANGEADMIN.fields_by_name['new_admin']._options = None
    _MSGCHANGEADMIN.fields_by_name['new_admin']._serialized_options = b'\xf2\xde\x1f\x10yaml:"new_admin"'
    _MSGSETDENOMMETADATA.fields_by_name['sender']._options = None
    _MSGSETDENOMMETADATA.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSETDENOMMETADATA.fields_by_name['metadata']._options = None
    _MSGSETDENOMMETADATA.fields_by_name['metadata']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"metadata"\xc8\xde\x1f\x00'
    _MSGCREATEDENOM._serialized_start = 157
    _MSGCREATEDENOM._serialized_end = 247
    _MSGCREATEDENOMRESPONSE._serialized_start = 249
    _MSGCREATEDENOMRESPONSE._serialized_end = 326
    _MSGMINT._serialized_start = 328
    _MSGMINT._serialized_end = 438
    _MSGMINTRESPONSE._serialized_start = 440
    _MSGMINTRESPONSE._serialized_end = 457
    _MSGBURN._serialized_start = 459
    _MSGBURN._serialized_end = 569
    _MSGBURNRESPONSE._serialized_start = 571
    _MSGBURNRESPONSE._serialized_end = 588
    _MSGCHANGEADMIN._serialized_start = 590
    _MSGCHANGEADMIN._serialized_end = 715
    _MSGCHANGEADMINRESPONSE._serialized_start = 717
    _MSGCHANGEADMINRESPONSE._serialized_end = 741
    _MSGSETDENOMMETADATA._serialized_start = 744
    _MSGSETDENOMMETADATA._serialized_end = 874
    _MSGSETDENOMMETADATARESPONSE._serialized_start = 876
    _MSGSETDENOMMETADATARESPONSE._serialized_end = 905
    _MSG._serialized_start = 908
    _MSG._serialized_end = 1462