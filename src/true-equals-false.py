import ctypes
longsize = ctypes.sizeof(ctypes.c_long)

# I set the ob_size to 0
val = ctypes.c_int.from_address(id(True) + longsize * 2)
val.value = 0

# I set the ob_digit to 0
val = ctypes.c_int.from_address(id(True) + longsize * 3)
val.value = 0

# Now True == False?
True == False
