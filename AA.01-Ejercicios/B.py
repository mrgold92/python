#------------------------------------------------------#
# B1. Pregunta un número al operador y muestra el resultado
# de multiplicarlo por PI. Utiliza la constante "math.pi"
# y recuerda incluir "import math"
#
# B2. Muestra la raíz cuadrada del mismo número.
#
# B3. Muestra el arco coseno del mismo número.
#------------------------------------------------------#
import math


def multPi(numero):
    return numero*math.pi


def raiz(numero):
    return math.sqrt(numero)


def arcoCoseno(numero):
    return math.acos(numero)


# B1
numero = int(input("Dime un número: "))
print(f"{numero} * PI = {multPi(numero)}")

# B2
if(numero >= 0):
    print(f"Raíz de {numero} = {raiz(numero)}")

# B3
if numero >= -1 and numero <= 1:
    print(f"Arco Coseno de {numero}: {arcoCoseno(numero)}")
