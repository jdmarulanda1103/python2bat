#van entre {}
#puedo añadir y quitar cosas siempre que sean diferentes
conjunto1 = {1,2,3,4}
conjunto2= {2,4,6}

conjunto1.add(5) #add= añadir cosas
print(conjunto1)

union = conjunto1|conjunto2 #junta los dos sin repetir
print(union)

interseccion= conjunto1 & conjunto2
print(interseccion)

diferencia = conjunto1 - conjunto2
print(diferencia)
