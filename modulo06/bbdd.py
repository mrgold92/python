#-----------------------------#
# Utilizamos mongodb.
# pip install pymongo
# pprint muy útil para ver jsons.
#---------------------------------------------#
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
import json

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

# Buscar con ascendente 1 o descente -1
result = client.Northwind.customers.find(
    {"Country": "USA", "City": "Portland"}).sort("City", -1)

for c in result:
    pprint(c)

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

# Buscar por _id
id = ObjectId("609110ee9fb937350c96c12b")
result = collection.find_one({"_id": id}).sort('City')

result = collection.find_one(
    {"_id": ObjectId("609110ee9fb937350c96c12b")}).sort('City')


# Añadir documentos a la colección
# utilizando un objeto json
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


# Insertamos un documento utilizando
# un objeto

class Customer:
    _id = None
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None


cliente = Customer()
cliente.CustomerID = "Demo 4"
cliente.CompanyName = "Uno dos Tres, S.L."
cliente.ContactName = "David Salazar"
cliente.ContactTitle = "Gerente"
cliente.Address = "Calle Gran vía 72"
cliente.City = "Madrid"
cliente.Region = "Madrid"
cliente.PostalCode = "28009"
cliente.Country = "Spain"
cliente.Phone = "(+34) 91 234 56 78"
cliente.Fax = "(+34) 91 234 56 78"

# Serializa objeto a JSON
pprint(json.dumps(cliente.__dict__))
# Otra forma de serializar a JSON
pprint(json.dumps(cliente, default=lambda x: x.__dict__))

# idNuevoDoc = client.Northwind.customers.insert_one(json.dumps(cliente,default=lambda x:x.__dict__)).inserted_id
# print("Id nuevo doc", idNuevoDoc)

idNuevoDoc = client.Northwind.customers.insert_one(
    cliente.__dict__).inserted_id
print("Id nuevo doc", idNuevoDoc)

# Editar documentos en una colección
query = {'Country': 'España'}
newValues = {
    "$set":
    {
        "Country": "Spain"
    }
}

# modificar el primero que encuentre
resultado = collection.update_one(query, newValues)
# modificar todos los que encuentre
resultado = collection.update_many(query, newValues)
print(resultado.matched_count, ' elementos encontrados.')
print(resultado.modified_count, ' elementos modificados.')

# agregación
data = client.Northwind.customers.aggregate(
    [
        {"$match": {"CustomerID": "ANATR"}},
        {"$sort": {"City": 1}},
        {"$lookup": {
            "from": "orders",
            "localField": "CustomerID",
            "foreignField": "CustomerID",
            "as": "Orders"
        }}
    ]
)

datos = data.next()
print("ID: ", datos['CustomerID'])
print("Empresa: ", datos['CompanyName'])
print("País: ", datos['Country'])

for o in datos['Orders']:
    print("ID Pedido: ", o['OrderID'])
    print("Empleado: ", o['EmployeeID'])

