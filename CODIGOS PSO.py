# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Función simulada de resistencia mecánica
def resistencia(x1, x2, x3):
    return (
        80 * np.exp(-((x1 - 30)**2) / 100) +
        40 * np.sin(np.pi * x2 / 120) +
        30 * np.cos(np.pi * x3 / 180)
    )

# Rango de variables
x1_vals = np.linspace(0, 50, 50)       # Proporción de carga (%)
x2_vals = np.linspace(0, 120, 50)      # Tiempo de curado (min)
x3_fixed = 160                         # Temperatura fija en °C

# Malla de evaluación
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = resistencia(X1, X2, x3_fixed)

# Encontrar máximo
max_idx = np.unravel_index(np.argmax(Z), Z.shape)
x1_max = X1[max_idx]
x2_max = X2[max_idx]
res_max = Z[max_idx]

# Gráfica 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Z, cmap='viridis', edgecolor='none')
ax.scatter(x1_max, x2_max, res_max, color='red', s=50, label='Máximo encontrado')
ax.set_title('Resistencia en función de carga y tiempo de curado (Temp. fija)')
ax.set_xlabel('Proporción de carga (%)')
ax.set_ylabel('Tiempo de curado (min)')
ax.set_zlabel('Resistencia estimada')
ax.legend()
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
plt.show()

# Resultado óptimo
print(f"Mejor proporción de carga: {x1_max:.2f}%")
print(f"Mejor tiempo de curado: {x2_max:.2f} minutos")
print(f"Temperatura fija: {x3_fixed} °C")
print(f"Resistencia máxima estimada: {res_max:.2f} MPa")
