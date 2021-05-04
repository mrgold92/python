#------------------------------------------------------#
# Pregunta un número al operador y muestra el resultado 
# de multiplicarlo por PI. Utiliza la constante "math.pi"
# y recuerda incluir "import math"
#------------------------------------------------------#
import math

def multPi(numero):
  return numero*math.pi

print(multPi(int(input("Dime un número:"))))