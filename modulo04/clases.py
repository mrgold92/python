#-------------------------------------------------------#
# Una clase es un constructor de objetos
#
# Class es la palabra reservada de Python para
# crear una clase.
#
# Las clases pueden contener variables, funciones
# y constructores.
#
# Las funciones y los constructores pueden estar
# sobrecargados.
#
# __init__ es el nombre especial para la función
# constructor.
#
# self es un parámetro especial que permite acceder
# al objeto mismo.
#-------------------------------------------------------#
from datetime import datetime


class Alumno:
    
    nombre = ""
    apellidos = ""
    fechaNacimiento = ""
    edad = 0


    def __init__(self, nombre, apellidos) -> None:
        self.nombre = nombre
        self.apellidos = apellidos

    def saluda(self) -> None:
        print(f'Hola {self.nombre} {self.apellidos} !!!')

    def setfechaNacimiento(self, fecha) -> None:
        try:
            if(len(fecha) == 8):
                self.fechaNacimiento = datetime.strptime(
                    fecha, '%d-%m-%y').date()
            else:
                self.fechaNacimiento = datetime.strptime(
                    fecha, '%d-%m-%Y').date()
            self.__calcularEdad()
        except:
            print("Formato incorrecto. [dd-mm-yyyy] || [dd-mm-yy] ")

    def __calcularEdad(self):
        self.edad = datetime.now().date().year - self.fechaNacimiento.year

    def getFechaNacimiento(self) -> datetime:
        return self.fechaNacimiento

    def getEdad(self) -> int:
        try:
            if(self.edad == 0):
                raise Exception("Debes incluir la fecha de nacimiento.")
            else:
                return self.edad
        except Exception as e:
            print(e)

    def getNombre(self) -> str:
        return self.nombre

    def getApellidos(self) -> str:
        return self.apellidos


alumno = Alumno("Pepito", "Pérez")
alumno.saluda()
alumno.setfechaNacimiento("26-07-92")
print(f"Edad: {alumno.getEdad()} años.")
