# ---------------------------------------------------------------------------#
# Creamos una bbdd llamada Nortwind.db
# Creamos tabla llamada Customers
# Trasladamos la información de SQLServer->Customers a SQLite -> Customers
# ---------------------------------------------------------------------------#

import sqlite3
import pymssql

# Conexiones SQLITE y SQLServer
consqlite = sqlite3.connect("06-Acceso-Base-de-Datos\\Nortwind.db")

con = pymssql.connect(server='localhost', user='david',
                      password='root', database='northwind')

# Cursores
c = consqlite.cursor()

cursor = con.cursor(as_dict=True)


# Consultas
c.execute("""CREATE TABLE IF NOT EXISTS Customers 
              (CustomerID, CompanyName, ContactName, ContactTitle, 
              Address, City, Region, PostalCode, Country, Phone, Fax)""")


cursor.execute('SELECT * FROM customers')

for row in cursor.fetchall():
    valores = (row['CustomerID'], row['CompanyName'], row['ContactName'],
               row['ContactTitle'], row['Address'], row['City'], row['Region'],
               row['PostalCode'], row['Country'], row['Phone'], row['Fax'])

    c.execute('INSERT INTO Customers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', valores)
    
    consqlite.commit()


# Cerramos conexiones y cursores
c.close()
cursor.close()
consqlite.close()
con.close()
