import requests
import json

URL = 'http://school.labs.com.es/api/students/'
data = None

# Petición get, mostrar por identificador
id = input('Dime un identificador: ')

r = requests.get(URL+id)

if r.status_code == 200:
    data = r.json()
    for k in data.keys():
        if k == 'id':
            continue
        print(f"{k}: {data[k]}")
else:
    print(
        f'Error -> {r.status_code} / {r.reason}.')


# Actualizar con el método put
nombre = input(f"Introduce tu nombre ({data['firstName']}): ")
ap = input(f"Introduce tu apellido ({data['lastName']}): ")
fecha = input(f"Introduce tu fecha de nacimiento ({data['dateOfBirth']}): ")
classId = input(f"Dime el ID de la clase (1, 2 o 3)(Actual: {data['classId']}): ")

if(nombre != ""):
    data['firstName'] = nombre
if (ap != ""):
    data['lastName'] = ap

if (fecha != ""):
    data['dateOfBirth'] = fecha

if (classId != ""):
    data['classId'] = int(classId)

# Petición
cabeceras = {"Content-type": "application/json"}
r = requests.put(URL+id, data=json.dumps(data), headers=cabeceras)

if r.status_code == 204:
    print("Estudiante actualizado.")
else:
    print(f'Error -> {r.status_code} / {r.reason}.')
