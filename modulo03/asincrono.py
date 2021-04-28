#-----------------------------------------------------#
# asyncio es una biblioteca para escribir código
# utilizando la sintaxis async/await
#
# Se utiliza como base para múltiples marcos
# asíncronos de Python que proporcionan redes
# y servidores web de alto rendimiento, bibliotecas
# de conexión de bases de datos, colas de tareas,
# distribuídas, etc.
#
# Permite realizar diferentes tareas al mismo tiempo.
#------------------------------------------------------#
import asyncio


async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("... world")

asyncio.run(main())
