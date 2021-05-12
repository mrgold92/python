# Plazas libres aparcar en Madrid

import requests
from config import cabecerasTokens
from termcolor import colored


URL = {
    'Login': 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'Parkings': 'https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability/'
}

# =====================LOGIN ================================
cabeceras = cabecerasTokens

token = ""

r = requests.get(URL['Login'], headers=cabeceras)

if r.status_code == 200:
    token = r.json()['data'][0]['accessToken']

else:
    print(f'Error -> {r.status_code} / {r.reason}.')


# ================ PARKING PLACES ========================


def infoParkings(i):
    data = {}
    data['nombre'] = i['name']
    data['direccion'] = i['address']
    data['postalCode'] = i['postalCode']

    if i['freeParking'] == None:
        data['plazasDisponibles'] = colored("Sin plazas", "red")
    else:
        data['plazasDisponibles'] = colored(str(i['freeParking']), "green")

    data['info'] = f"{'Nombre parada:':<17} {data['nombre']}\n{'Dirección:':<17} {data['direccion']}\n{'Plazas libres:':<17} {data['plazasDisponibles']}\n{'Cod.Postal:':<17} {data['postalCode']}"

    return data


cabeceras = {"accessToken": token, "Content-type": "application/json"}

r = requests.get(URL['Parkings'], headers=cabeceras)

if r.status_code == 200:
    print("Info parkings: ")

    data = list(map(infoParkings, r.json()['data']))
    totalPlazas = sum(list(map(lambda x: x['freeParking'], list(
        filter(lambda y: y['freeParking'] != None, r.json()['data'])))))

    for i in data:
        print("===================================================")
        print(i['info'])
    print("|=======================================================|")
    print(f"{'Total Plazas:':<17} {colored(totalPlazas,'blue')}")

else:
    print(f'Error -> {r.status_code} / {r.reason}.')
