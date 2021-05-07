#---------------------------------------------#
# 1. Preguntar al operador una frase.
# 2. Preguntar al operador una letra.
# 3. Mostrar por pantalla cuantas veces aparece 
# la letra en la frase.
# 4. Tenemos que usar un WHILE.
#---------------------------------------------#

frase = input('Dime una frase:')
letra = input('Ahora dime una letra:')

if(len(frase) < 2):
    print('Ingresa una frase más larga.')
elif(len(letra) > 1 or letra == ''):
    print('Ingresa solo una letra')
else:
    contador, i = 0, 0

    while(i < len(frase)):
        if(frase[i].lower() == letra.lower()):
            contador += 1
        i += 1

    print(f'La letra {letra} aparece {contador} veces en la frase.')
