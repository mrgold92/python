#-------------------------------------------------------#
# open es la palabra reservada de Python para
# trabajar con ficheros.
#
# Requiere dos parámetros, la ruta del fichero
# y el modo de apertura.
#
# Devuelve un objeto que representa el fichero con
# métodos como read, write, readline... que nos
# permite trabajar con el fichero para leer, escribir,
# y modificar su contenido.
#
# r  -> read
# r+ -> read - write
# w  -> write - create
# w+ -> read - write - create
# a  -> write - create
# a+ -> read - write - create
# b  -> formato binario
# t  -> Abrir en modo texto (defecto).
# x  -> modo creación. (falla si el fichero existe.)
#
# a  -> Deja el cursor posicionado al final.
# w  -> Deja el cursor posicionado al principio.
#-------------------------------------------------------#

fichero = open("modulo5\\fichero.txt", "r", encoding="UTF-8")

print(f"Fichero cerrado: {fichero.closed}")  # saber si el fichero está cerrado

contenido = fichero.read()  # defecto
# contenido = fichero.read(100) # 100 primeros caracteres
# linea = fichero.readline() # línea por línea

# for i in fichero:
#   print(fichero.readline())

# lineas = fichero.readlines() # devuelve un array con todas las líneas
# print(type(lineas))
# print(len(lineas))
# print(lineas[4])

print(contenido)
fichero.close()
print(f"Fichero cerrado: {fichero.closed}")
