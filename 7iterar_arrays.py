import numpy as np

'''
al iterar en un array hay que iterar enntre cada elemento
-si el array es 1D al iterar iteramos entre cada escalar
-si el array es 2D al iterar con "for x in array" iteraremos
en cada fila del array
-para un array 3d al iterar en una variable ,obtendremos un resultado
de iteracion entre matrices
-para iterar correctamente tenemos que iterar entre tantas dimensiones
como tenga el array
'''

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

#iterar entre filas
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)


#iterar entre elementos
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)

#iterar entre matrices de un array 3d
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
#iterar entre elementos
for x in arr:
    for y in x:
        for z in y:
            print(z)

'''
la iteracion entre elementos se puede hacer con
nditer ,esto tambien permite iterar entre elementos de
arrays con muchas dimensiones
'''

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

'''
el ejemplo de w3schools continua mas alla de esto
'''
