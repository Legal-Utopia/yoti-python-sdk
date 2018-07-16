# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signing.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import attribute_pb2 as attribute__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='signing.proto',
  package='attrpubapi_v1',
  syntax='proto3',
  serialized_pb=_b('\n\rsigning.proto\x12\rattrpubapi_v1\x1a\x0f\x61ttribute.proto\"\xaa\x01\n\x10\x41ttributeSigning\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x30\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32\x1a.attrpubapi_v1.ContentType\x12\x1a\n\x12\x61rtifact_signature\x18\x04 \x01(\x0c\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x19\n\x11signed_time_stamp\x18\x06 \x01(\x0c\x42#\n\x16\x63om.yoti.attrpubapi_v1B\tAttrProtob\x06proto3')
  ,
  dependencies=[attribute__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ATTRIBUTESIGNING = _descriptor.Descriptor(
  name='AttributeSigning',
  full_name='attrpubapi_v1.AttributeSigning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='attrpubapi_v1.AttributeSigning.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='attrpubapi_v1.AttributeSigning.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='attrpubapi_v1.AttributeSigning.content_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='artifact_signature', full_name='attrpubapi_v1.AttributeSigning.artifact_signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='attrpubapi_v1.AttributeSigning.sub_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signed_time_stamp', full_name='attrpubapi_v1.AttributeSigning.signed_time_stamp', index=5,
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
  serialized_start=50,
  serialized_end=220,
)

_ATTRIBUTESIGNING.fields_by_name['content_type'].enum_type = attribute__pb2._CONTENTTYPE
DESCRIPTOR.message_types_by_name['AttributeSigning'] = _ATTRIBUTESIGNING

AttributeSigning = _reflection.GeneratedProtocolMessageType('AttributeSigning', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTESIGNING,
  __module__ = 'signing_pb2'
  # @@protoc_insertion_point(class_scope:attrpubapi_v1.AttributeSigning)
  ))
_sym_db.RegisterMessage(AttributeSigning)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.yoti.attrpubapi_v1B\tAttrProto'))
# @@protoc_insertion_point(module_scope)
