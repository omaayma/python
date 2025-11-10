"""
print("Inicio mi programa")
try:
    denominador=input(int("Introduce el denominador"))
    x=24/denominador
    print(x)
except:
    print("EXCEPCIONES")
finally:
    print("Haya o no haya una excepcion")
print("Fin del programa")

from zope.interface.common.interfaces import IValueError

print("Inicio mi programa")
try:
    denominador=input(int("Introduce el denominador"))
    x=24/denominador
    print(x)
except ZeroDivisionError:
    print("No se puede dividir")
except IValueError:
    print("NO se puede convertir")
except:
    print("NO reconcodio la excepcion")
else:
    print("Error")
finally:
    print("Haya o no haya una excepcion")
print("Fin del programa")


#algunas cosas de listas que no hemos visto
lista = ["Pepe","María", "Juan"]
for nombre in lista:
    print(nombre)

for i, nombre in enumerate(lista):
    print(i, "-", nombre)


numero1 = [7]
numero2 = numero1.copy() #si haces copy se hace una copia del original y si no se pone solo se hace una referencia(donde el resultado saldrá igual)
numero2[0] =numero2[0] *2
print(numero2)
print(numero1)
"""
#seguimos con excepciones
"""
n = int(input("Inrroduce un numero entero positivo:"))
if n<0:
    raise Exception("No es un entero positivo")
print(n)

"""
n = int(input("Inrroduce un numero entero positivo:"))
assert (n>0 and n!=5), "El número no es positvo" #si introduces 1 esta bien pero otro numero sale excepcion
