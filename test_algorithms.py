import numpy as np
#
# # Definir la matriz X
# X = np.array([[-427.29, 190.68, -669.12],
#               [720.89, -122.13, -174.9],
#               [872.22, -944.6, -658.31],
#               [-569.98, -766.85, -568.39],
#               [693.3, -969.54, 100.84]])
#
# # Definir el vector de pesos W
# W = np.array([[5], [7], [3]])
# print(X)
# print(W)
# # Calcular U
# U = np.dot(X, W)
#
# print(U)

# Ejemplo con un vector
vector = np.array([1, 4, 7])
norm_vector = np.linalg.norm(vector)

print("Norma del vector:", norm_vector)

# Ejemplo con una matriz
matriz = np.array([[1],
                   [4],
                   [7]])
norm_matriz = np.linalg.norm(matriz)

print("Norma de la matriz:", norm_matriz)