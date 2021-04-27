frutas = ['naranja', 'limón', 'pomelo', 'lima']
print(frutas)
print(frutas[2])
frutas[2] = 10
print(frutas)
print(frutas[2])

# Añadir al final de la lista
frutas.append('manzana')
frutas.append('melón')
print(frutas)

# Añadir entre medias
frutas.insert(1, 'ciruela')

# Añadir muchos valores de golpe
valores = ["maracuyá", "sandía", "kiwi", "plátano"]
frutas.extend(valores)

# Eliminar
frutas.remove('naranja')
if('sandía' in frutas):
    frutas.remove('sandía')

frutas.pop(2)
print(frutas)

# Listar contenido
for fruta in frutas:
    print(fruta)

print("---------------")

# Ordenación
frutas.sort()
for fruta in frutas:
    print(fruta)

print("---------------")

# Reverse
frutas.reverse()
for fruta in frutas:
    print(fruta)

print("---------------")

# Ordenar y reverse
frutas.sort(reverse=True)
for fruta in frutas:
    print(fruta)


print("---------------")

# Número elementos
print(len(frutas))


print("---------------")

# Número ocurrencias
print(frutas.count('melón'))

print("---------------")

# Vaciar el array
frutas.clear()
for fruta in frutas:
    print(fruta)
