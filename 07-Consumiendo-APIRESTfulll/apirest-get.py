# requests es el objeto que representa la
# conexión http
#   - Las funciones de requests genera un objeto
#     respuesta desde donde podemos acceder a los
#     datos de respuesta
#   - text contiene el texto de la respuesta
#   - json() retorna el objeto deserializado de una
#     respuesta JSON

import requests

# Función GET

# URL de la petición por el método get
r = requests.get('http://api.open-notify.org/iss-now.json')

# Imprimimos el tipo de r -> <class 'requests.models.Response'>
print(type(r))

# Imprimimos el código de estado.
# Ejemplo status_code: 200
# reason para ver el estado en texto -> ok, not found...
print("Código de estado: ", r.status_code)
print("Estado: ", r.reason)

if r.status_code == 200:
    # Imprimimos las cabeceras
    print("Cabeceras: ", r.headers)

    # De las cabeceras, imprimimos el content-type
    # Ej de content-type -> application/json
    print("Content-type: ", r.headers['content-type'])

    if r.headers['content-type'] == 'application/json':
        # r.json() Devuelve el contenido de una respuesta en formato json.
        # De esa respuesta, obtenemos la distinta información
        data = r.json()
        print('Latitud: ', data['iss_position']['latitude'])
        print('Longitud: ', data['iss_position']['longitude'])
        print('Timestamp: ', data['timestamp'])
        print('Mensaje: ', data['message'])
    else:
        print("Contenido: ", r.text)
        print("Contenido: ", r.content)

