import pyximport; pyximport.install()
from utils import say_hello_to, to_int32

say_hello_to("Tom")

str_value = 'A009ABCD'
print(int(str_value, 16))
print(to_int32(int(str_value, 16)))