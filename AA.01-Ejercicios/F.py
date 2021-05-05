#----------------------------------------------------------------#
# Muestra las siguientes secuencias de número utilizando un FOR:
# del 1 al 100
# del 200 al 190
# del 10 a 10000 de 100 en 100
# los números impares del 51 al 91
# los multiplos de 5 del 40 al 30
# tabla de multiplicar de PI
# del 10 al 20 sumado con el anterior
# del 20 al 10 multimplicado del 5 a 8, utilizando dos FOR
#---------------------------------------------------------------#

import math

# Del 1 al 100
for i in range(1, 101):
    print(i)

print("-------------------")

# Del 200 al 190
for i in range(200, 189, -1):
    print(i)

print("-------------------")

# Del 100 al 10000 de 100 en 100
for i in range(100, 10001, 100):
    print(i)

print("-------------------")
# Los números impares del 51 al 91
for i in range(51, 92):
    if(i % 2 != 0):
        print(i)

print("-------------------")

# Los multiplos de 5 del 40 al 30
for i in range(40, 29, -1):
    if(i % 2 == 0):
        print(i)

print("-------------------")

# La tabla de multiplicar de PI
for i in range(11):
    print(f"{math.pi:1.2f} x {i} = {(math.pi * i):1.2f}")


print("-------------------")

# Del 10 al 20 sumado con el anterior
for i in range(10, 21):
    print(i + (i-1))


print("-------------------")

# Del 20 al 10 multimplicado del 5 a 8, utilizando dos FOR

for i in range(20, 9, -1):
    for j in range(5, 9):
        print(f"{i} x {j} = {i*j}")
    print("")
