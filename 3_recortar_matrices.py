import numpy as np
'''
si tenemos una matriz linea, podemos cortar la misma indicando
a=B[inicio:fin] o tambien a=B[inicio,fin,paso]
inicio por defecto=0
fin por defecto=ultimo elemento de la matriz
    el elemento final no esta incluido en la matriz recortada
    ej: si cortamos [1:4] incluye los elementos 1,2 y 3
paso por defecto=1

'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print("corte de la matriz")
print(arr[1:5])

print("corte desde el 4to elmento al final")
print(arr[4:])

print("corte desdeel inicio hasta el 4to elmento")
print(arr[:4])

'''
utilizando indices negativos podemos invertir la matriz
y hacer cortes de atraz para adelante
'''
print("corte de atras para adelante desd eel ante pen ultimo lugar(-3) al ante-ultimo(-1)")
print(arr[-3:-1])

print("corte salteado cada 2 elementos")
print(arr[1:5:2])

print("corte completo salteado cada 2 elementos")
print(arr[::2])

'''
cortes en array 2D:
como los array 2d tienen varias dimensiones el proceso de docrte es similar pero
agregando una coma para cada dimension
'''
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("matriz bidimensional")
print(arr)
print("recorte")
print(arr[1, 1:4])
