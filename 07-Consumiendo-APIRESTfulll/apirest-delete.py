import requests

URL = 'http://school.labs.com.es/api/students/'

# Función DELETE
id = input('Dime un identificador: ')

r = requests.delete(URL+id)

if r.status_code == 200:
    print("Estudiante borrado, id->", r.json()['id'])
else:
    print(
        f'Error -> {r.status_code} / {r.reason}.')
