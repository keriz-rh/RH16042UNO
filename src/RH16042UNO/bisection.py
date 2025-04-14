"""
Módulo que implementa el método de bisección para encontrar raíces de ecuaciones no lineales.
"""
import numpy as np

def bisection(func, a, b, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de una función dentro de un intervalo usando el método de bisección.
    
    Args:
        func (callable): La función para la cual se busca la raíz.
        a (float): Extremo izquierdo del intervalo inicial.
        b (float): Extremo derecho del intervalo inicial.
        tol (float, optional): Tolerancia para el criterio de convergencia. Por defecto es 1e-6.
        max_iter (int, optional): Número máximo de iteraciones. Por defecto es 100.
        
    Returns:
        float: Aproximación de la raíz.
        int: Número de iteraciones realizadas.
        
    Examples:
        >>> from rh16042uno import bisection
        >>> # Definir una función
        >>> def f(x):
        ...     return x**3 - x - 2
        >>> # Encontrar una raíz en el intervalo [1, 2]
        >>> root, iterations = bisection(f, 1, 2)
        >>> print(f"Raíz: {root}, Iteraciones: {iterations}")
        Raíz: 1.5213927373736647, Iteraciones: 23
    """
    # Verificar que los extremos del intervalo tienen signos opuestos
    fa = func(a)
    fb = func(b)
    
    if fa * fb > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo")
    
    # Inicializar variables
    c = a
    fc = fa
    iterations = 0
    
    # Iterar hasta convergencia o máximo de iteraciones
    while (b - a) > tol and iterations < max_iter:
        # Actualizar punto medio
        c = (a + b) / 2
        fc = func(c)
        
        # Actualizar intervalo
        if fc == 0:
            break  # Encontrado la raíz exacta
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iterations += 1
    
    if iterations == max_iter:
        print(f"Advertencia: El método alcanzó el máximo de iteraciones ({max_iter}) sin converger")
    
    return c, iterations