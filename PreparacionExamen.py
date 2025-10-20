"""
precio = int(input("Escriba el precio del producto:"))
precioConIva = precio*21 /100
resultado = precio + precioConIva
print("El precio con iva es:" , resultado)




import random
tiradas=0
dado1 = 0
dado2 = 1
while dado1 != dado2:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    tiradas += 1
    print(dado1,dado2)
print("He tirado ", tiradas)



import random

numDados = int(input("Introduce el número de dados"))
numCaras = int(input("Introduce el número de caras"))
resultado = 0
for i in range(numDados):
    tiradas = random.randint(1,numCaras)
    resultado += tiradas
print(resultado)



import random

num1 = int(input("Introduce primer número"))
num2 = int(input("Introduce el segundo número"))
numAleatorio = random.randint(num2,num1)
print("Nnúmero aleatorio entre", num1, "y", num2, "es", numAleatorio)


num1 = int(input("Introduce primer número"))
num2 = int(input("Introduce el segundo número"))
num3 = int(input("Introduce tercer número"))
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.sort()
print("La lista ordenada:", lista)



num1 = int(input("Introduce primer número"))
numPrimo=True
if num1 < 2 or(num1%2 ==0 and num1!=2):
    numPrimo=False
else:
    for i in range(2, num1):
        if num1 % i == 0:
            numPrimo = False
            break
if numPrimo:
    print("Es primo")
else:
    print("No es primo")



num = float(input("Introduce un número: "))
while num > 1:
    num /= 2
    print(round(num,2))


palabras = [input("Palabra 1: "), input("Palabra 2: "), input("Palabra 3: ")]
palabras.sort()
print("Orden ascendente:", palabras)


nota1 = float(input("Introduce primera nota: "))
nota2 = float(input("Introduce segunda nota: "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = round((nota1 + nota2) / 2)
    print("Media:", media)
else:
    print("Introduce una nota válida")


num= int(input("Escribe un num:"))
divisores = []
for i in range(1, num+1):
    if num % i == 0:
        divisores.append(i)

listadivisores = str(divisores)
listadivisores = listadivisores.replace("[","")
listadivisores = listadivisores.replace("]","")
print(listadivisores, sep=",", end=" ")



import random

numero = random.randint(1, 50)
intentos = 0
maxIntentos = 5
while intentos < maxIntentos:
    intento = int(input("Adivina el número entre el 1 y 50: "))
    intentos += 1

    if intento == numero:
        print("Has acertado")
        break
    elif intento > numero:
        print("Te has pasado")
    else:
        print("Te has quedado corto")

if intentos == maxIntentos and intento != numero:
    print("Has agotado los", maxIntentos, "intentos. El número era", numero)

"""





