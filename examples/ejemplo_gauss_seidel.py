import numpy as np


from rh16042uno.gauss_seidel import gauss_seidel

A = np.array([
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
], dtype=float)

b = np.array([1, -2, 0], dtype=float)

x = gauss_seidel(A, b)

print("Solución del sistema usando el Método de Gauss-Seidel:")
print(x)
