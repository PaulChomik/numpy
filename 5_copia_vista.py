import numpy as np

'''
una "vista" es una copia de como estaba un array en un momento
dado.
Una copia es un nuevo arrray

'''
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

y = arr.view()
arr[0] = 42

print(arr)
print(y)

#como hacer cambios en la view

y[0] = 31

print(arr)
print(y)

'''
una view no guarda su propio dato, solamente es uan "vista"
de un array que es el que contiene realmente su data.
Podemos consultar donde esta la data de esa vista
'''
print("datos de donde sale la vista.")
print(y.base)
