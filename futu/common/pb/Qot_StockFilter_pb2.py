# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_StockFilter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_StockFilter.proto',
  package='Qot_StockFilter',
  syntax='proto2',
  serialized_pb=_b('\n\x15Qot_StockFilter.proto\x12\x0fQot_StockFilter\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"f\n\nBaseFilter\x12\r\n\x05\x66ield\x18\x01 \x02(\x05\x12\x11\n\tfilterMin\x18\x02 \x01(\x01\x12\x11\n\tfilterMax\x18\x03 \x01(\x01\x12\x12\n\nisNoFilter\x18\x04 \x01(\x08\x12\x0f\n\x07sortDir\x18\x05 \x01(\x05\"(\n\x08\x42\x61seData\x12\r\n\x05\x66ield\x18\x01 \x02(\x05\x12\r\n\x05value\x18\x02 \x02(\x01\"r\n\tStockData\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\x12\x0c\n\x04name\x18\x02 \x02(\t\x12/\n\x0c\x62\x61seDataList\x18\x03 \x03(\x0b\x32\x19.Qot_StockFilter.BaseData\"\x8b\x01\n\x03\x43\x32S\x12\r\n\x05\x62\x65gin\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x02(\x05\x12\x0e\n\x06market\x18\x05 \x02(\x05\x12#\n\x05plate\x18\x06 \x01(\x0b\x32\x14.Qot_Common.Security\x12\x33\n\x0e\x62\x61seFilterList\x18\x07 \x03(\x0b\x32\x1b.Qot_StockFilter.BaseFilter\"W\n\x03S2C\x12\x10\n\x08lastPage\x18\x01 \x02(\x08\x12\x10\n\x08\x61llCount\x18\x02 \x02(\x05\x12,\n\x08\x64\x61taList\x18\x03 \x03(\x0b\x32\x1a.Qot_StockFilter.StockData\",\n\x07Request\x12!\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x14.Qot_StockFilter.C2S\"e\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12!\n\x03s2c\x18\x04 \x01(\x0b\x32\x14.Qot_StockFilter.S2C*b\n\x0bStockMarket\x12\x17\n\x13StockMarket_Unknown\x10\x00\x12\x12\n\x0eStockMarket_HK\x10\x01\x12\x12\n\x0eStockMarket_US\x10\x02\x12\x12\n\x0eStockMarket_CN\x10\x03*\xd9\x03\n\nStockField\x12\x16\n\x12StockField_Unknown\x10\x00\x12\x18\n\x14StockField_StockCode\x10\x01\x12\x18\n\x14StockField_StockName\x10\x02\x12\x17\n\x13StockField_CurPrice\x10\x03\x12,\n(StockField_CurPriceToHighest52WeeksRatio\x10\x04\x12+\n\'StockField_CurPriceToLowest52WeeksRatio\x10\x05\x12-\n)StockField_HighPriceToHighest52WeeksRatio\x10\x06\x12+\n\'StockField_LowPriceToLowest52WeeksRatio\x10\x07\x12\x1a\n\x16StockField_VolumeRatio\x10\x08\x12\x1a\n\x16StockField_BidAskRatio\x10\t\x12\x17\n\x13StockField_LotPrice\x10\n\x12\x18\n\x14StockField_MarketVal\x10\x0b\x12\x17\n\x13StockField_PeAnnual\x10\x0c\x12\x14\n\x10StockField_PeTTM\x10\r\x12\x15\n\x11StockField_PbRate\x10\x0e*W\n\x07SortDir\x12\x13\n\x0fSortDir_Unknown\x10\x00\x12\x0e\n\nSortDir_No\x10\x01\x12\x12\n\x0eSortDir_Ascend\x10\x02\x12\x13\n\x0fSortDir_Descend\x10\x03\x42\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])

_STOCKMARKET = _descriptor.EnumDescriptor(
  name='StockMarket',
  full_name='Qot_StockFilter.StockMarket',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='StockMarket_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockMarket_HK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockMarket_US', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockMarket_CN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=716,
  serialized_end=814,
)
_sym_db.RegisterEnumDescriptor(_STOCKMARKET)

StockMarket = enum_type_wrapper.EnumTypeWrapper(_STOCKMARKET)
_STOCKFIELD = _descriptor.EnumDescriptor(
  name='StockField',
  full_name='Qot_StockFilter.StockField',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='StockField_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_StockCode', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_StockName', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_CurPrice', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_CurPriceToHighest52WeeksRatio', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_CurPriceToLowest52WeeksRatio', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_HighPriceToHighest52WeeksRatio', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_LowPriceToLowest52WeeksRatio', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_VolumeRatio', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_BidAskRatio', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_LotPrice', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_MarketVal', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_PeAnnual', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_PeTTM', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StockField_PbRate', index=14, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=817,
  serialized_end=1290,
)
_sym_db.RegisterEnumDescriptor(_STOCKFIELD)

StockField = enum_type_wrapper.EnumTypeWrapper(_STOCKFIELD)
_SORTDIR = _descriptor.EnumDescriptor(
  name='SortDir',
  full_name='Qot_StockFilter.SortDir',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SortDir_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SortDir_No', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SortDir_Ascend', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SortDir_Descend', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1292,
  serialized_end=1379,
)
_sym_db.RegisterEnumDescriptor(_SORTDIR)

SortDir = enum_type_wrapper.EnumTypeWrapper(_SORTDIR)
StockMarket_Unknown = 0
StockMarket_HK = 1
StockMarket_US = 2
StockMarket_CN = 3
StockField_Unknown = 0
StockField_StockCode = 1
StockField_StockName = 2
StockField_CurPrice = 3
StockField_CurPriceToHighest52WeeksRatio = 4
StockField_CurPriceToLowest52WeeksRatio = 5
StockField_HighPriceToHighest52WeeksRatio = 6
StockField_LowPriceToLowest52WeeksRatio = 7
StockField_VolumeRatio = 8
StockField_BidAskRatio = 9
StockField_LotPrice = 10
StockField_MarketVal = 11
StockField_PeAnnual = 12
StockField_PeTTM = 13
StockField_PbRate = 14
SortDir_Unknown = 0
SortDir_No = 1
SortDir_Ascend = 2
SortDir_Descend = 3



_BASEFILTER = _descriptor.Descriptor(
  name='BaseFilter',
  full_name='Qot_StockFilter.BaseFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='Qot_StockFilter.BaseFilter.field', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterMin', full_name='Qot_StockFilter.BaseFilter.filterMin', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterMax', full_name='Qot_StockFilter.BaseFilter.filterMax', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isNoFilter', full_name='Qot_StockFilter.BaseFilter.isNoFilter', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sortDir', full_name='Qot_StockFilter.BaseFilter.sortDir', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=176,
)


_BASEDATA = _descriptor.Descriptor(
  name='BaseData',
  full_name='Qot_StockFilter.BaseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='Qot_StockFilter.BaseData.field', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Qot_StockFilter.BaseData.value', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=218,
)


_STOCKDATA = _descriptor.Descriptor(
  name='StockData',
  full_name='Qot_StockFilter.StockData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_StockFilter.StockData.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Qot_StockFilter.StockData.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baseDataList', full_name='Qot_StockFilter.StockData.baseDataList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=334,
)


_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_StockFilter.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='begin', full_name='Qot_StockFilter.C2S.begin', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='Qot_StockFilter.C2S.num', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market', full_name='Qot_StockFilter.C2S.market', index=2,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plate', full_name='Qot_StockFilter.C2S.plate', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baseFilterList', full_name='Qot_StockFilter.C2S.baseFilterList', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=476,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_StockFilter.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lastPage', full_name='Qot_StockFilter.S2C.lastPage', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allCount', full_name='Qot_StockFilter.S2C.allCount', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataList', full_name='Qot_StockFilter.S2C.dataList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=565,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_StockFilter.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_StockFilter.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=611,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_StockFilter.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_StockFilter.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_StockFilter.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_StockFilter.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_StockFilter.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=613,
  serialized_end=714,
)

_STOCKDATA.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_STOCKDATA.fields_by_name['baseDataList'].message_type = _BASEDATA
_C2S.fields_by_name['plate'].message_type = Qot__Common__pb2._SECURITY
_C2S.fields_by_name['baseFilterList'].message_type = _BASEFILTER
_S2C.fields_by_name['dataList'].message_type = _STOCKDATA
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['BaseFilter'] = _BASEFILTER
DESCRIPTOR.message_types_by_name['BaseData'] = _BASEDATA
DESCRIPTOR.message_types_by_name['StockData'] = _STOCKDATA
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['StockMarket'] = _STOCKMARKET
DESCRIPTOR.enum_types_by_name['StockField'] = _STOCKFIELD
DESCRIPTOR.enum_types_by_name['SortDir'] = _SORTDIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BaseFilter = _reflection.GeneratedProtocolMessageType('BaseFilter', (_message.Message,), dict(
  DESCRIPTOR = _BASEFILTER,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.BaseFilter)
  ))
_sym_db.RegisterMessage(BaseFilter)

BaseData = _reflection.GeneratedProtocolMessageType('BaseData', (_message.Message,), dict(
  DESCRIPTOR = _BASEDATA,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.BaseData)
  ))
_sym_db.RegisterMessage(BaseData)

StockData = _reflection.GeneratedProtocolMessageType('StockData', (_message.Message,), dict(
  DESCRIPTOR = _STOCKDATA,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.StockData)
  ))
_sym_db.RegisterMessage(StockData)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_StockFilter_pb2'
  # @@protoc_insertion_point(class_scope:Qot_StockFilter.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
