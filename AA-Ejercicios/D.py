# -----------------------------------------------------------------#
# D1. Pregunta al operador su DNI sin letra.
# D2. Calcula el resto de dividir el número del DNI entre 23.
# D3. Muestra el DNI con la letra. El resto de la división
# representa la posición de la letra del DNI en lista.
#------------------------------------------------------------------#

lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
         'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

dni = input("Dime tu DNI sin letra:")

if dni.isdigit():
    print(f"Tu DNI es: {dni}{lista[int(dni) % 23]}")
else:
    print("Debes introducir solo números.")
