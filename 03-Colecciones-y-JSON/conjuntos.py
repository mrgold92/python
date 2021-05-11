#----------------------------------------------------------------#
# Los conjuntos son una colección de elementos sin índice,
# se dice que está desordenado.
#
# En un conjunto se pueden añadir y eliminar elementos.
#
# Para acceder a los valores tenemos que recorrer la colección
# con for.
#-----------------------------------------------------------------#

set1 = {"java", "python", "android", "java"}
set1.add("ruby")
set1.discard("java")

print(len(set1))
print(set1)
for s in set1:
    print(s)
