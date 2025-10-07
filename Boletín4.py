"""
#Ejericio1
num = int(input("Introduce un número: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("El factorial de", num,"es", factorial)


#Ejercicio2
num = int(input("EScribe un número:"))
a = 0
b=1

for i in range(num):
    print(a, end="")

    if i < num - 1:
        print(",", end="")
    a, b = b, a + b
"""

#Ejericio3
numMax = int(input("Introduce un número: "))
a=0
b=1

while a <= numMax:
    if b<=numMax:
        print(a, end=",")
    a, b = b, a + b


