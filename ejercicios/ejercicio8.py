def generoMujeres(item):
    if(item.genero == 'Female'):
        return True
    else:
        return False


def generoHombres(item):
    if(item.genero == 'Male'):
        return True
    else:
        return False


class Cliente:

    identificador = None
    nombre = None
    apellidos = None
    genero = None
    pais = None
    edad = None
    fechaAlta = None

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
        cliente = Cliente(data[7].strip(), data[1], data[2])
        cliente.genero = data[3]
        cliente.edad = int(data[5])
        cliente.pais = data[4]
        clientes.append(cliente)


fichero.close()


while True:
    # identificador = int(input("Dime un identificador: "))

    # if identificador == -1:
    #     break

    # resultado = list(filter(
    #     lambda item: item.identificador == str(identificador), clientes))

    mujeres = list(filter(lambda item: item.genero == 'Female', clientes))
    mujeres2 = list(filter(generoMujeres, clientes))
    hombres = list(filter(lambda item: item.genero == 'Male', clientes))
    hombres2 = list(filter(generoHombres, clientes))

    print(f'Hay { len(mujeres) } mujeres (lambda).')
    print(f'Hay { len(mujeres2) } mujeres (función).')
    print(f'Hay { len(hombres) } hombres. (lambda).')
    print(f'Hay { len(hombres2) } hombres (función).')

    #print(f"{len(resultado)} clientes con ese identificador.")

    # buscamos clientes menores de 26 (hasta 25) de francia
    # buscamos clientes hombre de Estados Unidos
    # buscamos mujeres de Inglaterra mayores de 26 años.

    menoresveintiseis = list(filter(lambda item: item.edad < 26 and item.pais == 'France', clientes))
    hombreseeuu = list(filter(lambda item: item.genero =='Male' and item.pais == 'United States', clientes))
    mujeresinglesas = list(filter(lambda item: item.edad > 26 and item.pais == 'Great Britain', clientes))

    print(f'Hay { len(menoresveintiseis) } clientes menores de 26 en Francia.')
    print(f'Hay { len(hombreseeuu) } hombres de EEUU.')
    print(f'Hay { len(mujeresinglesas) } mujeres de Inglaterra mayores de 26.')
    break
