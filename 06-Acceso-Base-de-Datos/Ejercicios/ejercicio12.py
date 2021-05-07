from pymongo import MongoClient
from pprint import pprint
import json

# Conexión con MongoDB
connect = MongoClient("mongodb://localhost:27017/")

# Selección de la BBDD
db = connect.Northwind

# Selección de colecciones
products = db.products

print("===================================")
# Buscar cuántos productos tenemos
numProductos = products.estimated_document_count()
print("Número de productos: ", numProductos)

# Buscar y mostrar todos los productos
for product in products.find():
    print(f"{product['ProductName']}")

print("===================================")
# Buscar todos los productos cuyo UnitsInStock sea 0
# con filter
listaProductos = products.find()
pro = list(filter(lambda p: p['UnitsInStock'] == '0', listaProductos))

for p in pro:
    print(p['ProductName'])

print("===================================")
# Buscar todos los productos cuyo UnitsInStock sea 0
# directamente en la bbdd
lista = products.find({'UnitsInStock': '0'})
for p in lista:
    print(p['ProductName'])

print("===================================")

# Coste o valor de nuestro stock
# De cada producto necesitamos:
#  - UnitsInStock
#  - UnitPrice

total = 0
for p in products.find({'UnitsInStock': {'$ne': '0'}}):
    total += int(p['UnitsInStock']) * float(p['UnitPrice'])

print(f"Total en stock: {total:1.2f}€")

print("===================================")

# Coste o valor de nuestro stock
# utilizando la función aggregate

query = [
    {'$match': {'UnisInStock': {'$ne': 0}}},
    {'$addFields': {
        'Price': {'$toDouble': '$UnitPrice'},
        'Stock': {'$toInt': '$UnitsInStock'},
        }
    },
    { '$group': {
        '_id' : 'Valor del Stock',
        'Total': {'$sum': {'$multiply': ['$Price', '$Stock']}},
        'Items': { '$sum': 1}
        }
    }
]

listProductos = products.aggregate(query)
print(listProductos.next())

print("===================================")