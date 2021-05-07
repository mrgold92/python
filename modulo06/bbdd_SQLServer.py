import pymssql
import sys

# con = pymssql.connect(server='LAPTOP-AR7UGD3M',
#                       database='prueba')

con = pymssql.connect(server='localhost', user='david',
                      password='root', database='northwind')

cursor = con.cursor(as_dict=True)

#cursor.execute("INSERT INTO Customers (CustomerID, CompanyName,City, Country) VALUES('DEMO3', 'Empresa sin nombre dos', 'Madrid', 'Spain')")

# query = "INSERT INTO Customers (CustomerID, CompanyName,City,Country) VALUES(%d, %d, %d, %d)"

# lista = []
# lista.append(('DEXX1', 'EMPRESA 1, SL', 'Madrid', 'Spain'))
# lista.append(('DEXX2', 'EMPRESA 2, SL', 'Madrid', 'Spain'))
# lista.append(('DEXX3', 'EMPRESA 3, SL', 'Madrid', 'Spain'))
# lista.append(('DEXX4', 'EMPRESA 4, SL', 'Madrid', 'Spain'))


# cursor.executemany(query, lista)
# con.commit()


# cursor.execute("UPDATE Customers SET Country = 'Spain' WHERE Country= 'España'")
# con.commit()
# print("Filas afectadas: ",cursor.rowcount)


cursor.execute("DELETE FROM Customers WHERE CustomerID LIKE 'DEMO%'")
con.commit()
print("Filas afectadas: ",cursor.rowcount)

sys.exit()


cursor.execute('SELECT * FROM customers')

for row in cursor.fetchall():
    print(f"{row['City']}")

cursor.close()
con.close()