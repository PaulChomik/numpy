'''
con numpy se pueden crear arrays simplemente escribiendo
''' 
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

#tambien se pueden crear arrays a travex de listas
ar1=np.array((1,2,3,4,5))
print(ar1)

#el tipo de dato de este arr es ndarry
print(type(arr))

'''
se pueden crear arrays de diferentes dimensiones
0:corresponden a escalares,array con un solo elemento [0]
1:vectoreslinea o fila [1,2,3,4]
2:matrices bidimensionales |1 2 3|
                           |4 5 6|
                           |7 8 9|
3:son cajas, son matrices bidimensionales una atraz de la otra
"n":podemos crear matrices de la cantidad de dimensiones que queramos
'''
#array de 0 dimensiones o 1 solo elemento escalar
arr0=np.array(33)
print(arr0)
print('numero de dimensiones:'+str(arr0.ndim))

#array de 1 dimension o vector linea
arr1=np.array([1,2,3,4,6,7])
print(arr1)
print('numero de dimensiones:'+str(arr1.ndim))

#array de 2 dimensiones o matriz plana
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print('numero de dimensiones:'+str(arr2.ndim))


#array 3D, se crea conteniendo varios array 2D
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)
print('numero de dimensiones:'+str(arr3.ndim))
