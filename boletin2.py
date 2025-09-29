"""
#Ejercicio1
palabras = [input("Palabra 1: "), input("Palabra 2: "), input("Palabra 3: ")]
palabras.sort()
print("Orden ascendente:", palabras)



#Ejercicio2
palabras = [input("Palabra 1: "), input("Palabra 2: "), input("Palabra 3: ")]
palabras.sort(reverse=True)
print("Orden descendente:", palabras)



#Ejericio3
precio = float(input("Introduce el precio: "))
precioIva = round(precio * 1.21, 2)
print("Precio con IVA: ", precioIva)



#Ejercicio4
nota1 = float(input("Introduce primera nota: "))
nota2 = float(input("Introduce segunda nota: "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = round((nota1 + nota2) / 2)
    print("Media:", media)
else:
    print("Introduce una nota válida")



#Ejercicio5
nota1 = float(input("Nota del trabajo en clase: "))
nota2 = float(input("Nota de ejercicios prácticos: "))
nota3 = float(input("Nota del examen: "))

notaReal = nota1 * 0.05 + nota2 * 0.15 + nota3 * 0.80
notaBoletin = round(notaReal)

print("Nota real: ", notaReal)
print("Nota boletín:", notaBoletin)


#Ejercicio6
nota1 = float(input("Nota trabajo en clase: "))
nota2 = float(input("Nota ejercicios prácticos: "))
nota3 = float(input("Nota examen: "))

mediaReal = nota1 * 0.05 + nota2 * 0.15 + nota3 * 0.80

if mediaReal > 5:
    mediaBoletin = round(mediaReal)
else:
    mediaBoletin = int(mediaReal)

print("Nota real: ", mediaReal)
print("Nota boletín:", mediaBoletin)



#Ejercicio7
n = int(input("Introduce un número: "))
for i in range(1, 11):
    print(n, "x", i,"=", n*i)


#Ejercicio8
n = int(input("Introduce un número: "))
divisores = []

for i in range(1, n + 1):
    if n % i == 0:
        divisores.append(str(i))
        #Join une cadenas, aqui uso str para convertir el número a texto
print("Divisores del número", n, ":", ", ".join(divisores))



#Ejercicio9

contador = 0
while True:
    entrada = input("Introduce un número o FIN para terminar: ")
    if entrada == "FIN":
        break
    if entrada.isdigit():
        num = int(entrada)
        if 1 <= num <= 100:
            contador += 1
        else:
            print("Error:número fuera del rango")
    else:
        print("Entrada inválida")

print("Número de entradas válidas:" , contador)


from tkinter.constants import ROUND

#Ejericio10
suma = 0
contador = 0

while True:
    entrada = input("Introduce un número o FIN para terminar: ")
    if entrada == "FIN":
        break
    if entrada.isdigit():
        num = int(entrada)
        if 1 <= num <= 100:
            suma += num
            contador += 1
        else:
            print("Error: número fuera de rango.")
    else:
        print("Entrada inválida.")

if contador > 0:
    media = suma / contador
    print("Número de entradas válidas: ", contador)
    print("Media aritmética:", round(media,2))
else:
    print("No se introdujo nada")

#Ejercicio11
numeros = []

while True:
    entrada = input("Introduce un número o FIN para terminar: ")
    if entrada == "FIN":
        break
    if entrada.isdigit():
        num = int(entrada)
        if 1 <= num <= 100:
            numeros.append(num)
        else:
            print("Error: número fuera de rango")
    else:
        print("Entrada inválida")

if numeros:
    print("Número de entradas válidas:", len(numeros))
    print("Media aritmética: ", sum(numeros)/len(numeros))
    print("Número mayor:", max(numeros))
    print("Número menor:",min(numeros))
else:
    print("No se introdujo nada")


#Ejercicio12

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
#Ejercicio13











