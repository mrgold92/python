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

# Cadena de caracteres
cadena = "   hola mundo  "
print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[:2])
print(cadena[2:6])
print(cadena[-2])
print(len(cadena))
print(cadena.capitalize())
print(cadena.upper())
print(cadena.lower())
print(cadena.strip())
print(cadena.replace("hola", "adiós"))
print(cadena.lstrip())
print(cadena.rstrip())
print(cadena.split())

# Inputs y formato
nombre = input("Dime tu nombre: ")
numero = 10/3
print(nombre)
print(f"Tu nombre es: {nombre}")
print("Tu nombre es: {}".format(nombre))
print("Tu nombre es: {n}".format(n = nombre))
print("Tu nombre es:", nombre)
print("Resultado de número: {n:1.2f}".format(n=numero))