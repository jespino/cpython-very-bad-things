from ctypes import *

def repr(x):
    return "42"

CMPFUNC = CFUNCTYPE(c_void_p, c_void_p)

repr_func = CMPFUNC(repr)

tp_repr = c_long.from_address(id(int) + sizeof(c_long) * 11)
tp_repr.value = id(repr_func)

print(repr(5 + 5)) # 42
