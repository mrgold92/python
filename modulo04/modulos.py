
from clases import Alumno

alumno = Alumno("Lucas", "Martín")
alumno.saluda()
alumno.setfechaNacimiento("26-07-92")
print(f"Edad: {alumno.getEdad()} años.")