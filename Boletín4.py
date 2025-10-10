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


#Ejericio3
numMax = int(input("Introduce un número: "))
a=0
b=1

while a <= numMax:
    print(a, end=",")
    a, b = b, a + b

#Ejercicio4
num = int(input("Introduce un número: "))
numCifras = len(str(num))
print("El número", num, " tiene", numCifras, "cifras.")


#Ejercicio5
num = input("Introduce un número: ")
if num == num[::-1]:
    print("El número", num," es capicúa.")
else:
    print("El número no es capicúa")

#Ejercicio6
import math

contador = 0
num = 2

print("Primo   Raíz    Cuadrado   Cubo")
while contador < 50:
    esPrimo = True
    if num < 2:
        esPrimorimo = False
    else:
        i = 2
        while i <= int(math.sqrt(num)):
            if num % i == 0:
                esPrimorimo = False
                break
            i += 1

    if esPrimo:
        raiz = math.sqrt(num)
        cuadrado = num * num
        cubo = num * num * num
        print(num, "  ", round(raiz, 2), "  ", cuadrado, "  ", cubo)
        contador += 1
    num += 1


#Ejercicio7
import math

num = 51
while True:
    es_primo= True
    es_primoMas2 = True

    if num < 2:
        es_primo_num = False
    else:
        i = 2
        while i <= int(math.sqrt(num)):
            if num % i == 0:
                es_primo = False
                break
            i += 1

    n2 = num + 2
    if n2 < 2:
        es_primoMas2 = False
    else:
        i = 2
        while i <= int(math.sqrt(n2)):
            if n2 % i == 0:
                es_primoMas2 = False
                break
            i += 1

    if es_primo and es_primoMas2:
        print("La primera pareja de primos gemelos por encima de 50 es:", num, "y", n2)
        break
    num += 1


#Ejercicio8
num = input("Introduce un número: ")

sumaPares = 0
sumaImpares = 0

for cifra in num:
    if cifra.isdigit():
        n = int(cifra)
        if n % 2 == 0:
            sumaPares = sumaPares + n
        else:
            sumaImpares = sumaImpares + n

print("Suma de cifras pares:", sumaPares)
print("Suma de cifras impares:", sumaImpares)


#Ejercicio9
cadena = input("Introduce una cadena: ")
caracter = input("Introduce un carácter: ")

contador = 0
posiciones = []

for i in range(len(cadena)):
    if cadena[i] == caracter:
        contador = contador + 1
        posiciones.append(i)

print("El carácter", caracter, "aparece", contador, "veces.")
print("Las posiciones en las que aparece son:", posiciones)


#Ejercicio10
cadena = input("Introduce una cadena: ")
cifras = ""

for c in cadena:
    if c.isdigit():
        cifras = cifras + c

print("Cifras encontradas:", cifras)

"""

#Ejercicio11
frase = input("Introduce una frase: ")
resultado = ""

for c in frase:
    if c != " ":
        resultado += c + "-"
    else:
        if resultado.endswith("-"):
            resultado = resultado[:-1]
        resultado += " "

if resultado.endswith("-"):
    resultado = resultado[:-1]

print(resultado)


"""
#Ejercicio12
anio = int(input("Introduce un año: "))

if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    print("El año", anio, "es bisiesto.")
else:
    print("El año", anio, "no es bisiesto.")


#Ejercicio13
n = int(input("Introduce un número: "))
c = input("Introduce un carácter: ")

for i in range(n):
    print(c * n)


#Ejercicio14
hora = input("Introduce una hora: ")
partes = hora.split(":")

if len(partes) != 2:
    print("Formato incorrecto.")
else:
    horas = partes[0]
    minutos = partes[1]

    if horas.isdigit() and minutos.isdigit():
        horas = int(horas)
        minutos = int(minutos)

        if 0 <= horas <= 23 and 0 <= minutos <= 59:
            if 6 <= horas <= 11:
                print("Es hora de la mañana.")
            elif 12 <= horas <= 19:
                print("Es hora de la tarde.")
            elif 20 <= horas <= 23:
                print("Es hora de la noche.")
            else:
                print("Es hora de la madrugada.")
        else:
            print("Hora no válida.")
    else:
        print("Incorrecto.")

"""













