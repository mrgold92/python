#------------------------------------------------------#
# Una función lambda es una función pequeña y anónima.
#
# lambda es una palabra reservada de Python.
#------------------------------------------------------#

def saluda(nombre):
    print(f"Hola {nombre} !!!")

saludo = lambda nombre : print(f"Hola {nombre} !!!")

saludoEdad = lambda nombre, edad : print(f"Hola {nombre}!!!, edad:{edad}")

saluda("David")
saludo("Pepe")
saludoEdad("Ana", 18)

print("--------------------")

numeros = [10, 20, 30, 55, 78, 1, 96]
x = lambda n : n+10
y = lambda n1, n2 : n1+n2

print(x(numeros[1]))
print(y(numeros[0], 40))

print("--------------------")

def multiplicar(num):
  return lambda a : a * num

def dividir(num):
  return lambda a : a / num

def formula(num):
  return lambda a : (a * num - 100) / 2

def calcular(operacion):
  for n in range(1, 11):
    print(f"{operacion(n)}") # operacion(85)(n) 85=num a=n

calcular(formula(85))