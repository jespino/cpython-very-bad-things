from ctypes import *

class LifeInt(int):
    def __str__(self):
        return "42"

for x in range(-5, 258):
    type_addr = c_long.from_address(id(x) + sizeof(c_long))
    type_addr.value = id(LifeInt)

print(5 + 5) # 42
