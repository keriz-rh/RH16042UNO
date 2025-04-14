"""
Módulo que implementa el método de descomposición LU para resolver
sistemas de ecuaciones lineales.
"""
import numpy as np

def lu_decomposition(A, b):
    """
    Resuelve un sistema de ecuaciones lineales usando descomposición LU.
    
    Args:
        A (numpy.ndarray): Matriz de coeficientes.
        b (numpy.ndarray): Vector de términos independientes.
        
    Returns:
        numpy.ndarray: Vector solución del sistema.
        
    Examples:
        >>> import numpy as np
        >>> from carnetuno import lu_decomposition
        >>> A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
        >>> b = np.array([1, -2, 0], dtype=float)
        >>> x = lu_decomposition(A, b)
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
    
    # Inicializar matrices L y U
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Descomposición LU
    for k in range(n):
        # Diagonal en L
        L[k, k] = 1.0
        
        # Elementos de U en la fila k
        for j in range(k, n):
            U[k, j] = A[k, j] - np.sum(L[k, :k] * U[:k, j])
        
        # Elementos de L en la columna k
        for i in range(k + 1, n):
            if abs(U[k, k]) < 1e-10:
                raise ValueError("La matriz no permite descomposición LU estándar")
            L[i, k] = (A[i, k] - np.sum(L[i, :k] * U[:k, k])) / U[k, k]
    
    # Resolver Ly = b mediante sustitución hacia adelante
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.sum(L[i, :i] * y[:i])
    
    # Resolver Ux = y mediante sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if abs(U[i, i]) < 1e-10:
            raise ValueError("El sistema no tiene solución única")
        x[i] = (y[i] - np.sum(U[i, i+1:] * x[i+1:])) / U[i, i]
    
    return x