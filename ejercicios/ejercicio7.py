#---------------------------------------------------#
# Modificar el ejercicio 6 para utilizar funciones.
#---------------------------------------------------#


def addNumero(lista, cantidad):
    while(len(lista) != cantidad):
        n = input("- Dime un número: ")
        if(n.isdigit()):
            lista.append(int(n))
        else:
            print("No es número")


def showList(lista):
    for n in lista:
        print(n)


def oddEven(lista):
    parimp = {"pares": 0, "impares": 0}
    for numero in lista:
        if(numero % 2 == 0):
            parimp["pares"] += 1
        else:
            parimp["impares"] += 1

    return parimp


def showResult(lista):
    showList(lista)
    print(f"Suma total: { sum(lista)}")
    print(f"Media: {( sum(lista) / len(lista))}")
    print(f"Pares: {oddEven(lista)['pares']}")
    print(f"Impares: {oddEven(lista)['impares']}")


numeros = []

try:
    addNumero(numeros, 10)

    showResult(numeros)
    
except Exception as e:
    print(e)
