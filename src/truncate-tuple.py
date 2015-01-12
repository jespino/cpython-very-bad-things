import ctypes
longsize = ctypes.sizeof(ctypes.c_long)

x = (1, 2, 3)

# I change the ob_size of x to 2
tuple_size = ctypes.c_long.from_address(id(x) + longsize * 2)
tuple_size.value = 2

# Now x is the truncated tuple (1, 2) + a memory leak!
x
