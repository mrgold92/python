from datetime import datetime

datenow1 = datetime.now().date()
print('Fecha:', datenow1)
datenow2 = datetime.now()
print('Fecha:', datenow2)
print('Año:', datenow2.year)
print('Mes:', datenow2.month)
print('Dia:', datenow2.day)
print(f'Hora: {datenow2.hour}:{datenow2.minute}')