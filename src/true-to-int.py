import ctypes
longsize = ctypes.sizeof(ctypes.c_long)

# True is True (the representation of True bool object)
True

# I set the ob_type of True to int type
ctypes.c_long.from_address(id(True) + longsize)
type_addr = ctypes.c_long.from_address(id(True) + longsize)
type_addr.value = id(int)

# True is now 1 (the representation of 1 int object)
True
