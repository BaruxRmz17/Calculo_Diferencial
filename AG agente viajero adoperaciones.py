# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:39:53 2024

@author: usuario
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
ciudades = ['A', 'B', 'C', 'D', 'E']
coordenadas = {
    'A': (0, 0),
    'B': (3, 5),
    'C': (6, 1),
    'D': (2, 7),
    'E': (8, 8),
}

distancias = {
    ('A', 'B'): 300, ('A', 'C'): 400, ('A', 'D'): 250, ('A', 'E'): 500,
    ('B', 'A'): 300, ('B', 'C'): 150, ('B', 'D'): 200, ('B', 'E'): 600,
    ('C', 'A'): 400, ('C', 'B'): 150, ('C', 'D'): 350, ('C', 'E'): 450,
    ('D', 'A'): 250, ('D', 'B'): 200, ('D', 'C'): 350, ('D', 'E'): 700,
    ('E', 'A'): 500, ('E', 'B'): 600, ('E', 'C'): 450, ('E', 'D'): 700,
}

costos_transporte = {
    ('A', 'B'): 100, ('A', 'C'): 150, ('A', 'D'): 120, ('A', 'E'): 200,
    ('B', 'A'): 100, ('B', 'C'): 50,  ('B', 'D'): 70,  ('B', 'E'): 250,
    ('C', 'A'): 150, ('C', 'B'): 50,  ('C', 'D'): 100, ('C', 'E'): 150,
    ('D', 'A'): 120, ('D', 'B'): 70,  ('D', 'C'): 100, ('D', 'E'): 300,
    ('E', 'A'): 200, ('E', 'B'): 250, ('E', 'C'): 150, ('E', 'D'): 300,
}

# Restricciones
tiempo_maximo = 10  # máximo de días
presupuesto_maximo = 5000  # máximo presupuesto
distancia_por_dia = 300  # distancia máxima que puede recorrer en un día

# Función para calcular el tiempo total de un recorrido
def calcular_tiempo(ruta):
    tiempo_total = 0
    for i in range(len(ruta) - 1):
        tiempo_total += distancias[(ruta[i], ruta[i + 1])] / distancia_por_dia
    return tiempo_total

# Función para calcular el costo total de un recorrido
def calcular_costo(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        costo_total += costos_transporte[(ruta[i], ruta[i + 1])]
    return costo_total

# Función de aptitud (fitness): penaliza las soluciones que no cumplen con las restricciones
def aptitud(ruta):
    tiempo = calcular_tiempo(ruta)
    costo = calcular_costo(ruta)
    
    if tiempo > tiempo_maximo or costo > presupuesto_maximo:
        return float('inf')  # Penalizar soluciones inválidas
    
    return tiempo + costo  # La aptitud es la suma del tiempo y costo total

# Inicialización de la población
def inicializar_poblacion(tamano_poblacion, ciudades):
    poblacion = []
    for _ in range(tamano_poblacion):
        individuo = random.sample(ciudades, len(ciudades))  # Ruta aleatoria
        poblacion.append(individuo)
    return poblacion

# Selección por torneo
def seleccion(poblacion, k=3):
    seleccionados = random.sample(poblacion, k)
    seleccionados.sort(key=lambda x: aptitud(x))
    return seleccionados[0]  # Retorna el individuo con mejor aptitud

# Cruce de un solo punto
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + [ciudad for ciudad in padre2 if ciudad not in padre1[:punto_cruce]]
    hijo2 = padre2[:punto_cruce] + [ciudad for ciudad in padre1 if ciudad not in padre2[:punto_cruce]]
    return hijo1, hijo2

# Mutación por intercambio de dos ciudades
def mutacion(individuo):
    i, j = random.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

# Función para ejecutar el algoritmo genético
def algoritmo_genetico(tamano_poblacion, generaciones, tasa_cruce, tasa_mutacion, ciudades):
    poblacion = inicializar_poblacion(tamano_poblacion, ciudades)
    mejor_solucion = None
    
    for generacion in range(generaciones):
        nueva_poblacion = []
        
        for _ in range(tamano_poblacion // 2):  # Crear una nueva población
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            
            # Cruce
            if random.random() < tasa_cruce:
                hijo1, hijo2 = cruce(padre1, padre2)
            else:
                hijo1, hijo2 = padre1, padre2
            
            # Mutación
            if random.random() < tasa_mutacion:
                hijo1 = mutacion(hijo1)
            if random.random() < tasa_mutacion:
                hijo2 = mutacion(hijo2)
            
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
        
        # Reemplazar la población actual con la nueva
        poblacion = nueva_poblacion
        
        # Obtener la mejor solución de la población actual
        mejor_de_generacion = min(poblacion, key=lambda x: aptitud(x))
        if mejor_solucion is None or aptitud(mejor_de_generacion) < aptitud(mejor_solucion):
            mejor_solucion = mejor_de_generacion
    
    return mejor_solucion

# Parámetros del algoritmo genético
tamano_poblacion = 100
generaciones = 500
tasa_cruce = 0.8
tasa_mutacion = 0.2

# Ejecutar el algoritmo genético
mejor_ruta = algoritmo_genetico(tamano_poblacion, generaciones, tasa_cruce, tasa_mutacion, ciudades)

# Mostrar la mejor ruta y graficarla
if mejor_ruta:
    print(f"La mejor ruta es: {' -> '.join(mejor_ruta)}")
    print(f"Tiempo total: {calcular_tiempo(mejor_ruta):.2f} días")
    print(f"Costo total: ${calcular_costo(mejor_ruta)}")
    
    # Graficar la ruta
    def graficar_ruta(ruta, coordenadas):
        x_vals = [coordenadas[ciudad][0] for ciudad in ruta]
        y_vals = [coordenadas[ciudad][1] for ciudad in ruta]
        
        plt.figure(figsize=(8, 6))
        for ciudad in coordenadas:
            plt.scatter(coordenadas[ciudad][0], coordenadas[ciudad][1], label=ciudad, s=100)
            plt.text(coordenadas[ciudad][0] + 0.1, coordenadas[ciudad][1] + 0.1, ciudad, fontsize=12)
        
        for i in range(len(ruta) - 1):
            ciudad_origen = ruta[i]
            ciudad_destino = ruta[i + 1]
            x_vals = [coordenadas[ciudad_origen][0], coordenadas[ciudad_destino][0]]
            y_vals = [coordenadas[ciudad_origen][1], coordenadas[ciudad_destino][1]]
            plt.plot(x_vals, y_vals, 'r-', lw=2)  # Línea roja
        
        plt.title("Mejor ruta del Agente Viajero con Algoritmo Genético")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        plt.legend()
        plt.grid(True)
        plt.show()

    graficar_ruta(mejor_ruta, coordenadas)
else:
    print("No se encontró una ruta que cumpla con las restricciones.")
