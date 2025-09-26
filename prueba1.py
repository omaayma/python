#ESte es un comentario
"""
precio = 54.5
print("hola mundo")
print("hola", "mundo")
print (precio, "euros")
"""
import random

"""
nombre = input("Escriba su nombre")
apellido = input("Escriba su apellido")
edad = input("EScribe tu edad")
print("Te llamas " ,nombre, apellido, "y tienes ", edad, "años")
"""

"""
edad = input("Dime tu edad")
if edad == "65":
    print("Ya deberías de estar jubilado")
else:
    print("No se..")
    """
"""
edad = 65
if edad == 18:
    print("Ya eres mayor de edad")
elif edad == 65:
    print("Ya deberçias estar jubilado")
else:
    print("No se..")
    """
"""
encontrado = True
if not encontrado:
    print("Opcion 1")
else:
    print("Opcion 2")
    """
"""
for n in range(0,5):
    print(n)
    """
"""
for n in "hola mundo":
    print(n, end="") #Con el end sale la cadena toda junta, pero si solo pongo n saldrán las letras verticalemnte
    """
"""
for n in range(0,30,2):
    print (n, end=",")
    
    
    for n in range(30,0,-2):
    print (n, end=",")
    
    
    """
"""
edad = input("Introduce tu edad")
print("Te falta", 67-int(edad), "años para la jubilación")
"""
"""
import random

azar = random.randint(1, 6)
print(azar)
"""

"""
i=0
while i<16:
    print(i)
    i+=1
"""
#ejercicio de tirar 2 dados y que ponga cuantas veces se ha lanzado hasta conseguir el mimso número
import random

lanzados=0
a1=0
a2=1

while a1!=a2:
    a1=random.randint(1,6)
    a2=random.randint(1,6)
    lanzados +=1

    print(a1, "", a2)

print("Hemos lanzado", lanzados, "veces")

