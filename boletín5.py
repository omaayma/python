"""
#Ejercicio1
import random

numeros = random.sample(range(1, 50), 6)
print("Números generados:", numeros)


#Ejericio2
num1 = int(input("Escribe el primer número"))
num2 = int(input("Escribe el segundo número"))

divisores = []

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        divisores.append(i)
print("Los divisores comunes:", divisores)
"""

#Ejercicio3


