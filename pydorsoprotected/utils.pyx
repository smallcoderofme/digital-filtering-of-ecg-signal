# cython: language_level=3

def say_hello_to(name):
	print("Hello %s!" % name)

def to_int32(value):
	cdef int local_min=-2147483648
	cdef int local_max=2147483647
	if value >= local_max:
		return value - local_max + local_min
	else:
		return value