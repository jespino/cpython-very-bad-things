import ctypes

MYFUNCTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)

@MYFUNCTYPE
def my_add(x, y):
    return 42

my_add_address = ctypes.c_long.from_address(id(my_add) + 8 * 10)

int_address = id(int)
as_number_address = ctypes.c_long.from_address(int_address + 8 * 12)
add_address = ctypes.c_long.from_address(as_number_address.value)
add_address.value = my_add_address.value

refcnt = ctypes.c_long.from_address(id(42))
refcnt.value = refcnt.value + 1

x = 2
print(x + x)
