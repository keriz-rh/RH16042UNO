import numpy as np

from rh16042uno.lu_decomposition import lu_decomposition

A = np.array([
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
], dtype=float)

b = np.array([1, -2, 0], dtype=float)

x = lu_decomposition(A, b)

print("Solución del sistema usando Descomposición LU:")
print(x)
