
import random
num = int(input("Escribe un número:"))

for i in range(1, num):
    if num%2==0:
        numeros = random.sample(range(1, num), 5)
    if num <10:
        print("Introduce un número correcto")
numerosNuevos= str(numeros)
numerosNuevos=numerosNuevos.replace("[","")
numerosNuevos = numerosNuevos.replace("]", "")
print("5 números aleatorios y diferentes comprendidos entre el 1 y ", num, ":")
print(numerosNuevos)

