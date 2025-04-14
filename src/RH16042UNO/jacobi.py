"""
Módulo que implementa el método iterativo de Jacobi para resolver
sistemas de ecuaciones lineales.
"""
import numpy as np

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Resuelve un sistema de ecuaciones lineales usando el método iterativo de Jacobi.
    
    Args:
        A (numpy.ndarray): Matriz de coeficientes.
        b (numpy.ndarray): Vector de términos independientes.
        x0 (numpy.ndarray, optional): Vector inicial. Por defecto es un vector de ceros.
        tol (float, optional): Tolerancia para el criterio de convergencia. Por defecto es 1e-6.
        max_iter (int, optional): Número máximo de iteraciones. Por defecto es 100.
        
    Returns:
        numpy.ndarray: Vector solución del sistema.
        int: Número de iteraciones realizadas.
        
    Examples:
        >>> import numpy as np
        >>> from carnetuno import jacobi
        >>> A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]], dtype=float)
        >>> b = np.array([6, 25, -11], dtype=float)
        >>> x, iterations = jacobi(A, b)
        >>> print(x)
        [1. 2. -1.]
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
    
    # Inicializar vector solución
    if x0 is None:
        x0 = np.zeros(n)
    x = np.copy(x0)
    
    # Verificar que la matriz sea diagonalmente dominante
    for i in range(n):
        if abs(A[i, i]) <= np.sum(np.abs(A[i, :])) - abs(A[i, i]):
            print("Advertencia: La matriz no es diagonalmente dominante, puede no converger")
            break
    
    # Iterar hasta convergencia o máximo de iteraciones
    for iterations in range(max_iter):
        x_new = np.zeros(n)
        
        # Calcular el nuevo x usando el método de Jacobi
        for i in range(n):
            if abs(A[i, i]) < 1e-10:
                raise ValueError(f"El elemento diagonal A[{i},{i}] es cercano a cero")
            
            s = np.sum(A[i, :] * x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]
        
        # Verificar la convergencia
        if np.linalg.norm(x_new - x) < tol:
            return x_new, iterations + 1
        
        x = x_new.copy()
    
    print(f"Advertencia: El método alcanzó el máximo de iteraciones ({max_iter}) sin converger")
    return x, max_iter