from http.client import responses

import requests
from requests import request

api_key = "cb43c013d40bd1865fa9317096638066"
# Coordenadas de la ubicación (latitud y longitud)
lat = "40.7128"  # Latitud de Nueva York, por ejemplo
lon = "-74.0060"  # Longitud de Nueva York

# URL para hacer la solicitud
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    datos = response.json()

    temperatura = datos['main']['temp']
    descripcion = datos['weather'][0]['description']
    ciudad = datos['name']


print(f"El reportaje de la ciudad de {ciudad} que tiene una temperatura de {temperatura}ºC y una descripcion de {descripcion}")


