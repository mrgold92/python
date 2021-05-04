#------------------------------------------------------#
# B1. Pregunta un número al operador y muestra el resultado
# de multiplicarlo por PI. Utiliza la constante "math.pi"
# y recuerda incluir "import math"
#
# B2. Muestra la raíz cuadrada del mismo número
#------------------------------------------------------#
import math


def multPi(numero):
    return numero*math.pi


def raiz(numero):
    return math.sqrt(numero)


# B1
numero = int(input("Dime un número: "))
print(multPi(numero))

# B2
print(raiz(numero))
