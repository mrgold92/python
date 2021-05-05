#----------------------------------------------------------------#
# G1. Pregunta al operador cualquier cosa.
# G2. Muestra por Simón dice xxxxxxxxx incluyendo la respuesta
# del operador
# G3. Esta secuencia de pregunta/mostrar en pantalla se repite hasta
# que el operado responde fin
#---------------------------------------------------------------#
while(True):
    respuesta = input("¿De qué color es el caballo blanco de Santiago?: ")

    if respuesta.lower() == "fin":
        break

    print(f"Simón dice {respuesta}")
