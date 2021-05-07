#---------------------------------------------#
# Tabla de multiplicar dado un número.
#---------------------------------------------#

numero = int(input("Dime un número:"))

for i in range(11):
    print(f"{numero} x {i} = {(numero*i)}")
