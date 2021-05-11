import pymssql

con = pymssql.connect(server='localhost', user='david',
                      password='root', database='northwind')

cursor = con.cursor(as_dict=True)

# Insertar un registro
cursor.execute("""INSERT INTO Customers (CustomerID, CompanyName,City, Country) 
                VALUES('DEMO3', 'Empresa sin nombre dos', 'Madrid', 'Spain')""")

# Insertar varios registros
query = "INSERT INTO Customers (CustomerID, CompanyName,City,Country) VALUES(%d, %d, %d, %d)"

lista = []
lista.append(('DEXX1', 'EMPRESA 1, SL', 'Madrid', 'Spain'))
lista.append(('DEXX2', 'EMPRESA 2, SL', 'Madrid', 'Spain'))
lista.append(('DEXX3', 'EMPRESA 3, SL', 'Madrid', 'Spain'))
lista.append(('DEXX4', 'EMPRESA 4, SL', 'Madrid', 'Spain'))


cursor.executemany(query, lista)
con.commit()

# Actualizar registro
cursor.execute(
    "UPDATE Customers SET Country = 'Spain' WHERE Country= 'España'")
con.commit()
print("Filas afectadas: ", cursor.rowcount)


# Borrar registro
cursor.execute("DELETE FROM Customers WHERE CustomerID LIKE 'DEMO%'")
con.commit()
print("Filas afectadas: ", cursor.rowcount)

# Seleccionar registros
cursor.execute('SELECT * FROM customers')

for row in cursor.fetchall():
    print(f"{row['City']}")

# Cerrar cursores y conexiones
cursor.close()
con.close()
