import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función f(x)
f = (3*x**2 - 17*x + 20) / (4*x**2 - 25*x + 36)

# Simplificar la función
f_simplificada = sp.simplify(f)

# Calcular el límite de f(x) cuando x tiende a 4
limite = sp.limit(f, x, 4)

# Mostrar la simplificación y el límite
print(f"Función simplificada: {f_simplificada}")
print(f"Límite de f(x) cuando x tiende a 4: {limite}")

# Graficar la función
x_vals = np.linspace(0, 8, 400)  # Evitar el punto x=4 si hay una discontinuidad
y_vals = [f.subs(x, val) if val != 4 else None for val in x_vals]  # Evitar división por cero

plt.plot(x_vals, y_vals, label=r'$f(x)$', color='b')
plt.axvline(x=4, color='r', linestyle='--', label=r'$x = 4$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función f(x)')
plt.legend()
plt.grid(True)
plt.show()
