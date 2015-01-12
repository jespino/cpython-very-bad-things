import ctypes
longsize = ctypes.sizeof(ctypes.c_long)

# I define a new int with __repr__  and __str__ alwais equals to 42
class EvilInt(int):
    def __repr__(self):
        return "42"
    def __str__(self):
        return "42"

# I change the tpye of the integers from -5 to 256"
for x in range(-5, 257):
  type_addr = ctypes.c_long.from_address(id(x) + longsize)
  type_addr.value = id(EvilInt)

# Now 5 + 5 is: 42
5 + 5
