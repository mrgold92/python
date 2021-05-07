#----------------------------------------------#
# Para importar de diferentes carpetas:
#
# import sys
# sys.path.insert(0, 'ruta') 
# #tantas líneas insert como
# importanciones tengamos, subiendo el 0,1,2..
#
# from archivo import clase
# o
# from archivo import clase as alias
#-----------------------------------------------#

from clases import Alumno


alumno = Alumno("Lucas", "Martín")
alumno.saluda()
alumno.setfechaNacimiento("26-07-92")
print(f"Edad: {alumno.getEdad()} años.")