import pymssql


con = pymssql.connect(server='localhost', user='david',
                      password='root', database='northwind')

cursor = con.cursor(as_dict=True)

idPedido = input("Identificador del pedido: ")

cursor.execute("SELECT * FROM orders WHERE OrderID = %d", idPedido)
pedido = cursor.fetchone()

print("===============================================================")
print(f"Datos del pedido {idPedido}")
print("===============================================================")
print(f"Entregar: {pedido['ShipName']}")
print(f"          {pedido['ShipAddress']}")
print(f"          {pedido['ShipCity']} ({pedido['ShipCountry']})")

print("===============================================================")
print(f"{'Nombre':<35} {'cantidad':>6} {'precio':>8} {'total':>8}")
print("===============================================================")

cursor.execute("SELECT ProductID, UnitPrice,Quantity,UnitPrice * Quantity AS total FROM [Order Details] WHERE OrderID = %d", idPedido)

totalPedido = 0
if(cursor.rowcount != 0):
    detalle = cursor.fetchall()
    for p in detalle:
        cursor.execute("SELECT ProductName FROM products WHERE ProductID = %d", p['ProductID'])
        producto = cursor.fetchone()
        totalPedido += p['total']
        print(f"{producto['ProductName']:<35} {p['Quantity']:>6} {p['UnitPrice']:>8} {format(p['total'],'1.2f'):>10}")

    print("===============================================================")
    print(f"{'TOTAL':>51} {format(totalPedido,'1.2f'):>10}")
    cursor.close()

else:
    print("No hay resultados.")
© 2021 GitHub, Inc.