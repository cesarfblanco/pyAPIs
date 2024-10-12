import numpy as np

temperaturas = np.random.uniform(low=10, high=35,size=30)

#Promedio
promedio = np.mean(temperaturas)

temperaturaMax = np.max(temperaturas)
temperaturaMin = np.min(temperaturas)

#Calcular la desviación estándar de las temperaturas
desviacion_std = np.std(temperaturas)

#Filtrar las temperaturas por encima del promedio
temperaturas_altas = temperaturas[temperaturas > promedio]

print("Temperaturas del mes:", temperaturas)
print(f"Temperatura promedio: {promedio:.2f}°C")
print(f"Temperatura máxima: {temperaturaMax:.2f}°C")
print(f"Temperatura mínima: {temperaturaMin:.2f}°C")
print(f"Desviación estándar: {desviacion_std:.2f}")
print(f"Temperaturas por encima del promedio: {temperaturas_altas}")