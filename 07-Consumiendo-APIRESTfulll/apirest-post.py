
import requests
from pprint import pprint

# Función POST
URL = 'https://postman-echo.com/post'

parametros = {"param1": "demo", "params2": "demo"}
cabeceras = {"Content-type": "application/json"}
datos = {"nombre": "David", "apellidos": "Salazar"}

r = requests.post(URL, data=datos, params=parametros, headers=cabeceras)

if r.status_code == 200:
    print("Cabeceras: ", r.headers)
    pprint(r.json())

else:
    print(f'Error -> {r.status_code} / {r.reason}.')
