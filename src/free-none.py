import ctypes

ref_cnt = ctypes.c_long.from_address(id(None))
ref_cnt.value = 0
