def calcularNotaAcceso(notaBachillerato,notaFaseGeneral):
        notaAcceso = 0.6 * notaBachillerato + 0.4 * notaFaseGeneral
        return notaAcceso
def calcularNotaAdmision(notaAcceso,m1,m2,a,b):
    notaAdmision = notaAcceso + m1 * a + m2 * b
    return notaAdmision

notaBachillerato = float(input("nota Bachillerato"))
notaFaseGeneral = float(input("nota fase general"))

notaAcceso = calcularNotaAcceso(notaBachillerato,notaFaseGeneral)
print(f"tu nota de acceso es {notaAcceso}")

m1 = float(input("nota materia específica 1"))
m2 = float(input("nota materia específica 2"))
a = float(input("coeficiente ponderación 1"))
b = float(input("coeficiente ponderación 2"))

notaAdmision = calcularNotaAdmision(notaAcceso,m1,m2,a,b)

print(f"Tu nota de admision es {notaAdmision}.")

if notaAdmision >= 5 :
     print("entraste a Informática")
if notaAdmision <= 5 :
     print("entraste a Informática")

     