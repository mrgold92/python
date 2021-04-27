numero0 = "32"
numero1 = 100
numero2 = 0

try:
    if(type(numero0) is not int):
        raise Exception("La variable no es numérica")  # lanzar excepciones
    print(numero1/numero2)
except ZeroDivisionError:
    print('Error: No se puede dividir por cero.')
except Exception as e:
    print(e)
except:
    print('Error.')
else:
    print('Todo ok.')
finally:
    print('Fin del programa.')
