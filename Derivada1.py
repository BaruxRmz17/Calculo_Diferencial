# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:23:58 2025

@author: usuario
"""

import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Ejemplo 1: Derivada de un polinomio
f1 = 3*x**4 - 5*x**3 + 2*x**2 - x + 1
derivada_f1 = sp.diff(f1, x)

# Ejemplo 2: Derivada de una función racional
f2 = (x**2 + 3*x) / (x**2 - 2*x + 1)
derivada_f2 = sp.diff(f2, x)

# Ejemplo 3: Derivada de una función trigonométrica
f3 = sp.sin(x**2)
derivada_f3 = sp.diff(f3, x)

# Mostrar los resultados
print("Derivada de f1: ", derivada_f1)
print("Derivada de f2: ", derivada_f2)
print("Derivada de f3: ", derivada_f3)
