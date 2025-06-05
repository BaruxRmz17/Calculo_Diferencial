import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Definimos las variables simbolicas 
x,y = sp.symbols('x,y')

#Definir la funcion original
f = x**3 + 2

#Calculamos la inversa de la funcion 
f_inv = sp.solve(f - y,x)

#Mostrar la funcion original y su inveraa
print(f"Funcion original: f(x) = {f}")
print(f"Funcion inversa: f_inv(y) = {f_inv}")

#Para graficar, convertimos las funciones en expresiones numericas
f_lambdified = sp.lambdify(x,f, 'numpy')
f_inv_lambdified = sp.lambdify(y, f_inv[0], 'numpy')

#Rango de valores a graficar.
x_vals = np.linspace(-3,3,20)
y_vals = f_lambdified(x_vals)
y_inv_vals = f_inv_lambdified(x_vals)

#Imprimir los valores de la funcion original y su inversa para 20 puntos
print("\nValores de f(x) para 20 puntos: ")
for i in range(20):
    print(f"x = {x_vals[i]:.2f} , f(x) = {y_vals[i]:.2f}, f_inv(y) = {y_inv_vals[i]:.2f}")

#Creamos las graficas
plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, label="f(x) = x**2 + 2x + 1", color = 'blue')
plt.plot(y_vals, x_vals, label="f_inv(y) ", color = 'red', linestyle = 'dashed')

#configuracion de la grafica
plt.title("Funciones y su inversa")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth = 0.8)
plt.axvline(0, color='black', linewidth = 0.8)
plt.grid(True)
plt.legend()

#Se muestre la grafica
plt.show()

