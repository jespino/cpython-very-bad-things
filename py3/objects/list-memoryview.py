from ctypes import *

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7]
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(y) # [10, 9, 8, 7]
datos_y = c_long.from_address(id(y) + sizeof(c_long) * 3)
datos_x = c_long.from_address(id(x) + sizeof(c_long) * 3)
old_value = datos_y.value # To restore later
datos_y.value = datos_x.value
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(y) # [1, 2, 3, 4]
x[0] = 7
print(x) # [7, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(y) # [1, 2, 3, 4]
datos_y.value = old_value # This prevent deallocation problem
