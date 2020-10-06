# Machine Learning 02

import numpy as np

# TECNICAS DE APILAMIENTO

print('Tecnicas De Apilamiento \n')
print(' 1) Horizontal \n 2) Vertical \n 3) En Profundidad \n 4) Por Columnas \n 5) Por Filas \n')
print('Opcion:')
option = int(input())

# Matrices Inciales

a = np.arange(9).reshape(3,3)
b = a*3

print('a =\n', a, '\n')
print('b =\n', b, '\n')

if option == 1:
    print('Apilamiento horizontal =\n', np.hstack((a, b)))
elif option == 2:
    print('Apilamiento vertical =\n', np.vstack((a, b)))
elif option == 3:
    print('Apilamiento en profundidad =\n', np.dstack((a, b)))
elif option == 4:
    print('Apilamiento por columnas =\n', np.column_stack((a, b)))
elif option == 5:
    print('Apilamiento por filas =\n', np.row_stack((a, b)))
else:
    print('Opcion Invalida')

#------------------------------------------------------------------

# DIVISION DE ARRAYS

print('Division De Arrays \n')
print(' 1) Horizontal \n 2) Vertical \n 3) En Profundidad \n')
print('Opcion:')
option = int(input())

# Matrices Inciales

c = np.arange(9).reshape(3,3)
d = np.arange(27).reshape(3, 3, 3)

if option == 1:
    print(c, '\n')
    print('División horizontal =\n', np.hsplit(c, 3), '\n')
elif option == 2:
    print(c, '\n')
    print('División vertical =\n', np.vsplit(c, 3), '\n')
elif option == 3:
    print(d, '\n')
    print('División en profundidad =\n', np.dsplit(d, 3), '\n')
else:
    print('Opcion Invalida')

#------------------------------------------------------------------

# PROPIEDADES DE LOS ARRAYS

print(b, '\n')

print('\nnumero de dimenciones: ', b.ndim)

print('numero de elementos: ', b.size)

print('numero de bytes por elemento: ', b.itemsize)

print('numero total de bytes: ', b.nbytes, '\n')


b.resize(6, 4)
print(b, '\n')
print('Transpuesta: ', b.T)


b = np.array([1.j + 1, 2.j + 3])

print('parte complejo: \n', b)

print('parte real: ', b.real, '\n')

print('parte imaginario: ', b.imag)