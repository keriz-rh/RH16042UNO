"""
RH16042UNO - Biblioteca para resolver sistemas de ecuaciones lineales y no lineales.

Esta biblioteca implementa los siguientes métodos numéricos:
- Eliminación de Gauss
- Gauss-Jordan
- Crammer
- Descomposición LU
- Jacobi
- Gauss-Seidel
- Bisección
"""

from .gauss_elimination import gauss_elimination
from .gauss_jordan import gauss_jordan
from .crammer import crammer
from .lu_decomposition import lu_decomposition
from .jacobi import jacobi
from .gauss_seidel import gauss_seidel
from .bisection import bisection

__version__ = '0.1.0'