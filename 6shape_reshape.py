import numpy as np

'''
el metodo shape nos dice cuantos elementos tiene
un array en cada dimension
ej [1,2,3,4].shape da (4)
   |1,2,3|
   |4,5.6| .shape da(3,3)
'''
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


'''
se puede agarrar un array de 1D(linea) y convertirlo en
un array 2D(rectangular)

'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

'''
los reshape pueden incluso disminuir el numero de elementos
de un array
ej:array de 12elementos a 3x3,perdiendo 3 elementos
y reordenando el resto.
podemos mirar si el array es resultado de una copia
o es un original con View
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)


'''
si tenemos una rray que tiene "n" elementos y queremos
convertirlo en una matriz de 2x2x? y no sabemos el 3 valor
en la tercera dimension, podemos poner -1 y numpy resolverà
esta incognita
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
