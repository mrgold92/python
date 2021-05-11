import requests

# URL de la petición por el método get
URL = 'https://www.zippopotam.us/es/'

# Preguntamos un código postal
cod = input('Introduce un código postal: ')
# Completamos la URL con el código postal
r = requests.get(URL+cod)

# Si el código es 200 mostramos información
if r.status_code == 200:
    # Si devuelve la información en json, la mostramos
    if r.headers['content-type'] == 'application/json':
        for p in r.json()['places']:
            print('Place Name: ', p['place name'])
            print('Longitud: ', p['longitude'])
            print('State: ', p['state'])
            print('State Abbrevation: ', p['state abbreviation'])
            print('Latitude: ', p['latitude'])
            print("=================================================")
else:
    print(f'Error -> {r.status_code} / {r.reason}')
