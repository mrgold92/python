#-----------------------------#
# Utilizamos mongodb.
# pip install pymongo
# pprint muy útil para ver jsons.
#---------------------------------------------#
from pymongo import MongoClient
from pprint import pprint


client = MongoClient('localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")  # conexión

# Seleccionar bbdd
# conexion.bbdd
db = client.Northwind  # base de datos
# db = cliente['Northind']  # otra forma de base de datos

# Mostrar el estado del servidor
status = db.command("serverStatus")
# pprint(status)

# Listar las colecciones de la base de datos
print(db.list_collection_names())

# Seleccionar el documento (tabla)
# db.collection
collection = db.customers
# collection = db['customers'] #otra forma

# Número de documentos en la colección
result = collection.estimated_document_count()
print(result)

print("---------------")

# Búsqueda del primer documento encontrado
result = collection.find_one()
pprint(result)

# print("---------------")

# Búsqueda de documentos
# Sin parámetros, nos devuelve todos
result = collection.find()

# for i in result:
#     pprint(i)

print("---------------")

# Búsqueda de documentos con parámetros
result = collection.find({"Country": "USA"})
# result.alive  # nos dice si el cursor se puede seguir leyendo

# Mientras haya resultados, lee.
while(result.alive):
    pprint(result.next())

result.close()

# Saber cuántos documentos hay con un filtro
cpais = collection.count_documents({'Country': 'USA'})
print(f"Documentos encontrados: {cpais}")

# Ordenar documentos
result = collection.find({"Country": "USA"}).sort('City')
for c in result:
    pprint(c)

result.close()

# Buscar multiples
multiples = collection.find(
    {"Country":  {'$in': ['USA', 'Mexico']}}).sort('City')

# for c in multiples:
#     pprint(c)

multiples.close()

multiples2 = collection.find(
    {"Country": 'USA', 'City': 'Portland'}).sort('City')
# for c in multiples2:
#     pprint(c)
multiples2.close()


# Añadir documentos
customer = {
    "CustomerID": "DEMO1",
    "CompanyName": "Uno Comidas y Bebidas, SL",
    "ContactName": "David Salazar",
    "ContactTitle": "Propietario",
    "Address": "Calle Gran Vía",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28044",
    "Country": "Spain",
    "Phone": "(+34) 91 200 20 20",
    "Fax": "(+34) 91 200 20 20"
}

#idNuevoDoc = collection.insert_one(customer).inserted_id
#print("Id nuevo doc", idNuevoDoc)

# Editar
query = {'CustomerID': 'DEMO1'}
newValues = {
    "$set":
    {
        "CompanyName": "Restaurante 1, SL",
        "Address": "Calle Serrano,81",
        "Phone": "(+34) 91 234 34 59"
    }
}

resultado = collection.update_one(query, newValues)
print(resultado.matched_count, ' elementos encontrados.')
print(resultado.modified_count, ' elementos modificados.')
