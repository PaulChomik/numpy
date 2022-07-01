import numpy as np

'''
numpy tiene tipos de datos que se pueden almacenar en matrices
i=integer enteros
b=booleano
u-unsigned interger
f-float (variable con coma)
c-numeros imaginarios,variable compleja con coma flotante
m-timedelta (no se que es)
M-fecha de tiempo
O-objeto
S-alfanumerico
U-unicode alfanumerico (no se que es)
V-fixed chunk of memory for other type (void)
'''

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)


arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

'''
conversion de matrices:
podemos convertir una matriz con un tipo de datos
a otra matriz con otro tipo de datos
-una matriz alfanumerica no puede convertirse a alfanumerica
-una matriz de enteros puede convertirse en coma flotante

se recomienda crear un array nuevo cada vez que se
hace una conversion ,esto puede hacerse con astype()
la funcion astype() crea una copia del array y nos per-
mite indicar el tipo de dato

'''
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#ejemplo de como cambiar numeros racionales a enteros
arr = np.array([1.1, 2.1, 3.1])
print(arr)
newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)
#cambiar datos de enteros a booleanos
#se toman impares como 1=true
#pares como 0=False
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)
print(arr)
print(newarr)
print(newarr.dtype)
