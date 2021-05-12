
# =======================================================#
# El ejercicio consiste en buscar información de la EMT.
# config:
#   cabecerasTokens = {"X-ClientId": "lo que sea",
#           "passKey": "lo que sea"}
# =======================================================#

import requests
import json
from datetime import datetime
from config import cabecerasTokens


URL = {
    'Base': 'https://openapi.emtmadrid.es/v1/',
    'Login': 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'TimeArrival': 'https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopId>/arrives/'
}


# =====================LOGIN ================================
cabeceras = cabecerasTokens

token = ""

r = requests.get(URL['Login'], headers=cabeceras)

if r.status_code == 200:
    token = r.json()['data'][0]['accessToken']

else:
    print(f'Error -> {r.status_code} / {r.reason}.')


# ================TIME ARRIVAL BUS ========================

def infoArrival(arrive):
    print("========================================================")
    print(f"Línea: {arrive['line']}.")
    print(f"{'':>5}- Destino: {arrive['destination']}.")
    print(f"{'':>5}- Distancia: {arrive['DistanceBus']}m.")

    minutos = arrive['estimateArrive']//60

    if minutos < 2:
        if minutos == 0:
            minutos = "Llegando"
        else:
            minutos = f'{minutos} minuto'
    else:
        if(minutos > 20):
            minutos = '+20 minutos'
        else:
            minutos = f'{minutos} minutos'

    print(f"{'':>5}- Tiempo estimado de llegada: {minutos}.")


parada = input("Introduce el número de una parada: ")

body = {
    "cultureInfo": "ES",
    "Text_StopRequired_YN": "Y",
    "Text_EstimationsRequired_YN": "Y",
    "Text_IncidencesRequired_YN": "N",
    "DateTime_Referenced_Incidencies_YYYYMMDD": datetime.now().date().strftime('%Y%m%d')
}
cabeceras = {"accessToken": token, "Content-type": "application/json"}

r = requests.post(URL['TimeArrival'].replace(
    '<stopId>', parada), data=json.dumps(body), headers=cabeceras)

if r.status_code == 200:
    data = r.json()
    arrives = data['data'][0]['Arrive']

    print(f"Información de la parada: {parada}:")

    for arrive in list(map(infoArrival, arrives)):
        arrive

else:
    print(f'Error -> {r.status_code} / {r.reason}.')
