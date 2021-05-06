# 10308
from pymongo import MongoClient
from pprint import pprint
import json

# Conexión
client = MongoClient("mongodb://localhost:27017/")
db = client.Northwind

# Colecciones
order_details = db.order_details
orders = db.orders
products = db.products

idPedido = input("Identificador del pedido: ")

pedido = orders.find_one({"OrderID": idPedido})

if(pedido != None):
    print("===============================================================")
    print(f"Datos del pedido {idPedido}")
    print("===============================================================")
    print(f"Entregar: {pedido['ShipName']}")
    print(f"          {pedido['ShipAddress']}")
    print(f"          {pedido['ShipCity']} ({pedido['ShipCountry']})")

    # Buscamos el detalle del pedido
    # Recorremos con while el cursor del detalle del pedido
    # Mostramos cada línea del pedido
    # Buscamos y mostramos la descripcióon del producto
    # Descripción - cantidad - precio * cantidad
    detalle = order_details.find({"OrderID": idPedido})
    print("===============================================================")
    print(f"{'Nombre':<35} {'cantidad':>6} {'precio':>8} {'total':>8}")
    print("===============================================================")

    totalPedido = 0
    while(detalle.alive):
        p = detalle.next()
        productId = p['ProductID']
        producto = products.find_one({"ProductID": productId})

        t = float(p['UnitPrice']) * int(p['Quantity'])
        totalPedido += t

        print(
            f"{producto['ProductName']:<35} {p['Quantity']:>6} {p['UnitPrice']:>8} {format(t,'1.2f'):>10}")
    print("===============================================================")
    print(f"{'TOTAL':>51} {format(totalPedido,'1.2f'):>10}")

else:
    print("No hay resultados.")
