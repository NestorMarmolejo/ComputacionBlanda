# Machine Learning 01

import numpy as np

# Creando un arreglo

print('Digite numero de elementos:')
n = int(input())
a = np.arange(n)

print('Arreglo a =', a, '\n')
print('Tipo de a =', a.dtype, '\n')
print('Dimensión de a =', a.ndim, '\n')
print('Número de elementos de a =', a.shape)

# Creando un arreglo multidimensional

print('\nDigite numero de elementos para areglo 1:')
f = int(input())
print('Digite numero de elementos para arreglo 2:')
c = int(input())
m = np.array([np.arange(f), np.arange(c)])
print(m);

# Utilización de arreglos multidimensionales

print('Digite numero de elementos:')
n = int(input())
print('Digite numero de bloques:')
b = int(input())
print('Digite numero de filas:')
f = int(input())
print('Digite numero de columnas:')
c = int(input())

z = np.arange(n).reshape(b,f,c)
print('z =\n', z)

print('Buscar un elemento en especifico\n')
print('Bloque:')
b = int(input())
print('Fila:')
f = int(input())
print('Columna:')
c = int(input())
print('\n z[b, f, c] =', z[b, f, c])
