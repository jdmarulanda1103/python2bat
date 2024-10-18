# 1. pensar palabra 2.escribir _ _ _ _ 
# Pedir letras 
# Busacar SI está en la palabra
# --> SI escribir _a___   mirar si hemos acertado si es que si=fin
#--> NO quitar vidas -1 -- mirar si hemos perdido

palabraSecreta = "gato"

letrasCorrectas = []
letrasIncorrectas = []

seguirJugando = True 

while seguirJugando == True:
    for letra in palabraSecreta:
        if letra in letrasCorrectas:
            print(letra, end="") #end="" es para que no salga en columna la palabra si no en fila
        else: 
            print("_",end="")
letraPedida = input("Dime una letra\n") # \n salta la línea en la terminal

if letraPedida in palabraSecreta:
    letrasCorrectas.append(letraPedida)
else:
    letrasIncorrectas.append(letraPedida)

    print(f"correctas: {letrasCorrectas}")
    print(f"correctas: {letrasIncorrectas}")

if set(letrasCorrectas) == set(palbraSecreta):

