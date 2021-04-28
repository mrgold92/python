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
    # __nombreatributo is private
    # _nombreatrubuto is protected
    # nombreatributo is public
    __nombre = ""
    __apellidos = ""
    __fechaNacimiento = ""
    __edad = 0


    def __init__(self, nombre, apellidos) -> None:
        self.__nombre = nombre
        self.__apellidos = apellidos

    def saluda(self) -> None:
        print(f'Hola {self.__nombre} {self.__apellidos} !!!')

    def setfechaNacimiento(self, fecha) -> None:
        try:
            if(len(fecha) == 8):
                self.__fechaNacimiento = datetime.strptime(
                    fecha, '%d-%m-%y').date()
            else:
                self.__fechaNacimiento = datetime.strptime(
                    fecha, '%d-%m-%Y').date()
            self.__calcularEdad()
        except:
            print("Formato incorrecto. [dd-mm-yyyy] || [dd-mm-yy] ")

    def __calcularEdad(self):
        self.__edad = datetime.now().date().year - self.__fechaNacimiento.year

    def getFechaNacimiento(self) -> datetime:
        return self.__fechaNacimiento

    def getEdad(self) -> int:
        try:
            if(self.__edad == 0):
                raise Exception("Debes incluir la fecha de nacimiento.")
            else:
                return self.__edad
        except Exception as e:
            print(e)

    def getNombre(self) -> str:
        return self.__nombre

    def getApellidos(self) -> str:
        return self.__apellidos


alumno = Alumno("Pepito", "Pérez")
alumno.saluda()
print('--------------------')
alumno.setfechaNacimiento("26-07-92")
print(f"Edad: {alumno.getEdad()} años.")
