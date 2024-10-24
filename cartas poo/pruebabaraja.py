from baraja import Baraja #xq esta en otro archivo

mibaraja = Baraja() #estoy llamando a init
# mibaraja.mostrarCartas()

# mibaraja.barajar()
# mibaraja.mostrarCartas()

if mibaraja.quedanCartas(): #eso da True o False por el Return de la funcion
    print("Quedan cartas")
else:
    print("No quedan cartas")

while mibaraja.quedanCartas():
    carta = mibaraja.sacarCarta()
    numCartas = mibaraja.contar()
    print(f"{carta}. Quedan {numCartas}")