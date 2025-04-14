"""
Módulo que implementa el método de Crammer (regla de Cramer) para resolver
sistemas de ecuaciones lineales.
"""
import numpy as np

def crammer(A, b):
    """
    Resuelve un sistema de ecuaciones lineales usando la regla de Cramer.
    
    Args:
        A (numpy.ndarray): Matriz de coeficientes.
        b (numpy.ndarray): Vector de términos independientes.
        
    Returns:
        numpy.ndarray: Vector solución del sistema.
        
    Examples:
        >>> import numpy as np
        >>> from rh16042uno import crammer
        >>> A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
        >>> b = np.array([1, -2, 0], dtype=float)
        >>> x = crammer(A, b)
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
    
    # Calcular el determinante de A
    det_A = np.linalg.det(A)
    
    # Verificar si el determinante es cero
    if abs(det_A) < 1e-10:
        raise ValueError("El sistema no tiene solución única (determinante es cero)")
    
    # Inicializar el vector solución
    x = np.zeros(n)
    
    # Resolver usando la regla de Cramer
    for i in range(n):
        # Crear una copia de A para reemplazar la columna i con b
        Ai = A.copy()
        Ai[:, i] = b
        
        # Calcular el determinante de la matriz modificada
        det_Ai = np.linalg.det(Ai)
        
        # Calcular el valor de x[i]
        x[i] = det_Ai / det_A
    
    return x