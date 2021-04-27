#--------------------------------------#
# 1. Preguntamos 10 números al operador
# 2. Añadimos los números al array.
# 3. Mostrar por pantalla la suma total de todos, la media,
# la cantidad de números pares y los impares.
#--------------------------------------#

numeros = []

while(len(numeros) != 10):

    n = input(f"- Dime un número: ")
    if(n.isdigit()):
        numeros.append(int(n))
    else:
        print("No es número")

for n in numeros:
    print(n)

pares = impares = 0
suma = sum(numeros)

for numero in numeros:
    if(numero % 2 == 0):
        pares += 1
    else:
        impares += 1


print(f"Suma total: {suma}")
print(f"Media: {(suma / len(numeros))}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
