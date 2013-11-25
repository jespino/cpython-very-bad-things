from ctypes import *

ref_cnt = c_long.from_address(id(None))
ref_cnt.value = 0
