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
while(c <= 91):
    if(c % 2 != 0):
        print(c)
    c += 1

print("--------------------")

# Tabla de multiplicar de PI
c = 0
while(c <= 10):
    print(f"{math.pi:1.2f} x {c} = {(math.pi * c):1.2f}")
    c += 1

print("--------------------")
# Del 20 al 10 multimplicado del 5 a 8, utilizando un while
c1, c2 = 20, 5
while(c1 >= 10):
    while(c2 <= 8):
        print(f"{c1} x {c2} = {c1*c2}")
        c2 += 1
    c1 -= 1
    c2 = 5
