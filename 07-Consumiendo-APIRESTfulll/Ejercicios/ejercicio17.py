# ---------------------------------------- #
# Creación de un alumno utilizando una api
# ---------------------------------------- #
# http://school.labs.com.es/api/students
# firstName:asdasd, lastName:asd, datOfBirth:2006-05-09 classId:1,2 o 3 cod->201

import requests
import json

URL = 'http://school.labs.com.es/api/students'

nom = input('Introduce tu nombre: ')
ap = input("Introduce tu apellido: ")
fecha = input("Introduce tu fecha de cumpleaños(YYYY-mm-dd): ")
classId = input("Dime el ID de la clase (1, 2 o 3): ")

cabeceras = {"Content-type": "application/json"}
datos = {"firstName": nom, "lastName": ap,
         "dateOfBirth": fecha, "classId": int(classId)}

r = requests.post(URL, data=json.dumps(datos), headers=cabeceras)

if r.status_code == 201:
    print("Estudiante creado, id->", r.json()['id'])
else:
    print(f'Error -> {r.status_code} / {r.reason}.')
