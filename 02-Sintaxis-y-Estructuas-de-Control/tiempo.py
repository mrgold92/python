import time
#----------------------------------------------------------------#
# time() retorna el tiempo actual.
# localtime() retorna una representación local del tiempo.
# aasctime() retorna una representación del tiempo alfanumérica
# con fecha, hora y día de la semana.
#----------------------------------------------------------------#

print('Time: ', time.time())
print(time.localtime(time.time()))
print('Año: ', time.localtime(time.time()).tm_year)
print('Minutos: ', time.localtime(time.time()).tm_min)
print('Milisegundos: ', int(time.time() * 1000.0))
print(time.asctime(time.localtime(time.time())))
