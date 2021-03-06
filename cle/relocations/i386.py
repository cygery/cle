from . import generic

arch = 'X86'

R_386_32 = generic.GenericAbsoluteAddendReloc
R_386_COPY = generic.GenericCopyReloc
R_386_GLOB_DAT = generic.GenericJumpslotReloc
R_386_JMP_SLOT = generic.GenericJumpslotReloc
R_386_RELATIVE = generic.GenericRelativeReloc

R_386_TLS_DTPMOD32 = generic.GenericTLSModIdReloc
R_386_TLS_TPOFF = generic.GenericTLSOffsetReloc
R_386_TLS_DTPOFF32 = generic.GenericTLSDoffsetReloc
