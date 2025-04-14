import numpy as np

from rh16042uno.jacobi import jacobi

A = np.array([
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
], dtype=float)

b = np.array([1, -2, 0], dtype=float)

x = jacobi(A, b)

print("Solución del sistema usando el Método de Jacobi:")
print(x)
