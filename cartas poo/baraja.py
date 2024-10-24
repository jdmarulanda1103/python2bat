import random 
from cartas import Carta

class Baraja:
    def __init__(self):
        self.cartas=[]#[]=lista vacia
        palos = ["corazones","treboles","diamantes","picas"]
        valores=["As","2","3","4","5","6","7","8","9","10",
            "Jota","Reina","Rey"]

        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo,valor))
    def barajar(self):
        random.shuffle(self.cartas)
    def mostrarCartas(self):
        for carta in self.cartas:
            print(carta)
#hasta ahora solo hemos definido lo que es una baraja
    def contar(self):
        return len(self.cartas) #len= cantidad deelementos dentro de la baraja
    def __repr__(self):
        return f"Baraja de{self.contar()}"
    def sacarCarta(self):
        if len(self.cartas)>0:
            return self.cartas.pop()
        else:
            return None
    def quedanCartas(self):
        return len(self.cartas)!=0 #!=0 len() te dice True si >0 o False si =0