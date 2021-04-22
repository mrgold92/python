# Tipos de datos

numero = 10
Numero = 20
saludo = "Hola a todos !!"

print(numero)
print(Numero)
print(numero+Numero)
print("Saludo: " +saludo)

print(type(numero))
print(type(saludo))

# Asignación simultánea
a = 10
b = 5

a,b = b,a

print(a)
print(b)

# Casting de tipos
a = 5
b = "25"
c = "25.7"
d = 25.8999
print("Número: " + str(a))
print(int(b))
print(float(c))
print(int(d))