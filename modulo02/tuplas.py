#----------------------------------------------------------------#
# Las tuplas son una colección de datos de elementos ordenados con
# un índice de base 0.
#
# A diferencia de las listas, las tuplas no se pueden modificar.
# Por ejemplo, podríamos utilizar tuplas para:
#  - Códigos postales.
#  - Ciudades.
#  - Días de la semana.
#  - Etc.
#-----------------------------------------------------------------#

numeros = (17, 89, 21, 988, 43, 429, 32, 834)
print(numeros[4])
print(list(enumerate(numeros)))
print(max(numeros))
print(min(numeros))
print(sum(numeros))
