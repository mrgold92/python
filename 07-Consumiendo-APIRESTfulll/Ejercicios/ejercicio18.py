import requests

URL = 'http://school.labs.com.es/api/students/'

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
