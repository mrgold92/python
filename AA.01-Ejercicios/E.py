# -----------------------------------------------------------------#
# E1. Pregunta un número al operador y muestra el mensaje los siguientes mensajes:
#   - Correcto si el valor coincide con el contenido en la variable numero
#   - Bajo si el valor es inferior al contenido en la variable numero
#   - Alto si el valor es superior al contenido en la variable numero
#   - Añade la palabra Demasiado si la diferencia entre el valor y
#     contenido de la variable # numero es de 25 o más.
#------------------------------------------------------------------#
numero = 100
mensaje = ""


try:
    n = int(input("Dime un número: "))

    if(n == numero):
        mensaje = "Correcto."
    elif(n < numero):
        mensaje = "Bajo."
    elif((n-numero) >= 25):
        mensaje = "Demasiado."
    elif(n > numero):
        mensaje = "Alto."

    print(mensaje)
except:
    print("Error.")
