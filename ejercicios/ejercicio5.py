import random

#---------------------------------------------#
# 1. Generar número aleatorio.
# 2. Preguntar un número.
# 3. Comprobar si se ha adivinado el número.
#---------------------------------------------#
numero = random.randint(1, 20)
correcto = False

while(correcto == False):
    num = int(input("Dime un número:"))
    if(num == numero):
        correcto = True
    elif(num > numero):
        print('Prueba con un número menor.')
    else:
        print('Prueba con un número mayor.')


print(f'Has adivinado el número: {numero}')
