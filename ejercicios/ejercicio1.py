#----------------------------------------------------#
# 1. Pregunta la fecha de nacimiento.
# 2. Calcula la edad.
# 3. Muestra por pantalla el mensaje correspondiente:
#   a. Tienes xx años, eres mayor de edad.
#   b. Te faltan xx años para ser mayor de edad.
#----------------------------------------------------#

from datetime import datetime

print("Dime tu fecha de cumpleaños: ")
fecha = input()
dt3 = datetime.strptime(fecha, '%d-%m-%Y').date()  # string a date
fechaAct = datetime.now().date()
years = fechaAct.year - dt3.year

if(years >= 18):
    print(f'Tienes {years} años. Eres mayor de edad.')
else:
    faltan = 18 - years
    print(
        f'Tienes {years} años. Te faltan {faltan} años para ser mayor de edad.')
