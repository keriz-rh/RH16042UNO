"""
Módulo que implementa el método de eliminación de Gauss para resolver 
sistemas de ecuaciones lineales.
"""
import numpy as np

def gauss_elimination(A, b):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de eliminación de Gauss.
    
    Args:
        A (numpy.ndarray): Matriz de coeficientes.
        b (numpy.ndarray): Vector de términos independientes.
        
    Returns:
        numpy.ndarray: Vector solución del sistema.
        
    Examples:
        >>> import numpy as np
        >>> from rh16042uno import gauss_elimination
        >>> A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
        >>> b = np.array([1, -2, 0], dtype=float)
        >>> x = gauss_elimination(A, b)
        >>> print(x)
        [1. 1. 2.]
    """
    # Crear una copia para no modificar los originales
    A = np.copy(A).astype(float)
    b = np.copy(b).astype(float)
    n = len(b)
    
    # Verificar que A sea una matriz cuadrada
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matriz A debe ser cuadrada")
    
    # Verificar que b tenga la dimensión correcta
    if A.shape[0] != len(b):
        raise ValueError("La dimensión de b debe coincidir con las filas de A")
    
    # Eliminación hacia adelante
    for i in range(n):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(A[i:, i])) + i
        if i != max_index:
            A[[i, max_index]] = A[[max_index, i]]
            b[[i, max_index]] = b[[max_index, i]]
        
        # Verificar si hay un pivote igual a cero
        if abs(A[i, i]) < 1e-10:
            raise ValueError("El sistema no tiene solución única")
        
        # Eliminación
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]
    
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
    
    return x