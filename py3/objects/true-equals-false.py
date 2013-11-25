from ctypes import *

val = c_int.from_address(id(True) + sizeof(c_long) * 2)
val.value = 0
val = c_int.from_address(id(True) + sizeof(c_long) * 3)
val.value = 0
assert(True == False)
print(True == False)
