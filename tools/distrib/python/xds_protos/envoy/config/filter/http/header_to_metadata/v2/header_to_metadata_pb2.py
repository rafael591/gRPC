# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/header_to_metadata/v2/header_to_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGenvoy/config/filter/http/header_to_metadata/v2/header_to_metadata.proto\x12.envoy.config.filter.http.header_to_metadata.v2\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xfd\x05\n\x06\x43onfig\x12R\n\rrequest_rules\x18\x01 \x03(\x0b\x32;.envoy.config.filter.http.header_to_metadata.v2.Config.Rule\x12S\n\x0eresponse_rules\x18\x02 \x03(\x0b\x32;.envoy.config.filter.http.header_to_metadata.v2.Config.Rule\x1a\xf3\x01\n\x0cKeyValuePair\x12\x1a\n\x12metadata_namespace\x18\x01 \x01(\t\x12\x14\n\x03key\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12\r\n\x05value\x18\x03 \x01(\t\x12N\n\x04type\x18\x04 \x01(\x0e\x32@.envoy.config.filter.http.header_to_metadata.v2.Config.ValueType\x12R\n\x06\x65ncode\x18\x05 \x01(\x0e\x32\x42.envoy.config.filter.http.header_to_metadata.v2.Config.ValueEncode\x1a\xf5\x01\n\x04Rule\x12\x1d\n\x06header\x18\x01 \x01(\tB\r\xfa\x42\nr\x08 \x01\xc0\x01\x01\xc8\x01\x00\x12^\n\x11on_header_present\x18\x02 \x01(\x0b\x32\x43.envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair\x12^\n\x11on_header_missing\x18\x03 \x01(\x0b\x32\x43.envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair\x12\x0e\n\x06remove\x18\x04 \x01(\x08\"7\n\tValueType\x12\n\n\x06STRING\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\x12\n\x0ePROTOBUF_VALUE\x10\x02\"#\n\x0bValueEncode\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x42\x41SE64\x10\x01\x42\x86\x02\n<io.envoyproxy.envoy.config.filter.http.header_to_metadata.v2B\x15HeaderToMetadataProtoP\x01Zjgithub.com/envoyproxy/go-control-plane/envoy/config/filter/http/header_to_metadata/v2;header_to_metadatav2\xf2\x98\xfe\x8f\x05\x35\x12\x33\x65nvoy.extensions.filters.http.header_to_metadata.v3\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.filter.http.header_to_metadata.v2.header_to_metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n<io.envoyproxy.envoy.config.filter.http.header_to_metadata.v2B\025HeaderToMetadataProtoP\001Zjgithub.com/envoyproxy/go-control-plane/envoy/config/filter/http/header_to_metadata/v2;header_to_metadatav2\362\230\376\217\0055\0223envoy.extensions.filters.http.header_to_metadata.v3\272\200\310\321\006\002\020\001'
  _CONFIG_KEYVALUEPAIR.fields_by_name['key']._options = None
  _CONFIG_KEYVALUEPAIR.fields_by_name['key']._serialized_options = b'\372B\004r\002 \001'
  _CONFIG_RULE.fields_by_name['header']._options = None
  _CONFIG_RULE.fields_by_name['header']._serialized_options = b'\372B\nr\010 \001\300\001\001\310\001\000'
  _globals['_CONFIG']._serialized_start=212
  _globals['_CONFIG']._serialized_end=977
  _globals['_CONFIG_KEYVALUEPAIR']._serialized_start=392
  _globals['_CONFIG_KEYVALUEPAIR']._serialized_end=635
  _globals['_CONFIG_RULE']._serialized_start=638
  _globals['_CONFIG_RULE']._serialized_end=883
  _globals['_CONFIG_VALUETYPE']._serialized_start=885
  _globals['_CONFIG_VALUETYPE']._serialized_end=940
  _globals['_CONFIG_VALUEENCODE']._serialized_start=942
  _globals['_CONFIG_VALUEENCODE']._serialized_end=977
# @@protoc_insertion_point(module_scope)
