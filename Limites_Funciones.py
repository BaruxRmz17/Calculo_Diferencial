import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definimos la variable simbólica
x = sp.symbols('x')

# Definimos la función f(x) = (x^3 - 1) / (x - 1)
# ERROR: En el comentario original, escribiste "x^ - 1" en lugar de "x^3 - 1".
f = (x**3 - 1) / (x - 1)

# Simplificar la función
f_simplificada = sp.simplify(f)

# Calculamos el límite de f(x) cuando x tiende a 1
limite = sp.limit(f, x, 1)

# Mostramos el límite y la simplificación de la función
# ERROR: "Limmite" está mal escrito, debe ser "Límite".
print(f"Funcion simplificada: {f_simplificada}")
print(f"Limmite de (x) cuando x tiende a 1: {limite} " )  # ERROR TIPOGRÁFICO

# Graficar la función f(x) y su simplificación
# Definir la función para la gráfica (usaremos la simplificación)
def func(x):
    return (x**2 + x + 1)  # ERROR: Si en el futuro se usa la función original, no hay control sobre x=1.

# Definir un rango de valores para x
x_vals = np.linspace(-2, 2, 400)
y_vals = func(x_vals)

# Graficamos la función
plt.plot(x_vals, y_vals, label=r'$f(x) = \frac{x^3 - 1}{x - 1}$(simplificada)')

# ERROR: "linestyle = '*******'" no es un estilo válido en Matplotlib. 
# Se debe usar '--', '-', '-.', ':' u otros estilos soportados.
plt.axvline(x=1, color='r', linestyle='-', label=r'$x = 1$')  # ERROR

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Gráfica de la función f(x) = (x^3 - 1) / (x - 1)")
plt.legend()
plt.grid(True)
plt.show()
