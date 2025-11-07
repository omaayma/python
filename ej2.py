import random

numeros = []
contador =0


for i in range(10):
    n = random.randint(1, 100)
    numeros.append(n)


mayor = max(numeros)
menor = min(numeros)
numerosNuevos = str(numeros)
numerosNuevos = numerosNuevos.replace("[", "")
numerosNuevos = numerosNuevos.replace("]", "")

"""
#He intenado contar los pares e impares de esta manera pero no lo consigo
for i in numeros:
    if numeros%2==0:
        pares=numeros.count(i)
    else:
        impares = numeros.count(i)
        """


print("10 números entre el 1 y el 1000")
print(numerosNuevos)
#print("He generado ", pares,"números pares y ", impares, "números impares" )
print("El número mayor ha sido el", mayor, "y el menor el", menor)


