# Taller Validacion Regresion y Clasificacion

import numpy as np, os
from sklearn import preprocessing


# PROCESAMIENTO DIGITAL

print('\n Procesamiento Digital \n')
print(' 1) Binarizar los datos \n'
      ' 2) Media y desviacion estandar (SIN ESCALAR) \n'
      ' 3) Media y desviacion estandar (DESPUES DE ESCALAR) \n'
      ' 4) Escalamiento Min Max \n'
      ' 5) Normalizacion de datos \n')
print('Opcion:')
option = int(input())

# Datos iniciales
input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])

print("\nDatos iniciales =\n", input_data)


if option == 1:
    data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
    print("\nDatos binarizados =\n", data_binarized)

elif option == 2:
    print("Media =", input_data.mean(axis=0))
    print("Desviación estándar =", input_data.std(axis=0))

elif option == 3:
    data_scaled = preprocessing.scale(input_data)
    print("Media =", data_scaled.mean(axis=0))
    print("Desviación estándar =", data_scaled.std(axis=0))

elif option == 4:
    data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
    data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
    print("\nMin max escalamiento de datos:\n", data_scaled_minmax)

elif option == 5:
    data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
    data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
    print("\nL1 dato normalizado:\n", data_normalized_l1)
    print("\nL2 dato normalizado:\n", data_normalized_l2)

else:
    print('Opcion Invalida')
    os.system('cls')

# ------------------------------------------------------------------

# Manejo de etiquetas

# Datos iniciales
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow',
                'white']

# Se crea un codificador de etiquetas y se ajustan las etiquetas
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# Se imprime el mapeo entre palabras y números
print("\nMapeo de etiquetas:")
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)

# Codificar un conjunto de etiquetas con el codificador
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print("Encoded values =", list(encoded_values))

# Decodificar un conjunto de valores usando el codificador
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))