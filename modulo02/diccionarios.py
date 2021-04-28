#---------------------------------------------------------#
# Un diccionario es una coleccion de elementos indexados
# por su clave
#
# Cada elemento del diccionario se compone de clave y valor.
#
# Cuando recorremos un diccionario mediante for los valores
# que obtenemos son las claves.
#
# get(k, "") muestra el valor de una clave o un valor
# alternativo si la clave no existe.
#---------------------------------------------------------#

dicc = {"red": "rojo", "blue": "azul", "green": "verde"}
print(dicc)

# añadimos nuevo elemento (si existe la clave, se modifica)
dicc["black"] = "negro" 
 
dicc.pop("blue")  # eliminamos el elemento con la clave blue
print(dicc)

print(dicc["red"])

for k in dicc:
    print(k, '->', dicc[k])
