# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/variables.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protos/variables.proto\x12\x0b\x61ngr.protos\"\x90\x01\n\x0cVariableBase\x12\r\n\x05ident\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x06region\x18\x03 \x01(\x04H\x00\x88\x01\x01\x12\x15\n\x08\x63\x61tegory\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x0f\n\x07renamed\x18\x05 \x01(\x08\x12\x0e\n\x06is_phi\x18\x06 \x01(\x08\x42\t\n\x07_regionB\x0b\n\t_category\"L\n\x11TemporaryVariable\x12\'\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x19.angr.protos.VariableBase\x12\x0e\n\x06tmp_id\x18\x02 \x01(\r\"V\n\x10RegisterVariable\x12\'\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x19.angr.protos.VariableBase\x12\x0b\n\x03reg\x18\x02 \x01(\r\x12\x0c\n\x04size\x18\x03 \x01(\r\"U\n\x0eMemoryVariable\x12\'\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x19.angr.protos.VariableBase\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\r\"u\n\rStackVariable\x12\'\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x19.angr.protos.VariableBase\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\r\x12\x0f\n\x07sp_base\x18\x04 \x01(\x08\x12\x0e\n\x06offset\x18\x05 \x01(\x05\"\x9c\x02\n\x0eVariableAccess\x12\r\n\x05ident\x18\x01 \x01(\t\x12\x12\n\nblock_addr\x18\x02 \x01(\x04\x12\x10\n\x08stmt_idx\x18\x03 \x01(\x05\x12\x10\n\x08ins_addr\x18\x04 \x01(\x04\x12\x13\n\x06offset\x18\x05 \x01(\x03H\x00\x88\x01\x01\x12\x43\n\x0b\x61\x63\x63\x65ss_type\x18\x06 \x01(\x0e\x32..angr.protos.VariableAccess.VariableAccessSort\x12\x16\n\tatom_hash\x18\x07 \x01(\rH\x01\x88\x01\x01\"8\n\x12VariableAccessSort\x12\t\n\x05WRITE\x10\x00\x12\x08\n\x04READ\x10\x01\x12\r\n\tREFERENCE\x10\x02\x42\t\n\x07_offsetB\x0c\n\n_atom_hash\"/\n\x0cVariableType\x12\r\n\x05ident\x18\x01 \x01(\t\x12\x10\n\x08var_type\x18\x02 \x01(\t\";\n\x0bVar2Unified\x12\x11\n\tvar_ident\x18\x01 \x01(\t\x12\x19\n\x11unified_var_ident\x18\x02 \x01(\t\"/\n\x07Phi2Var\x12\x11\n\tphi_ident\x18\x01 \x01(\t\x12\x11\n\tvar_ident\x18\x02 \x01(\t\"\xe6\x04\n\x17VariableManagerInternal\x12\x30\n\x08tempvars\x18\x01 \x03(\x0b\x32\x1e.angr.protos.TemporaryVariable\x12.\n\x07regvars\x18\x02 \x03(\x0b\x32\x1d.angr.protos.RegisterVariable\x12,\n\x07memvars\x18\x03 \x03(\x0b\x32\x1b.angr.protos.MemoryVariable\x12-\n\tstackvars\x18\x04 \x03(\x0b\x32\x1a.angr.protos.StackVariable\x12-\n\x08\x61\x63\x63\x65sses\x18\x05 \x03(\x0b\x32\x1b.angr.protos.VariableAccess\x12\x38\n\x10unified_tempvars\x18\x06 \x03(\x0b\x32\x1e.angr.protos.TemporaryVariable\x12\x36\n\x0funified_regvars\x18\x07 \x03(\x0b\x32\x1d.angr.protos.RegisterVariable\x12\x34\n\x0funified_memvars\x18\x08 \x03(\x0b\x32\x1b.angr.protos.MemoryVariable\x12\x35\n\x11unified_stackvars\x18\t \x03(\x0b\x32\x1a.angr.protos.StackVariable\x12-\n\x0bvar2unified\x18\n \x03(\x0b\x32\x18.angr.protos.Var2Unified\x12(\n\x05types\x18\x0b \x03(\x0b\x32\x19.angr.protos.VariableType\x12%\n\x07phi2var\x18\x0c \x03(\x0b\x32\x14.angr.protos.Phi2Varb\x06proto3')



_VARIABLEBASE = DESCRIPTOR.message_types_by_name['VariableBase']
_TEMPORARYVARIABLE = DESCRIPTOR.message_types_by_name['TemporaryVariable']
_REGISTERVARIABLE = DESCRIPTOR.message_types_by_name['RegisterVariable']
_MEMORYVARIABLE = DESCRIPTOR.message_types_by_name['MemoryVariable']
_STACKVARIABLE = DESCRIPTOR.message_types_by_name['StackVariable']
_VARIABLEACCESS = DESCRIPTOR.message_types_by_name['VariableAccess']
_VARIABLETYPE = DESCRIPTOR.message_types_by_name['VariableType']
_VAR2UNIFIED = DESCRIPTOR.message_types_by_name['Var2Unified']
_PHI2VAR = DESCRIPTOR.message_types_by_name['Phi2Var']
_VARIABLEMANAGERINTERNAL = DESCRIPTOR.message_types_by_name['VariableManagerInternal']
_VARIABLEACCESS_VARIABLEACCESSSORT = _VARIABLEACCESS.enum_types_by_name['VariableAccessSort']
VariableBase = _reflection.GeneratedProtocolMessageType('VariableBase', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLEBASE,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.VariableBase)
  })
_sym_db.RegisterMessage(VariableBase)

TemporaryVariable = _reflection.GeneratedProtocolMessageType('TemporaryVariable', (_message.Message,), {
  'DESCRIPTOR' : _TEMPORARYVARIABLE,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.TemporaryVariable)
  })
_sym_db.RegisterMessage(TemporaryVariable)

RegisterVariable = _reflection.GeneratedProtocolMessageType('RegisterVariable', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERVARIABLE,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.RegisterVariable)
  })
_sym_db.RegisterMessage(RegisterVariable)

MemoryVariable = _reflection.GeneratedProtocolMessageType('MemoryVariable', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYVARIABLE,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.MemoryVariable)
  })
_sym_db.RegisterMessage(MemoryVariable)

StackVariable = _reflection.GeneratedProtocolMessageType('StackVariable', (_message.Message,), {
  'DESCRIPTOR' : _STACKVARIABLE,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.StackVariable)
  })
_sym_db.RegisterMessage(StackVariable)

VariableAccess = _reflection.GeneratedProtocolMessageType('VariableAccess', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLEACCESS,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.VariableAccess)
  })
_sym_db.RegisterMessage(VariableAccess)

VariableType = _reflection.GeneratedProtocolMessageType('VariableType', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLETYPE,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.VariableType)
  })
_sym_db.RegisterMessage(VariableType)

Var2Unified = _reflection.GeneratedProtocolMessageType('Var2Unified', (_message.Message,), {
  'DESCRIPTOR' : _VAR2UNIFIED,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.Var2Unified)
  })
_sym_db.RegisterMessage(Var2Unified)

Phi2Var = _reflection.GeneratedProtocolMessageType('Phi2Var', (_message.Message,), {
  'DESCRIPTOR' : _PHI2VAR,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.Phi2Var)
  })
_sym_db.RegisterMessage(Phi2Var)

VariableManagerInternal = _reflection.GeneratedProtocolMessageType('VariableManagerInternal', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLEMANAGERINTERNAL,
  '__module__' : 'protos.variables_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.VariableManagerInternal)
  })
_sym_db.RegisterMessage(VariableManagerInternal)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VARIABLEBASE._serialized_start=40
  _VARIABLEBASE._serialized_end=184
  _TEMPORARYVARIABLE._serialized_start=186
  _TEMPORARYVARIABLE._serialized_end=262
  _REGISTERVARIABLE._serialized_start=264
  _REGISTERVARIABLE._serialized_end=350
  _MEMORYVARIABLE._serialized_start=352
  _MEMORYVARIABLE._serialized_end=437
  _STACKVARIABLE._serialized_start=439
  _STACKVARIABLE._serialized_end=556
  _VARIABLEACCESS._serialized_start=559
  _VARIABLEACCESS._serialized_end=843
  _VARIABLEACCESS_VARIABLEACCESSSORT._serialized_start=762
  _VARIABLEACCESS_VARIABLEACCESSSORT._serialized_end=818
  _VARIABLETYPE._serialized_start=845
  _VARIABLETYPE._serialized_end=892
  _VAR2UNIFIED._serialized_start=894
  _VAR2UNIFIED._serialized_end=953
  _PHI2VAR._serialized_start=955
  _PHI2VAR._serialized_end=1002
  _VARIABLEMANAGERINTERNAL._serialized_start=1005
  _VARIABLEMANAGERINTERNAL._serialized_end=1619
# @@protoc_insertion_point(module_scope)
