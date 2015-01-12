import ctypes

longsize = ctypes.sizeof(ctypes.c_long)

##############################
# Example 2                  #
##############################

x = 1000

# Modify the ob_digit of x object
int_value = ctypes.c_uint.from_address(id(x) + longsize * 3)
int_value.value = 1001

# The x instance has been modified
x
# Another 1000 instance keep unmodified
1000

##############################
# Example 2                  #
##############################

x = 100
# Modify the ob_digit of x object
int_value = ctypes.c_uint.from_address(id(x) + longsize * 3)
int_value.value = 101

# All 100 instances has been modified
x
100
x + 2
98 + 2

# The id of x and another 100 instance is the same
id(x) == id(100)
