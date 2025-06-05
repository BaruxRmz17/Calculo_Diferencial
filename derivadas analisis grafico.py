# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 15:01:00 2025

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función y su derivada
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Crear un rango de valores para x
x = np.linspace(-5, 5, 400)
y = f(x)
dy = df(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Gráfico de la función f(x) = x^2
plt.plot(x, y, label='$f(x) = x^2$', color='b')

# Gráfico de la derivada f'(x) = 2x
plt.plot(x, dy, label="$f'(x) = 2x$", color='r', linestyle='--')

# Etiquetas y leyenda
plt.title("Gráfico de la función y su derivada")
plt.xlabel("x")
plt.ylabel("y / f'(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
