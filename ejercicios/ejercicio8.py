class Cliente:

    identificador = None
    nombre = None
    apellidos = None
    genero = None
    pais = None
    fechaNacimiento = None

    def __init__(self, identificador, nombre, apellidos):
        self.identificador = identificador
        self.nombre = nombre
        self.apellidos = apellidos


ruta = "modulo05\\fichero.txt"
fichero = open(ruta, "r", encoding="UTF-8")
clientes = []

for i in fichero.readlines():
    data = i.split(",")
    if(data[0].isdigit()):
        clientes.append(Cliente(data[7].strip(), data[1], data[2]))


fichero.close()


while True:
    identificador = int(input("Dime una identificador: "))

    if identificador == -1:
        break

    resultado = list(filter(
        lambda item: item.identificador == str(identificador), clientes))

    for i in resultado:
        print(f"{i.identificador} {i.nombre} {i.apellidos}")
