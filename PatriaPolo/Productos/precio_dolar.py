import requests
import json
# Llamada a la API
response = requests.get('https://api.bluelytics.com.ar/v2/latest')
response_json = response.json()

# Variables
dolar_blue = response_json["blue"]
precio_venta = int(dolar_blue["value_sell"])
print(precio_venta)

