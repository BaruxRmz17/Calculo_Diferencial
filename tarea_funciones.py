#Tarea 2: Graficar una funcion
"""
La funcion que graficaremos en el codigo es la siguinte
6x^3 + 4x^2 + 5 +12
La cual tendra un rango de -10 a 10 y se haran 100 calculos
"""

# Importamos las librerías necesarias
import numpy as np  
import matplotlib.pyplot as plt  

# Definimos la función f(x), que representa una ecuación cubica
def f(x):
    return x**3 - 3*x**2 - 4*x + 12 

# Generamos un conjunto de valores para x en el rango de -2 a 2
x = np.linspace(-10, 10, 100)

# Calculamos los valores de f(x) evaluando la función en cada valor de x
y = f(x)


# Imprimimos los valores de x y f(x) para ver los resultados numéricos
print("Valores de x y f(x): ")
for i in range(len(x)): 
    print(f"x = {x[i]:.2f}, f(x) = {y[i]:.2f}")  

# Graficamos la función
plt.plot(x, y, label="f(x) =6x^3 + 4x^2 + 5 +12 ")  

# Configuramos la gráfica
plt.title("Gráfica de f(x) =6x^3 + 4x^2 + 5 +12")  
plt.xlabel("x")  
plt.ylabel("f(x)")  

# Añadimos líneas en los ejes X y Y para referencia
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1)  

# Mostramos la cuadrícula para facilitar la lectura de valores
plt.grid(True)

# Mostramos la leyenda de la función
plt.legend()

# Finalmente, mostramos la gráfica
plt.show()