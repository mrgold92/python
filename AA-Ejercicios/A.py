#-----------------------------------------------#
# Realiza el ejercicio con el siguiente código:
#
# cadena = "Hola mundo !!"
# numero = 100
# lista = ["T", "R", "W", "A", "G", "M", "Y", "F",
# "P", "D", #"X",  # "B", "N", "J", "Z", "S", "Q",
# "V", "H", "L", # # "C", "K", "E"]
#
# A1.Pregunta el nombre del operador y muestra un saludo
# incluyendo el contenido de la variable cadena
#
# A2.Muestra el saludo, en mayúsculas, minúsculas y con la letra de cada palabra en mayúsculas
#-----------------------------------------------#

cadena = "Hola mundo !!"

# Pregunta el nombre del operador y muestra un saludo
# incluyendo el contenido de la variable cadena


def saludo(nombre):
    return f"{cadena}, ¿qué tal {nombre}?"


nombre = input("Dime tu nombre: ")

print(saludo(nombre))

# Muestra el saludo, en mayúsculas, minúsculas y con la letra de cada # palabra en mayúsculas
print(saludo(nombre).upper())
print(saludo(nombre).lower())
print(saludo(nombre).title())
