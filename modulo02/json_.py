#--------------------------------------------------------------#
# JSON (JavaScript Object Notation) es un formato de texto
# sencillo para el intercambio y almacenamiento de datos.
#
# Se trata de un subconjunto de la notación literal de objetos
# de JavaScript, aunque, debido a su amplia adopción como
# alternativa XML, se considera un formato independiente
# del lenguaje.
#--------------------------------------------------------------#

import json

citricos = ["limón", "naranja", "pomelo", "lima"]
citricosJSON = json.dumps(citricos)

print(citricos)
print(citricos[2])
print(type(citricos))

print(citricosJSON)
print(citricosJSON[2])
print(type(citricosJSON))

frutas = json.loads(citricosJSON)
print(frutas)
print(frutas[2])
print(type(frutas))

semana = json.loads('["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]')
print(semana)
print(semana[2])
print(type(semana))
