from ctypes import *

x = (1, 2, 3)
print(x) # (1, 2, 3)
tuple_size = c_long.from_address(id(x) + sizeof(c_long) * 2)
tuple_size.value = 2
print(x) # (1, 2)
