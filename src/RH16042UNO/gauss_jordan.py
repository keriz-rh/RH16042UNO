"""
Módulo que implementa el método de Gauss-Jordan para resolver
sistemas de ecuaciones lineales.
"""
import numpy as np

def gauss_jordan(A, b):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan.
    
    Args:
        A (numpy.ndarray): Matriz de coeficientes.
        b (numpy.ndarray): Vector de términos independientes.
        
    Returns:
        numpy.ndarray: Vector solución del sistema.
        
    Examples:
        >>> import numpy as np
        >>> from rh16042uno import gauss_jordan
        >>> A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
        >>> b = np.array([1, -2, 0], dtype=float)
        >>> x = gauss_jordan(A, b)
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
    
    # Combinar A y b para la forma aumentada
    Ab = np.column_stack((A, b))
    
    # Proceso de eliminación Gauss-Jordan
    for i in range(n):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(Ab[i:, i])) + i
        if i != max_index:
            Ab[[i, max_index]] = Ab[[max_index, i]]
        
        # Verificar si hay un pivote igual a cero
        if abs(Ab[i, i]) < 1e-10:
            raise ValueError("El sistema no tiene solución única")
        
        # Normalizar la fila pivote
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Eliminación en las demás filas
        for j in range(n):
            if j != i:
                Ab[j] = Ab[j] - Ab[j, i] * Ab[i]
    
    # Extraer la solución
    x = Ab[:, n]
    
    return x