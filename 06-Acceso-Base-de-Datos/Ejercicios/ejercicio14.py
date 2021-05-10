# ---------------------------------------------------------------------------#
# Creamos una bbdd llamada Nortwind.db
# Creamos tabla llamada Customers
# Trasladamos la información de SQLServer->Customers a SQLite -> Customers
# ---------------------------------------------------------------------------#

import sqlite3
import pymssql

consqlite = sqlite3.connect("06-Acceso-Base-de-Datos\\Nortwind.db")

c = consqlite.cursor()

con = pymssql.connect(server='localhost', user='david',
                      password='root', database='northwind')

cursor = con.cursor(as_dict=True)


c.execute("""CREATE TABLE IF NOT EXISTS Customers 
              (CustomerID, CompanyName, ContactName, ContactTitle, 
              Address, City, Region, PostalCode, Country, Phone, Fax)""")


cursor.execute('SELECT * FROM customers')

for row in cursor.fetchall():
    valores = (row['CustomerID'], row['CompanyName'], row['ContactName'], row[
        'ContactTitle'], row['Address'], row['City'], row['Region'], row['PostalCode'], row['Country'], row['Phone'], row['Fax'])
    c.execute(
        'INSERT INTO Customers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', valores)
    consqlite.commit()


c.close()
cursor.close()
consqlite.close()
con.close()


# cliente.CustomerID = "Demo 4"
# cliente.CompanyName = "Uno dos Tres, S.L."
# cliente.ContactName = "David Salazar"
# cliente.ContactTitle = "Gerente"
# cliente.Address = "Calle Gran vía 72"
# cliente.City = "Madrid"
# cliente.Region = "Madrid"
# cliente.PostalCode = "28009"
# cliente.Country = "Spain"
# cliente.Phone = "(+34) 91 234 56 78"
# cliente.Fax = "(+34) 91 234 56 78"
