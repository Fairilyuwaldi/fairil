# a =, 10, a adalah dengan nilai 10

# tipe data: Angka satuan yang gak ada
 # koma nya (integer)
data_integer = 1
print("data : ", type (data_integer))
print("- bertipe : ", type (data_integer))

# tipe data: angka dengan koma (float
data_float = 1,5
print("data : ", data_float)
print("- bertipe : ", type (data_float))

# tipe data: kumpulan karakter (string)
data_string = "fairil"
print("data : ", data_float)
print("- bertipe : ", type (data_float))

# tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_float)
print("- bertipe : ", type (data_float))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type (data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10,5)
print("data : ", data_c_double)
print("-bertipe ", type(data_c_double))