from ctypes import *

x = 100
print(x)
int_value = c_uint.from_address(id(x) + sizeof(c_long) * 3)
int_value.value = 101
print(x)
print(100)
