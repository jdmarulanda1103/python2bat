#establecer un estado inicial en el objeto nada más instanciarlo
class Carta:    #class es el molde para crear el objeto y desps llamarlo como queramos
    def __init__(self,palo,valor):
        self.palo = palo           #«self» es una convención que se utiliza como nombre para el primer parámetro de un método en una clase.
        self.valor = valor
    def __repr__(self):  # repr no es una variable, no puedo hacer print sobre un objeto
        return f"{self.valor} de {self.palo}"
