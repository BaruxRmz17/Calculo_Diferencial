import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definimos la variable simbólica
x = sp.symbols('x')

# Definimos la función f(x) = (x^3 - 1) / (x - 1)
# ERROR: En el comentario original, escribiste "x^ - 1" en lugar de "x^3 - 1".
f = (3*x**2 - 17*x + 20) / (4*x**2 - 25*x + 36)

# Simplificar la función
f_simplificada = sp.simplify(f)

# Calculamos el límite de f(x) cuando x tiende a 4
limite = sp.limit(f, x, 4)

# Mostramos el límite y la simplificación de la función
# ERROR: "Limmite" está mal escrito, debe ser "Límite".
print(f"Funcion simplificada: {f_simplificada}")
print(f"Límite de f(x) cuando x tiende a 4: {limite}")

# Graficar la función f(x) y su simplificación
# Definir la función para la gráfica (usaremos la simplificación)
def func(x):
    return(3*x**2 - 17*x + 20) / (4*x**2 - 25*x + 36)  # ERROR: Si en el futuro se usa la función original, no hay control sobre x=1.

# Definir un rango de valores para x
x_vals = np.linspace(-5, 5, 400)
x_vals = x_vals[x_vals != 4]  # Evita la descontinuidad
y_vals = func(x_vals)

# Graficamos la función
plt.plot(x_vals, y_vals, label=r'$f(x) = \frac{3x^2 - 17x + 20}{4x^2 - 25x + 36}$simplificada')


# ERROR: "linestyle = '*******'" no es un estilo válido en Matplotlib. 
# Se debe usar '--', '-', '-.', ':' u otros estilos soportados.
plt.axvline(x=4, color='r', linestyle='-', label=r'$x = 4$')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Gráfica de la función f(x) = (3x^2 - 17x + 20)/(4x^2 - 25x + 36)")
plt.legend()
plt.grid(True)
plt.show()
