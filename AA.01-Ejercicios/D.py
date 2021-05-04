# D1. Pregunta al operador su DNI sin letra.
# D2. Calcula el resto de dividir el número del DNI entre 23.
# D3. Muestra el DNI con la letra. El resto de la división representa la posición de la letra del DNI en lista.

def calcularLetraDNI(numeroDNI):
  return numeroDNI % 23

print(calcularLetraDNI(int(input("Dime tu DNI sin letra."))))