import sqlite3


# Si no existe el fichero, lo crea
con = sqlite3.connect("06-Acceso-Base-de-Datos\\demo.db")

c = con.cursor()


# # command = "SELECT count(name) FROM sqlite_master WHERE type = 'table' and name='alumnos'"
# # c.execute(command)
# # tablas = c.fetchone()[0]
# # if tablas == 0:

# # Siempre necesitamos crear las tablas o comprobar que ya no existan
# c.execute("""CREATE TABLE IF NOT EXISTS Alumno (id, nombre, apellidos, curso, notas)""")

# # Insercción
# c.execute("INSERT INTO Alumno VALUES('A00', 'David', 'Salazar', '1A', '')")

# listaAlumnos = [('AR0', 'Ana', 'Trujillo', '1A', ''),
#                 ('Z02', 'Jimena', 'Sanz', '2A', '')]

# c.executemany('INSERT INTO Alumno VALUES(?, ?, ?, ?, ?)', listaAlumnos)

# con.commit()


# Selección
c.execute("SELECT * FROM Alumno")

for a in c.fetchall():
  print(a)

con.close()
