import ctypes
longsize = ctypes.sizeof(ctypes.c_long)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7]

# I set the y ob_item equals to the x ob_item
data_y = ctypes.c_long.from_address(id(y) + longsize * 3)
data_x = ctypes.c_long.from_address(id(x) + longsize * 3)
data_y_back = data_y.value
data_y.value = data_x.value

# now y is a view to the first 4 positions of the x list
y

# I can change it from x
x[0] = 7

# And view it on y
y

# I can change it from y
y[1] = -1

# And view it on x
x

# I restore the previews address before freeding
data_y = ctypes.c_long.from_address(id(y) + longsize * 3)
data_y.value = data_y_back
