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



#Ejercicio13
import random

numero = random.randint(1, 50)
intentos = 0

while True:
    intento = int(input("Adivina el número entre el 1 y 50: "))
    if intento == numero:
        print("Has acertado")
        print("Has fallado", intentos, "veces antes de lograrlo")
        break
    elif intento > numero:
        print("Te has pasado")
    else:
        print("Te has quedado corto")

    intentos += 1



#Ejercicio14
import random

jugar = "s"

while jugar == "s":
    numero = random.randint(1, 50)
    intentos = 0

    while True:
        intento = int(input("Adivina el número entre el 1 y 50: "))
        if intento == numero:
            print("Has acertado")
            print("Has fallado", intentos, "veces antes de lograrlo")
            break
        elif intento > numero:
            print("Te has pasado")
        else:
            print("Te has quedado corto")

        intentos += 1

    jugar = input("¿Quieres jugar otra vez?")

print("")


#Ejercicio15
import random

jugar = "s"

while jugar == "s":
    maxNumero = int(input("Introduce el número máximo: "))
    maxIntentos = int(input("Introduce el número máximo de intentos: "))

    numero = random.randint(1, maxNumero)
    intentos = 0

    while intentos < maxIntentos:
        intento = int(input("Adivina el número entre el 1 y " + str(maxNumero) + ": "))
        intentos += 1

        if intento == numero:
            print("Has acertado")
            print("Has fallado", intentos - 1, "veces antes de lograrlo")
            break
        elif intento > numero:
            print("Te has pasado")
        else:
            print("Te has quedado corto")

    if intentos == maxIntentos and intento != numero:
        print("Has agotado los", maxIntentos, "intentos. El número era", numero)

    jugar = input("¿Quieres jugar otra vez?").

print(" ")



#Ejercicio16
# Ejercicio 16: Circunferencia

radio = float(input("Introduce el radio de la circunferencia: "))

pi = 3.14159
longitud = 2 * pi * radio
area = pi * (radio ** 2)

print("La longitud de la circunferencia es:", round(longitud, 5))
print("El área de la circunferencia es:", round(area, 5))


#Ejercicio17

entrada = input("Introduce la temperatura: ")

valor = float(entrada[:-1])
unidad = entrada[-1].upper()  # Última letra, convertida en mayúscula

if unidad == "C":
    f = valor * 1.8 + 32
    k = valor + 273.15
    print(valor, "°C son", round(f, 2), "°F y", round(k, 2), "K")

elif unidad == "F":
    c = (valor - 32) / 1.8
    k = (valor - 32) * 5/9 + 273.15
    print(valor, "°F son", round(c, 2), "°C y", round(k, 2), "K")

elif unidad == "K":
    c = valor - 273.15
    f = 1.8 * (valor - 273.15) + 32
    print(valor, "K son", round(c, 2), "°C y", round(f, 2), "°F")

else:
    print("Unidad no válida. Usa C, F o K.")


#Ejercicio18

sueldo = float(input("Introduce tu sueldo anual en euros: "))

if sueldo <= 12450:
    porcentaje = 19
elif sueldo <= 20200:
    porcentaje = 24
elif sueldo <= 35200:
    porcentaje = 30
elif sueldo <= 60000:
    porcentaje = 37
elif sueldo <= 300000:
    porcentaje = 45
else:
    porcentaje = 47

retencion = sueldo * porcentaje / 100
neto = sueldo - retencion

print("Tu sueldo anual es:", sueldo, "€")
print("El porcentaje de retención es:", porcentaje, "%")
print("El importe de la retención es:", round(retencion, 2), "€")
print("El sueldo neto que cobrarás es:", round(neto, 2), "€")

"""












