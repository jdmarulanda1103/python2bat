def :
    a = int(input("Introduzca el primero número"))
    b = int(input("intruduzca el segundo número"))

elccion = 0

while True:
    print("""
    Indique la operación ha realizar:

    1)Sumar
    2)Restar
    3)Multiplicar
    4)Dividir
    5)cambiar los números indicados
    6)salir de la calculadora
    """)
    eleccion =int(input())

    if eleccion == 1:
        print(" ")
        print("RESULTADO: ",numero1," + ",{numero1}," = ",numero1+numero2)
    elif eleccion == 2:
         print(" ")
         print("RESULTADO: ",numero1," - ",numero2," = ",numero1-numero2)
    elif eleccion == 3:
         print(" ")
         print("RESULTADO: ",numero1," - ",numero2," = ",numero1-numero2)
    elif eleccion == 4:
         print(" ")
         print("RESULTADO: ",numero1," - ",numero2," = ",numero1-numero2)
    elif eleccion == 5:
        numero1 = int(input("introduzca el primer número: "))
        numero2 = int(input("introduzca el segundo número: "))
    elif eleccion == 6:
        print("Hasta pronto")