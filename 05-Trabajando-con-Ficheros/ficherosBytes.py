#------------------------------------------------------#
# b delante del limitador de una cadena de caracteres
# la convierte en un array de bytes
#
# bytes() transforma una cadena de caracteres 
# en un array de bytes.
#
# encode() transforma una cadena de caracteres en un 
# array de bytes.
#
# decode() transforma un array de bytes en una cadena
# de caracteres.
# 
# Los pickle de Python son muy útiles ya que representan
# un objeto Python como una cadena de bytes.
#
# Se pueden hacer multitud de cosas con los bytes,
# como por ejemplo, almacenarlos en un archivo,
# almacenarlos en una base de datos, transferirlos a
# través de una red...
#
# Para utilizar los pickle en Python, utlizaremos el 
# módulo Pickle
#------------------------------------------------------#
import pickle

bytes1 = "En un lugar de la Mancha...".encode()
bytes2 = b"En un lugar de la Mancha..."
bytes3 = bytes("En un lugar de la Mancha...", "utf-8")
print(bytes1)
print(bytes2)
print(bytes3)
print(type(bytes3))
for b in bytes3:
  print(b, end=" ")

# pickle
texto = "Nuevo contenido para el fichero"
fichero = open("modulo05\\demo.bin", "wb")
#FALTA CONTENIDO
