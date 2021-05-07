# ---------------------------------------------------------------------#
# I1. Pregunta al operador 5 colores
# I2. Muestra los colores ordenados
# I3. Muestra el color que más letras contenga
# I4. Muestra el color que más vocales contenga
# I5. Muestra la cantidad de colores que comienza y finaliza por vocal.
# ---------------------------------------------------------------------#

colores = []

# Preguntar 5 colores
for i in range(5):
    colores.append(input("Dime un color: "))

print("--------------")

# Ordenar los colores
colores.sort()
for color in colores:
    print(color)

print("--------------")

# Mostrar el color que más letra tenga
print(f"Color con más letras: {max(colores, key=len)}")

print("--------------")

# Muestra el color que más vocales contenga
s = 0
colorelegido = []

for color in colores:
    suma = 0
    for letra in color:
        if(letra.lower() in "aeiouáéíóúü"):
            suma += 1

    if(suma > s):
        colorelegido.append(color)

    s = suma

if(len(colorelegido) > 1):
    colorelegido.sort()


print("Color con más vocales:", colorelegido[0])

print("--------------")

# Muestra la cantidad de colores que comienza y finaliza por vocal.
c = 0
vocales = "aeiouáéíóúü"

for color in colores:
    if color[0].lower() in vocales or color[len(color)-1] in vocales:
        c += 1

print("Cantidad de colores que empiezan o acaban por vocal: ", c)