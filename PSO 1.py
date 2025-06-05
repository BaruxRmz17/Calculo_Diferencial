# -*- coding: utf-8 -*-

import numpy as np
from pyswarm import pso
import matplotlib.pyplot as plt

# ------------------------------
# Función de resistencia mecánica
# ------------------------------
def resistencia(x1, x2, x3):
    return (
        80 * np.exp(-((x1 - 30)**2) / 100) +
        40 * np.sin(np.pi * x2 / 120) +
        30 * np.cos(np.pi * x3 / 180)
    )

# ------------------------------
# Función objetivo para PSO (negada para maximizar)
# ------------------------------
def objetivo(x):
    x1, x2, x3 = x
    return -resistencia(x1, x2, x3)

# ------------------------------
# Rango de búsqueda para cada variable
# ------------------------------
lb = [0, 0, 100]       # Límites inferiores: x1, x2, x3
ub = [50, 120, 200]    # Límites superiores: x1, x2, x3

# ------------------------------
# Ejecución del PSO
# ------------------------------
best_pos, best_val = pso(objetivo, lb, ub, swarmsize=50, maxiter=100)

# Invertimos el valor porque lo minimizamos (negamos antes)
resistencia_max = -best_val

# ------------------------------
# Resultados
# ------------------------------
x1_opt, x2_opt, x3_opt = best_pos
print("\n--- Resultados Óptimos con PSO ---")
print(f"Mejor proporción de carga (x1): {x1_opt:.2f} %")
print(f"Mejor tiempo de curado (x2): {x2_opt:.2f} min")
print(f"Mejor temperatura (x3): {x3_opt:.2f} °C")
print(f"Resistencia máxima estimada: {resistencia_max:.2f} MPa")

# ------------------------------
# Visualización 2D en un plano x1-x2 con x3 fijo en el valor óptimo
# ------------------------------
x1_vals = np.linspace(0, 50, 50)
x2_vals = np.linspace(0, 120, 50)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = resistencia(X1, X2, x3_opt)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Z, cmap='viridis', edgecolor='none')
ax.scatter(x1_opt, x2_opt, resistencia_max, color='red', s=60, label='Óptimo PSO')
ax.set_title('Resistencia mecánica optimizada con PSO (x3 fijo en óptimo)')
ax.set_xlabel('Proporción de carga (%)')
ax.set_ylabel('Tiempo de curado (min)')
ax.set_zlabel('Resistencia estimada (MPa)')
ax.legend()
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
plt.show()
