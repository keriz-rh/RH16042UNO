import numpy as np

from rh16042uno.bisection import bisection

# Definimos una función no lineal
def func(x):
    return x**2 - 4  # Ecuación x^2 - 4 = 0

# Intervalo de búsqueda
a, b = 0, 3

# Llamamos al método de Bisección
root = bisection(func, a, b)

print("Raíz de la ecuación usando el Método de Bisección:")
print(root)
