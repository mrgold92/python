import requests

# URL de la petición
# Funciona con parámetros
# ?id = all... ANATR...
URL = 'http://api.labs.com.es/v1.0/clientes.ashx/'

para = input('Dime un identificador: ')

r = requests.get(URL, params=para)

if r.status_code == 200:
    if len(r.json()) > 0:
        if 'application/json' in r.headers['content-type']:
            for p in r.json():
                print('CustomerID: ', p['CustomerID'])
                print('CompanyName: ', p['CompanyName'])
                print('ContactName: ', p['ContactName'])
                print('ContactTitle: ', p['ContactTitle'])
                print('Address: ', p['Address'])
                print('City: ', p['City'])
                print('Region: ', p['Region'])
                print('PostalCode: ', p['PostalCode'])
                print('Country: ', p['Country'])
                print('Phone: ', p['Phone'])
                print('Fax: ', p['Fax'])
                print("=================================================")
        else:
            print("No se puede procesar el contenido.")
    else:
        print('No existe ese identificador.')
else:
    print(
        f'Error -> {r.status_code} / {r.reason}. O Ningún dato con ese indentificador.')
