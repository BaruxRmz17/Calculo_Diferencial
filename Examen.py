# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:23:58 2025

@author: usuario
"""

import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')
y = sp.symbols('y')




# Ejemplo 1: Derivada de un polinomio
f1 = 2*x / sp.sin(3*x)
derivada_f1 = sp.diff(f1, x)

f2 = sp.sin(9*x) / sp.sin(7*x)
derivada_f2 = sp.diff(f2, x)

f3 = 3*x / sp.sin(5*x)
derivada_f3 = sp.diff(f3, x)

f4 = x**2 / sp.sin(3*x)**2
derivada_f4 = sp.diff(f4, x)





# Mostrar los resultados
print("Derivada de f1: ", derivada_f1)
print("Derivada de f2: ", derivada_f2)
print("Derivada de f3: ", derivada_f3)
print("Derivada de f4: ", derivada_f4)





