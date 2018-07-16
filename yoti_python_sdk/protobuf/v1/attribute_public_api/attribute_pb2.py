# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attribute.proto

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='attribute.proto',
  package='attrpubapi_v1',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x61ttribute.proto\x12\rattrpubapi_v1\"\x82\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x30\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32\x1a.attrpubapi_v1.ContentType\x12&\n\x07\x61nchors\x18\x04 \x03(\x0b\x32\x15.attrpubapi_v1.Anchor\"\x98\x01\n\x06\x41nchor\x12\x15\n\rartifact_link\x18\x01 \x01(\x0c\x12\x1b\n\x13origin_server_certs\x18\x02 \x03(\x0c\x12\x1a\n\x12\x61rtifact_signature\x18\x03 \x01(\x0c\x12\x10\n\x08sub_type\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\x0c\x12\x19\n\x11signed_time_stamp\x18\x06 \x01(\x0c*O\n\x0b\x43ontentType\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x08\n\x04JPEG\x10\x02\x12\x08\n\x04\x44\x41TE\x10\x03\x12\x07\n\x03PNG\x10\x04\x12\x08\n\x04JSON\x10\x05\x42#\n\x16\x63om.yoti.attrpubapi_v1B\tAttrProtob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='attrpubapi_v1.ContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JPEG', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNG', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=322,
  serialized_end=401,
)
_sym_db.RegisterEnumDescriptor(_CONTENTTYPE)

ContentType = enum_type_wrapper.EnumTypeWrapper(_CONTENTTYPE)
UNDEFINED = 0
STRING = 1
JPEG = 2
DATE = 3
PNG = 4
JSON = 5



_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='attrpubapi_v1.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='attrpubapi_v1.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='attrpubapi_v1.Attribute.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='attrpubapi_v1.Attribute.content_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchors', full_name='attrpubapi_v1.Attribute.anchors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=165,
)


_ANCHOR = _descriptor.Descriptor(
  name='Anchor',
  full_name='attrpubapi_v1.Anchor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='artifact_link', full_name='attrpubapi_v1.Anchor.artifact_link', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin_server_certs', full_name='attrpubapi_v1.Anchor.origin_server_certs', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='artifact_signature', full_name='attrpubapi_v1.Anchor.artifact_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='attrpubapi_v1.Anchor.sub_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='attrpubapi_v1.Anchor.signature', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signed_time_stamp', full_name='attrpubapi_v1.Anchor.signed_time_stamp', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=320,
)

_ATTRIBUTE.fields_by_name['content_type'].enum_type = _CONTENTTYPE
_ATTRIBUTE.fields_by_name['anchors'].message_type = _ANCHOR
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name['Anchor'] = _ANCHOR
DESCRIPTOR.enum_types_by_name['ContentType'] = _CONTENTTYPE

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTE,
  __module__ = 'attribute_pb2'
  # @@protoc_insertion_point(class_scope:attrpubapi_v1.Attribute)
  ))
_sym_db.RegisterMessage(Attribute)

Anchor = _reflection.GeneratedProtocolMessageType('Anchor', (_message.Message,), dict(
  DESCRIPTOR = _ANCHOR,
  __module__ = 'attribute_pb2'
  # @@protoc_insertion_point(class_scope:attrpubapi_v1.Anchor)
  ))
_sym_db.RegisterMessage(Anchor)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.yoti.attrpubapi_v1B\tAttrProto'))
# @@protoc_insertion_point(module_scope)
