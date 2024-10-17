miLista = [1,2,3,4] #1=posicion 0; 2= posicion 1 ...

print(miLista)

print(miLista[2]) # lo que esta en [] es la posición de miLista


ingredientes = ["patatas","huevos"]  #la primera lista
ingredientes.append("cebolla")      #append() añade un elemento a la lista

print(ingredientes)

for ingrediente in ingredientes: # coloca en bucle los elementos de la lista
    print(ingrediente)

ingredientes.sort() #sort() hace que la lista aparezca alfabetica
print(ingredientes)

ingredientes.pop() #pop() saca el último elemento de la lista
print(ingredientes)