
"""

def calculadora():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Debes introducir un número válido")
        return

    operacion = input("Elige operación: S (suma), R (resta), M (multiplicación), D (división): ").upper()

    try:
        match operacion:
            case "S":
                print("Resultado:", num1 + num2)
            case "R":
                print("Resultado:", num1 - num2)
            case "M":
                print("Resultado:", num1 * num2)
            case "D":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre 0")
                print("Resultado:", num1 / num2)
            case _:
                raise ValueError("Operación no válida")
    except Exception as e:
        print("Error:", e)
calculadora()



import math



def calculadora():
    try:
        num = float(input("Introduce un número: "))
    except ValueError:
        print("Debes introducir un número válido")
        return

    operacion = input("Elige operación: R (raíz), C (cuadrado), U (cubo): ").upper()

    try:
        match operacion:
            case "R":
                if num < 0:
                    raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
                res = round(math.sqrt(num), 2)
                print("Resultado", res)
            case "C":
                print("Resultado:", num**2)
            case "U":
                print("Resultado:", num**3)
            case _:
                raise ValueError("Operación no válida")
    except Exception as e:
        print("Error:", e)
calculadora()



def mes():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    try:
        n = int(input("Introduce un número del 1 al 12: "))
        if n<1 or n>12 :
            raise ValueError("Número fuera de rango")
        print("Mes:", meses[n-1])
    except ValueError :
        print("Error, INTROUCE NUMERO VALIDO")

mes()



def calificacion():
    try:
        nota = int(input("Introduce una nota entre 1 y 10: "))
        if nota < 1 or nota > 10:
            raise ValueError("Nota fuera de rango")
    except ValueError:
        print("Error: Debes introducir un número entero entre 1 y 10")
        return

    if nota <= 2:
        print("Muy deficiente")
    elif nota <= 4:
        print("Insuficiente")
    elif nota == 5:
        print("Suficiente")
    elif nota == 6:
        print("Bien")
    elif nota <= 8:
        print("Notable")
    else:
        print("Sobresaliente")
calificacion()

import  random
def array_estadisticas():
    try:
        n = int(input("Introduce el tamaño del array: "))
        if n <= 0:
            raise ValueError("El tamaño debe ser mayor que 0")
    except ValueError:
        print("Error: Debes introducir un número entero positivo")
        return

    arr = []
    for i in range(n):
        arr.append(random.randint(10, 1000))

    maximo = max(arr)
    minimo = min(arr)
    media = sum(arr) / len(arr)

    print("Array:", arr)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    print("Media: {:.2f}".format(media))
array_estadisticas()


import random
def array_estadisticas_posiciones():
    try:
        n = int(input("Introduce el tamaño del array: "))
        if n <= 0:
            raise ValueError("El tamaño debe ser mayor que 0")
    except ValueError:
        print("Error: Debes introducir un número entero positivo")
        return

    arr = []
    for i in range(n):
        arr.append(random.randint(10, 1000))

    maximo = max(arr)
    minimo = min(arr)
    media = sum(arr) / len(arr)

    pos_max = []
    pos_min = []
    for i in range(len(arr)):
        if arr[i] == maximo:
            pos_max.append(i)
        if arr[i] == minimo:
            pos_min.append(i)

    print("Array:", arr)
    print("Máximo:", maximo, "en posiciones", pos_max)
    print("Mínimo:", minimo, "en posiciones", pos_min)
    print("Media: {:.2f}".format(media))
array_estadisticas_posiciones()


import random
def array_valor_posicion():
    try:
        n = int(input("Introduce el tamaño del array: "))
        if n <= 0:
            raise ValueError("El tamaño debe ser mayor que 0")
    except ValueError:
        print("Error: Debes introducir un número entero positivo")
        return

    arr = []
    for i in range(n):
        arr.append(random.randint(10, 1000))

    print("Array generado:", arr)

    try:
        pos = int(input("Introduce la posición que quieres recuperar: "))
        if pos < 0 or pos >= len(arr):
            raise IndexError("Posición fuera de rango")
        print("Valor en la posición {}: {}".format(pos, arr[pos]))
    except ValueError:
        print("Error: Debes introducir un número entero")
    except IndexError:
        print("Error: La posición está fuera del rango del array")

array_valor_posicion()
"""
import random
def buscaminas():
    filas = 5
    columnas = 5
    tablero = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        tablero.append(fila)

    minas = set()
    while len(minas) < 5:
        f = random.randint(0, filas-1)
        c = random.randint(0, columnas-1)
        if (f, c) not in minas:
            minas.add((f, c))
            tablero[f][c] = 1

    print("Tablero de Buscaminas:")
    for i in range(filas):
        for j in range(columnas):
            print(tablero[i][j], end=" ")
        print()

buscaminas()

