#--------------------------------------------------#
# 1. Pregunta los metros.
# 2. Pregunta el tiempo en minutos.
# 3. Calcula la velocidad km/h.
# 4. Muestra por pantalla el mensaje correspondiente:
#   a. Inferior a 30km/h
#      -> Velocidad moderada.
#    b. Mayor de 30km/h e inferior a 75km/h.
#      -> Velocidad media.
#    c. Mayor de 75km/h
#      -> Velocidad Alta.
#--------------------------------------------------#

metros = float(input("Dime los metros recorridos:"))
minutos = float(input("Dime los minutos utilizados:"))
velocidad = ((metros/1000) / (minutos / 60))

print('{:.2f}km/h'.format(velocidad))

if(velocidad <= 30):
    print("Velocidad moderada.")
elif(velocidad > 30 and velocidad <= 75):
    print("Velocidad media.")
else:
    print('Velocidad alta.')
