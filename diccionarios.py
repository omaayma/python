diccionario={"Nombre":"Sara","Edad":34,"Solter@":True}
print(diccionario)

for elemento in diccionario:
    print(elemento) #claves
print()
for elemento in diccionario:
    print(diccionario[elemento]) #valores
print()
for elemento in diccionario:
    print(elemento,":",diccionario[elemento])
print()
for clave,valor in diccionario.items():
    print(clave,":",valor)
print()
print(diccionario.get("Edad")) #si pongo una clave queno existe no salta error solo "none"
print(diccionario["Edad"]) #si pongo una clave que no existe salta error
diccionario["Edad"]=67
print(diccionario)
diccionario["Asignatura"]="Bases de Datos"
print(diccionario)
#diccionario.clear()
#dicc2=dict()  / dicc2={}
dicc2=dict(Primero="Uno",Tercero = "Tres")
dicc2["Segundo"]="Dos"
print(dicc2)
print()
print(dicc2.keys())
print(dicc2.values())
print(dicc2.items())

print(diccionario.get("Titulo","No encontrado")) #si no existe el elemento, se puede poner algo por defecto en vez de devolver none / vale false
print(diccionario.pop("Edad")) #elimina el elemento de la clave y devuelve el valor
print(diccionario)
print(diccionario.popitem()) #elimina la ultima pareja de clave-valor
print(diccionario)
print()

diccionario.update((dicc2)) #actualiza los elementos, si hay duplicados se sustituyen, si no se añaden
print(diccionario)
print()



d1=dict(Sara = 33,Pepe = 55, Luis = 44, Manolo = 21, Eva = 98, Ines = 27)
print(d1)
import random

def eliminarAlAzar(d1):
    claves = list() #claves = list(d1.keys())
    for elemento in d1:
        claves.append(elemento)
    borrar=random.choice(claves)
    d1.pop(borrar)
    print(d1)
eliminarAlAzar(d1)

d1=dict(Sara = [1,2,3],Pepe = 55, Luis = 44, Manolo = 21, Eva = 98, Ines = 27)
print(d1)

