#-----------------------------------------------#
# Realiza el ejercicio con el siguiente código:
#
# cadena = "Hola mundo !!"
# numero = 100
# lista = ["T", "R", "W", "A", "G", "M", "Y", "F",
# "P", "D", #"X",  # "B", "N", "J", "Z", "S", "Q", 
# "V", "H", "L", # # "C", "K", "E"]
#-----------------------------------------------#

# Pregunta el nombre del operador y muestra un saludo
# incluyendo el contenido de la variable cadena

cadena = "Hola mundo !!"

def saludo(nombre):
    return f"{cadena}, ¿qué tal {nombre}?"

nombre = input("Dime tu nombre: ")

print(saludo(nombre))