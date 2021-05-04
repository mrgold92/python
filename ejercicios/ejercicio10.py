# texto = "En un lugar de la Mancha de cuyo..."
# textoBytes1 = texto.encode()  # convertir a binario
# textoBytes2 = bytes(texto, "UTF-8")  # otra forma de convertir a binario
# textoBytes3 = b"En un lugar de la Mancha de cuyo..."  # otra forma

# print(type(textoBytes1))
# print(type(textoBytes2))
# print(type(textoBytes3))

# print(textoBytes1)
# print(textoBytes2)
# print(textoBytes3)

# # Representación hexadecimal del contenido
# print(textoBytes1.hex())
# print(textoBytes2.hex())
# print(textoBytes3.hex())

# # Representación decimal del contenido
# for c in textoBytes1:
#   print(c, end=" ")

# # Decodificar texto

# print(textoBytes3.decode())# Trabajar con binario


import pickle
import os  # repesenta sistema operativo

# Leemos el fichero
file = open('modulo05\\clientes.json', 'rt', encoding='UTF-8')
contenido = file.read()
file.close()

# Guardamos el contenido del fichero en binario
file2 = open("modulo05\\clientes.bin", "wb")
pickle.dump(contenido, file2)
file2.close()

t1 = "texto de prueba"
file3 = open("modulo05\\prueba.txt", "wt")
file3.write(t1)
file3.close()

# Comando del sistema operativo
# que borra la pantalla (en windows)
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

# Comando del sistema operativo
# que borra un fichero
os.remove("modulo05\\prueba.txt")
