#----------------------------------------------------------------#
# H1. Muestra las siguientes secuencias de número utilizando
# un WHILE:
#  - del 1 al 100
#  - los números impares del 51 al 91
#  - tabla de multiplicar de PI
#  - del 20 al 10 multimplicado del 5 a 8, utilizando un FOR.
#---------------------------------------------------------------#
import math

# Números del 1 al 100
c = 0
while(c < 100):
    c += 1
    print(c)

print("--------------------")


# Números impares del 51 al 91
c = 51
while(c < 91):
    c += 1
    if(c % 2 != 0):
        print(c)

print("--------------------")

# Tabla de multiplicar de PI
c = 0
while(c < 10):
    c += 1
    print(f"{math.pi:1.2f} x {c} = {(math.pi * c):1.2f}")

# Del 20 al 10 multimplicado del 5 a 8, utilizando un FOR
# Preguntar.
