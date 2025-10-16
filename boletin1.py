"""
#EJERICICIO1
print("10 primeros enteros")
for i in range(1, 11):
    print(i)
#EJERCICIO2
print("50 primeros números pares")
contador = 0
numero = 2
while contador < 50:
    print(numero)
    numero = numero + 2
    contador = contador + 1

#EJERCICIO3
num_usuario = int(input("Introduce un número: "))
print("Los 5 primeros múltiplos de", num_usuario, "son:")
for i in range(1, 6):
    multiplo = num_usuario * i
    print(multiplo)
#EJERCICIO4
print("Divisibles por 7 (< 10000)")
for num in range(7, 10000, 7):
    print(num)

#EJERCICIO5
num_check = int(input("Introduce un número entero para ver si es par o impar: "))
if num_check % 2 == 0:
    print("El número", num_check, "es PAR.")
else:
    print("El número", num_check, "es IMPAR.")

#EJERCICIO6
num_check = int(input("Introduce un número entero para ver si es divisible por 3: "))
if num_check % 3 == 0:
    print("El número", num_check, "SÍ es divisible por 3.")
else:
    print("El número", num_check, "NO es divisible por 3.")


#Ejercicio9
import random
num= random.randint(0,50)
print ("Número aleatorio entre 0 y 50:" , num)

#Ejercicio8

importe = float(input("Introduce el importe a pagar en euros"))
meses = int(input("Introduce el número de meses"))
pagoMes = round(importe/meses, 2)
print("Tienes que pagar", pagoMes, "euros cada mes ")


#Ejercicio 7
precio = float(input("Introduce el precio"))
print("Precio con Iva" , round(precio * 1.21, 2))

#EJERCICIO10
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Suma de los dados:", dado1 + dado2)


#EJERCICIO11
import random
tiradas = 0
dado1 = 0
dado2 = 1
while dado1 != dado2:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    tiradas = tiradas + 1
    print("Tirada", tiradas, ": Dado 1 =", dado1, ", Dado 2 =", dado2)
print("Ha habido que hacer", tiradas, "tiradas para conseguir el", dado1, "doble.")

#EJERCICIO12
num_dados = int(input("Cant. Dados: "))
caras_dado = int(input("Cant. Caras: "))
resultados = 0
for i in range(num_dados):
    tirada = random.randint(1, caras_dado)
    resultados = resultados + tirada
print("TOTAL:", resultados)

#EJERCICIO13
num_dados = int(input("Cant. Dados: "))
caras_dado = 0
while caras_dado % 2 != 0:
    caras_dado = int(input("Caras (PAR): "))
resultados = 0
for i in range(num_dados):
    resultados = resultados + random.randint(1, caras_dado)
print("TOTAL:", resultados)

#Ejercicio 14
import random
num1 = int(input("Introduce el primer número"))
num2 = int(input("Introduce el segundo número"))
numAleatorio = random.randint(num1,num2)

print("El número aleatorio entre", num1, "y", num2, "es:", numAleatorio)


#Ejercicio 15
import random
num1 = int(input("Introduce el primer número"))
num2 = int(input("Introduce el segundo número"))
numAleatorio = random.randint(num2,num1)

print("El número aleatorio entre", num1, "y", num2, "es:", numAleatorio)


#Ejercicio 16

import random
print("Seis números aleatorios entre el 1 y 49:")
for i in range(6):
    print( random.randint(1,49))


#Ejercicio 17

import random

for i in range (15):
    r=random.randint(1,3)
    if r ==3:
        print("x")
    else:
        print(r)


#Ejercicio 18

import random

contador = 0
num=0
while num != 666:
    num = random.randint(1, 1000)
    contador += 1

print("¡Faltan", contador, "días para que se acabe todo!")



#Ejercicio 19
num=int(input("Introduce un número"))
for i in range(1,num):
    if num%i == 0:
        print(i)


#Ejercicio 20
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)

#EJERCICIO21
num = int(input("Dime un número: "))

es_primo = True
if num < 2:
    es_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print("ES PRIMO")
else:
    print("NO ES PRIMO")


#EJERCICIO22
MINIMO = 10000000
MAXIMO = 50000000

primo_aleatorio = 0

while True:
    primo_aleatorio = random.randint(MINIMO, MAXIMO)

    es_primo = True
    for i in range(2, primo_aleatorio):
        if primo_aleatorio % i == 0:
            es_primo = False
            break

    if es_primo:
        break

print("Primo encontrado (¡puede tardar!):")
print(primo_aleatorio)

#EJERCICIO23
print("Números primos del 1 al 100:")

# Bucle principal: va del 1 al 100
for num in range(1, 101):

    es_primo = True
    if num < 2:
        es_primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                es_primo = False  
                break

    if es_primo:
        print(num)

#EJERCICIO24
limite_inferior = int(input("Límite inferior: "))
limite_superior = int(input("Límite superior: "))

if limite_inferior > limite_superior:
    temp = limite_inferior
    limite_inferior = limite_superior
    limite_superior = temp

print("Primos entre", limite_inferior, "y", limite_superior, ":")

for num in range(limite_inferior, limite_superior + 1):

    es_primo = True

    if num < 2:
        es_primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break

    if es_primo:
        print(num)



#Ejercicio 25
num = float(input("Introduce un número: "))
while num > 1:
    num /= 2
    print(round(num,2))"""

import random

tiradas = 0
dado1 = 0
dado2 = 1
dado3 = 2

# Diccionario para contar cuántas veces sale cada número (del 1 al 6)
contador = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
# Bucle principal: sigue tirando mientras los tres dados NO sean iguales
while not (dado1 == dado2 and dado2 == dado3):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)

    tiradas = tiradas + 1

    # 2. Contar los resultados de la tirada actual
    contador[dado1] = contador[dado1] + 1
    contador[dado2] = contador[dado2] + 1
    contador[dado3] = contador[dado3] + 1

    # 3. Mostrar el resultado de la tirada
    print("Tirada", tiradas, ":", dado1, dado2, dado3)

# El bucle termina cuando dado1 == dado2 == dado3
print("Ha habido que hacer", tiradas, "tiradas para conseguir el triple", dado1)

# Mostrar el conteo final de cada número
print("CONTEO TOTAL DE NÚMEROS SALIDOS:")
print("Número 1 ha salido:", contador[1], "veces")
print("Número 2 ha salido:", contador[2], "veces")
print("Número 3 ha salido:", contador[3], "veces")
print("Número 4 ha salido:", contador[4], "veces")
print("Número 5 ha salido:", contador[5], "veces")
print("Número 6 ha salido:", contador[6], "veces")