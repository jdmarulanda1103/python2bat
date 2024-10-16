#elegir numero

import random

minimo = 1
maximo = 10



numeroElegido= random.randint(minimo,maximo)

numeroPedido = int(input(f"Elige un número {minimo} y {maximo}"))

if numeroElegido == numeroPedido:
    print("Enhorabuena lo acertaste")
else: 
    print(f"No has acertado el numero. Era el {numeroElegido}")




#pedir el numero
#comprobar si es el mismo numero