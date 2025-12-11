"""Ejercicio 1: calcular el salario total de un trabajador con horas extras
Ejercicio 3: contar cuántos elementos de una lista son pares e impares
Ejercicio 4: verificar si una palabra es un palíndromo
Ejercicio 5: función que devuelva el número mayor de tres valores
Ejercicio 6: crear una calculadora simple con funciones
Ejercicio 7: generar una tabla de multiplicar usando funciones
Ejercicio 8: calcular el promedio de una lista de números con una función
Ejercicio 9: crear una función que invierta una cadena de texto
"""

# Definir la función para calcular el salario total
def calcular_salario(horas, tarifa):
    if horas > 40:
        horas_extras = horas - 40
        salario = 40 * tarifa + horas_extras * tarifa * 1.5
    else:
        salario = horas * tarifa
    return salario

# Pedir los datos al usuario
horas = float(input("Introduce el número de horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))

# Llamar a la función y mostrar el resultado
salario_total = calcular_salario(horas, tarifa)
print(f"El salario total es: {salario_total}")




# Definir la función para contar pares e impares
def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Pedir la lista de números al usuario
numeros = [int(x) for x in input("Introduce una lista de números separados por espacio: ").split()]

# Llamar a la función y mostrar el resultado
pares, impares = contar_pares_impares(numeros)
print(f"Hay {pares} números pares y {impares} números impares.")





# Definir la función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas
    return palabra == palabra[::-1]

# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

# Llamar a la función y mostrar el resultado
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")




    # Definir la función para encontrar el número mayor
    def numero_mayor(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c


    # Pedir tres números al usuario
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    c = int(input("Introduce el tercer número: "))

    # Llamar a la función y mostrar el resultado
    mayor = numero_mayor(a, b, c)
    print(f"El número mayor es: {mayor}")





# Definir las funciones de la calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Pedir al usuario que elija una operación
operacion = input("Elige una operación (sumar, restar, multiplicar, dividir): ")

# Pedir los dos números
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

# Realizar la operación elegida
if operacion == "sumar":
    print(f"El resultado es: {sumar(a, b)}")
elif operacion == "restar":
    print(f"El resultado es: {restar(a, b)}")
elif operacion == "multiplicar":
    print(f"El resultado es: {multiplicar(a, b)}")
elif operacion == "dividir":
    print(f"El resultado es: {dividir(a, b)}")
else:
    print("Operación no válida.")




# Definir la función para generar una tabla de multiplicar
def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append(numero * i)
    return tabla

# Pedir el número al usuario
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Llamar a la función y mostrar la tabla
tabla = tabla_multiplicar(numero)
for i, valor in enumerate(tabla, 1):
    print(f"{numero} x {i} = {valor}")






# Definir la función para calcular el promedio
def calcular_promedio(numeros):
    total = 0
    for numero in numeros:
        total += numero
    promedio = total / len(numeros)
    return promedio

# Pedir una lista de números al usuario
numeros = [float(x) for x in input("Introduce una lista de números separados por espacio: ").split()]

# Llamar a la función y mostrar el resultado
promedio = calcular_promedio(numeros)
print(f"El promedio es: {promedio}")










# Definir la función para invertir una cadena de texto
def invertir_cadena(cadena):
    return cadena[::-1]

# Pedir una cadena de texto al usuario
cadena = input("Introduce una cadena de texto: ")

# Llamar a la función y mostrar el resultado
cadena_invertida = invertir_cadena(cadena)
print(f"La cadena invertida es: {cadena_invertida}")






def precio_con_iva(precio, iva):
    # Calcular el precio final
    precio_final = precio + (precio * iva / 100)
    return precio_final


# Programa principal
try:
    # Pedir datos al usuario
    precio = float(input("Introduce el precio sin IVA: "))
    iva = float(input("Introduce el porcentaje de IVA: "))

    # Validar que los valores sean positivos
    if precio < 0 or iva < 0:
        raise ValueError("El precio y el IVA deben ser positivos")

    # Llamar a la función
    total = precio_con_iva(precio, iva)

    # Mostrar resultado con formato
    print("Precio sin IVA:  {:.2f} €".format(precio))
    print("IVA aplicado:    {} %".format(int(iva)))
    print("Precio con IVA:  {:.2f} €".format(total))

except ValueError as e:
    print("Error:", e)
