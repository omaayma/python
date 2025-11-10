"""

import random

num = int(input("Escribe un número: "))
while num < 10:
    print("Introduce un número correcto")

pares = []
for i in range(1, num):
    if i % 2 == 0:
        pares.append(i)

numeros = random.sample(pares, 5)

numerosNuevos = str(numeros)
numerosNuevos = numerosNuevos.replace("[", "")
numerosNuevos = numerosNuevos.replace("]", "")

print("5 números aleatorios y diferentes comprendidos entre 1 y", num, ":")
print(numerosNuevos)


import random

numeros = []
pares = 0
impares = 0

for i in range(10):
    n = random.randint(1, 1000)
    numeros.append(n)

mayor = max(numeros)
menor = min(numeros)

for i in numeros:
    if i % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1


numerosNuevos = str(numeros)
numerosNuevos = numerosNuevos.replace("[", "")
numerosNuevos = numerosNuevos.replace("]", "")

print("10 números entre el 1 y el 1000:")
print(numerosNuevos)
print("He generado", pares, "números pares y", impares, "números impares.")
print("El número mayor ha sido el", mayor, "y el menor el", menor)


texto = input("Escribe un texto:")

vocales = "aeiouAEIOU"
espacio = " "

contador_vocales = 0
contador_espacios = 0

for letra in texto:
    if letra in vocales:
        contador_vocales = contador_vocales + 1
    if letra == " ":
        contador_espacios = contador_espacios + 1


textoNuevo = ""
for letra in texto:
    if letra not in vocales and letra != " ":
        textoNuevo = textoNuevo + letra

print("Sin vocales ni espacios:", textoNuevo)
print("Vocales suprimidas:", contador_vocales)
print("Espacios en blanco suprimidos:", contador_espacios)
"""
fraccion = input("Escribe tu fracción:")

if fraccion.count("/") == 1 and fraccion[0] != "/" and fraccion[-1] != "/":
    partes = fraccion.split("/")
    numerador = partes[0]
    denominador = partes[1]

    if numerador.isdigit() and denominador.isdigit():
        numerador = int(numerador)
        denominador = int(denominador)

        if denominador != 0:
            valor = numerador / denominador
            print("El valor de tu fracción es:", round(valor, 3))
        else:
            print("Error: el denominador no puede ser 0")
    else:
        print("Error: numerador o denominador no son enteros")
else:
    print("Error: formato de fracción incorrecto")
