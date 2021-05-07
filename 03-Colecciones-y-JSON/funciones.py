#----------------------------------------------------------------#
# Una función es un bloque de código que se ejecuta
# cuando es llamado.
#
# def es la palabra reservada de python para crear una
# función.
#
# return es la palabra reservada de Python para retornar
# un resultado desde una función.
#
# Las colecciones y otros objetos son parámetros por referencia.
#----------------------------------------------------------------#

def saluda(nombre):
    print(f'Hola {nombre}!!!')


def suma(a, b):
    return a+b


def addColor(colores, color):
    colores.append(color)
    return True


saluda("David")
print(suma(10, 20))
colores = ["azul", "rojo", "verde"]
addColor(colores, "negro")
print(colores)
