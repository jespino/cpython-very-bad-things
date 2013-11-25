from ctypes import *

x = 1000
print(x)
int_value = c_uint.from_address(id(x) + sizeof(c_long) * 3)
int_value.value = 1001
print(x)
