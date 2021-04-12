from ctypes import *
cdll.msvcrt("./PythonLaba1_5/PythonLaba1_5/test.so")



a = 2
resultat = a + 2
print(resultat)

test=ctypes.CDLL('./PythonLaba1_5/PythonLaba1_5/test.so')

test.primer_int.restype=ctypes.c_int
test.primer_int.argtypes = [ctypes.c_int]
print("решение ", test.primer_int)

asd