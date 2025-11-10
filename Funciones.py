
"""
def miFuncion():
    texto = "Holaaaaaaa"
    otroTexto="este es otro"
    print("Dentro de la función", texto)
    return otroTexto


texto = "Hola mundo"
print("Valor devuelto: ", miFuncion())
print("Fuera de mi función", texto)



def miFuncion(texto, veces):
    for i in range(0, veces):
        print(texto)

texto="Hola mundo"
veces =3
miFuncion("Hola mundo", veces)
miFuncion(texto, 1)
print(veces)


def miFuncion(texto, veces):
    for i in range(0, veces):
        print(texto)
        veces =2
    otroTexto="Hola otra vez mundo cruel"
    print(otroTexto)


otroTexto="Hola mundo cruel"
miFuncion("Hola mundo", 3)



def miFuncion(t, l, n):
    t="HOLA MUNDO CRUEL"
    n=4,4
    l[1]=111

texto = "Hola mundo"
lista=[64,2,13]
numero= 5,5
miFuncion(texto,lista,numero)
print(texto,"-", numero, "-", lista)



def saludo(nombre, mensaje="Hola", despedida="Hasta la vista"):
    print(mensaje, nombre, despedida)

saludo("José María", despedida="Nos vemos pronto")
saludo("José María", "Atentamente")


def argumentosTupla(nombre, titulos):
    for titulo in titulos:
        print(titulo, end="")
    print(nombre)

argumentosTupla("José María", "Se")
argumentosTupla("José María", "Excelenstisimo", "Ilustrasimo")


def mostrarDatos(nombre, edad):
    print("Nombre", nombre, "Edad", edad)

mostrarDatos("JOSE MAREIA", 56)
datos = ("Pedro", 54)
mostrarDatos(*datos)
"""

def devolverTresEnteros():
    return 14, 17,29

num1, num2, num3 = devolverTresEnteros()
print(num1, num2, num3, sep="--")






