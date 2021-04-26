from datetime import datetime

datenow1 = datetime.now().date()
print('Fecha:', datenow1)
datenow2 = datetime.now()
print('Fecha:', datenow2)
print('Año:', datenow2.year)
print('Mes:', datenow2.month)
print('Dia:', datenow2.day)
print(f'Hora: {datenow2.hour}:{datenow2.minute}')

# Parse fechas
print("Escribe tu cumpleaños:")
# fecha = input() #d-m-y
fecha = '26-07-1992'
dt3 = datetime.strptime(fecha, '%d-%m-%Y').date() #string a date
print('Fecha parse: ', dt3 )

# Operaciones entre fechas
fechaAct = datetime.now().date()
fechaCump = fechaAct.year - dt3.year
print(f'Tienes {fechaCump} años')

# Fomatear fechas
fechaFormat = datetime.now()
print(fechaFormat.strftime('%A, %d de %b de %Y '))
print(fechaFormat.strftime('Día %j del año %Y'))
