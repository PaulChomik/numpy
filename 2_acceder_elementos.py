import numpy as np
'''
los array de numpy estan indexados del 0 al (ultimo-1)
es decir
array [1 , 2 , 3 , 4 , 5 , 6 ]
orden [0ª, 1ª, 2ª, 3ª, 4ª, 5ª]
de econsultar el elemento ârrar[0]=sale 1
se puede consultar de atraz para adelante usando indices negativos
array [1 , 2 , 3 , 4 , 5 , 6 ]
orden [-6ª,-5ª,-4ª,-3ª,-2ª,-1ª]
esto es util sobretodo para cobsultar el ultimo y anteultimo
elemento del vector
'''

#array 1D
ar1=np.array([1,2,3,4])
print(ar1[1])
print('ultimo:'+str(ar1[-1]))

#array 2D
arDos=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('1er fila,2da columna: '+str(arDos[0, 1]))

#array 3D
ar3=np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(ar3[0,1,2])

print("none")


'''
imprime 6 porque la matriz 3D son 2 matrices una traz de otra

matriz1=|1 2 3|    matriz2=|7 8  9 |
        |4 5 6|            |9 10 11|
al poner nlos numeros [0,1,2] elegimos [matriz,fila,columna]
'''
