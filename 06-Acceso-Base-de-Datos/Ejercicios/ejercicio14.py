# ---------------------------------------------------------------------------#
# Creamos una bbdd llamada Nortwind.db
# Creamos tabla llamada Customers
# Trasladamos la información de SQLServer->Customers a SQLite -> Customers
# ---------------------------------------------------------------------------#

import sqlite3, pymssql

# Conexiones SQLITE y SQLServer
consqlite = sqlite3.connect("06-Acceso-Base-de-Datos\\Nortwind.db")

con = pymssql.connect(server='localhost', user='david',
                      password='root', database='northwind')

# Cursores
c = consqlite.cursor()

cursor = con.cursor()


# Consultas
c.execute("""CREATE TABLE IF NOT EXISTS Customers 
              (CustomerID, CompanyName, ContactName, ContactTitle, 
              Address, City, Region, PostalCode, Country, Phone, Fax)""")


cursor.execute('SELECT * FROM customers')
c.executemany("INSERT INTO Customers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", cursor.fetchall())

consqlite.commit()


# Cerramos conexiones y cursores
c.close()
cursor.close()
consqlite.close()
con.close()
