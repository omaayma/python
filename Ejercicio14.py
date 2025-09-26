"""
Ejercicio9
import random
num= random.randint(0,50)
print ("Número aleatorio entre 0 y 50:" , num)

Ejercicio8

importe = float(input("Introduce el importe a pagar en euros"))
meses = int(input("Introduce el número de meses"))
pagoMes = round(importe/meses, 2)
print("Tienes que pagar", pagoMes, "euros cada mes ")


Ejercicio 7
precio = float(input("Introduce el precio"))
print("Precio con Iva" , round(precio * 1.21, 2))

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
num1=int(input("Introduce el primer número"))
num2=int(input("Introduce el segundo número"))
num3=int(input("Introduce el tercer número"))

"""


#Ejercicio 25
num = float(input("Introduce un número: "))
while num > 1:
    num /= 2
    print(round(num,2))







