## Instalación RH16042UNO

Para instalar la biblioteca, simplemente ejecuta:

```bash
pip install RH16042UNO
```

```markdown
# RH16042UNO

**RH16042UNO** es una biblioteca para resolver sistemas de ecuaciones lineales y no lineales utilizando diferentes métodos numéricos.

### Métodos Implementados

--Eliminación de Gauss**
--Gauss-Jordan**
--Regla de Cramer**
--Descomposición LU**
--Método de Jacobi**
--Método de Gauss-Seidel**
--Método de Bisección**
```

Si deseas instalarla desde el código fuente:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/RH16042UNO.git
   ```

2. Navega a la carpeta del proyecto:
   ```bash
   cd RH16042UNO
   ```

3. Instala las dependencias:
   ```bash
   pip install .
   ```

## Uso

### Ejemplo 1: **Eliminación de Gauss**
Resuelve un sistema de ecuaciones lineales utilizando el método de eliminación de Gauss.

```python
import numpy as np
from rh16042uno.gauss_elimination import gauss_elimination

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
b = np.array([1, -2, 0], dtype=float)

x = gauss_elimination(A, b)
print("Solución del sistema usando Gauss:", x)
```

### Ejemplo 2: **Gauss-Jordan**
Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Jordan.

```python
import numpy as np
from rh16042uno.gauss_jordan import gauss_jordan

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
b = np.array([1, -2, 0], dtype=float)

x = gauss_jordan(A, b)
print("Solución del sistema usando Gauss-Jordan:", x)
```

### Ejemplo 3: **Regla de Cramer**
Resuelve un sistema de ecuaciones lineales utilizando la regla de Cramer.

```python
import numpy as np
from rh16042uno.crammer import crammer

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
b = np.array([1, -2, 0], dtype=float)

x = crammer(A, b)
print("Solución del sistema usando la Regla de Cramer:", x)
```

### Ejemplo 4: **Descomposición LU**
Resuelve un sistema de ecuaciones lineales utilizando la descomposición LU.

```python
import numpy as np
from rh16042uno.lu_decomposition import lu_decomposition

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
b = np.array([1, -2, 0], dtype=float)

x = lu_decomposition(A, b)
print("Solución del sistema usando Descomposición LU:", x)
```

### Ejemplo 5: **Método de Jacobi**
Resuelve un sistema de ecuaciones lineales utilizando el método iterativo de Jacobi.

```python
import numpy as np
from rh16042uno.jacobi import jacobi

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
b = np.array([1, -2, 0], dtype=float)

x = jacobi(A, b)
print("Solución del sistema usando el Método de Jacobi:", x)
```

### Ejemplo 6: **Método de Gauss-Seidel**
Resuelve un sistema de ecuaciones lineales utilizando el método iterativo de Gauss-Seidel.

```python
import numpy as np
from rh16042uno.gauss_seidel import gauss_seidel

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
b = np.array([1, -2, 0], dtype=float)

x = gauss_seidel(A, b)
print("Solución del sistema usando el Método de Gauss-Seidel:", x)
```

### Ejemplo 7: **Método de Bisección**
Resuelve una ecuación no lineal utilizando el método de bisección.

```python
import numpy as np
from rh16042uno.bisection import bisection

# Definimos una función no lineal
def func(x):
    return x**2 - 4  # Ecuación x^2 - 4 = 0

# Intervalo de búsqueda
a, b = 0, 3

# Llamamos al método de Bisección
root = bisection(func, a, b)
print("Raíz de la ecuación usando el Método de Bisección:", root)
```

## Contribuciones

Si deseas contribuir a la biblioteca, puedes hacer un *fork* del proyecto y enviar un *pull request* con tus mejoras.

## Licencia

Esta biblioteca está bajo la licencia **MIT**. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

¡Gracias por usar RH16042UNO! Esperamos que te sea útil en tus proyectos.
```
