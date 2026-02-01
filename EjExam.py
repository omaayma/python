"""1. Números aleatorios, pares, impares y primos

Escribe una función que pida un número entero n > 0 (lanza ValueError si no).

Genera una lista de n números aleatorios entre 1 y 200.

Separa los números en tres listas: pares, impares y primos.

Muestra todas las listas en consola.

2. Validación de fecha y cálculo de edad

Crea una función que pida una fecha en formato dd/mm/aaaa.

Usa expresiones regulares para validar el formato.

Si la fecha no es válida, lanza ValueError.

Si es válida, calcula la edad aproximada del usuario y muestra si es “Adulto” o “Menor”.

3. Muestra aleatoria de lista

Escribe una función que pida un número entero n > 5.

Genera una lista de n números aleatorios entre 10 y 1000.

Crea otra lista de 5 elementos usando random.sample (sin repetidos).

Ordena ambas listas, imprime ambas y muestra la suma de cada una.

4. Validación de matrícula de coche

Crea una función que pida una matrícula española (formato 4 números + 3 letras).

Valida el formato con expresiones regulares.

Si es incorrecta, lanza ValueError.

Si es correcta, muestra cuántas letras vocales contiene.

5. Estadísticas de lista aleatoria

Escribe una función que pida un número entero n > 0.

Genera una lista de n números aleatorios entre 1 y 1000.

Muestra el máximo, mínimo, media (2 decimales) y todas las posiciones del máximo y mínimo.

6. Contador de palabras y palíndromos

Función que reciba un texto del usuario.

Si está vacío, lanza ValueError.

Cuenta el total de palabras y cuántas de esas palabras son palíndromos.

Muestra los resultados en consola.

7. Calculadora avanzada con excepciones

Función que pida dos números y una operación (+, -, *, /, **).

Si la operación es / y el segundo número es 0, lanza ZeroDivisionError.

Muestra el resultado con 3 decimales.

8. Tablero de minas simplificado

Función que genere una matriz de 6 filas × 4 columnas con ceros.

Pide un número entero m (1 ≤ m ≤ 24).

Coloca m minas (1) en posiciones aleatorias sin repetir (usar set).

Imprime la matriz fila por fila.

9. Lista con transformaciones

Función que pida un número entero n > 0.

Genera una lista de n números aleatorios entre 50 y 150.

Sustituye cada número impar por su triple y cada par por su mitad.

Imprime la lista antes y después.

10. Extracción de fechas de un texto

Función que reciba un texto del usuario.

Si está vacío, lanza ValueError.

Usa expresiones regulares para extraer todas las fechas en formato dd/mm/aaaa.

Para cada fecha encontrada, calcula cuántos días han pasado hasta hoy (usa datetime).

Muestra la lista de fechas y los días transcurridos.

Ejercicio 1: Análisis completo de texto

Función que reciba un texto del usuario.

Si el texto está vacío, lanza ValueError.

Debe calcular y mostrar:

Número de palabras

Número de vocales (a, e, i, o, u, mayúsculas y minúsculas)

Número de consonantes

Número de dígitos que aparecen en el texto

Todo se muestra alineado usando format.

Debe usar bucles y listas para recorrer el texto y contar los elementos.

Ejercicio 2: Validación y separación de correo electrónico

Función que pida un correo electrónico al usuario.

Valida el formato usando expresiones regulares (usuario@dominio.ext).

Si el formato no es correcto, lanza ValueError.

Si es válido, imprime:

Parte del usuario (antes de @)

Dominio (después de @)

Extensión (después del último .)

Usa format para mostrar los resultados en columnas alineadas.

Debe manejar excepciones si la entrada no cumple.

Ejercicio 3: Estadísticas de palabras y transformación

Función que reciba un texto del usuario.

Si el texto está vacío, lanza ValueError.

Realiza lo siguiente:

Separa el texto en palabras.

Crea una lista con las palabras invertidas.

Cuenta cuántas palabras empiezan con mayúscula.

Cuenta cuántas palabras tienen más de 5 letras.

Imprime cada palabra invertida junto con su longitud, alineadas en columnas usando format.

Debe usar bucles y listas para procesar las palabras."""

import random
import math
import re
from datetime import date, datetime

# 1. Números aleatorios, pares, impares y primos
def numeros_pares_impares_primos():
    try:
        n = int(input("Introduce un número entero mayor que 0: "))
        if n <= 0:
            raise ValueError("El número debe ser mayor que 0")
    except ValueError as e:
        print("Error:", e)
        return

    numeros = []
    lista_pares = []
    lista_impares = []
    lista_primos = []

    i = 0
    while i < n:
        num = random.randint(1, 200)
        numeros.append(num)
        i = i + 1

    j = 0
    while j < len(numeros):
        num = numeros[j]

        if num % 2 == 0:
            lista_pares.append(num)
        if num % 2 != 0:
            lista_impares.append(num)

        if num > 1:
            es_primo = True
            k = 2
            while k <= int(math.sqrt(num)):
                if num % k == 0:
                    es_primo = False
                k = k + 1
            if es_primo:
                lista_primos.append(num)
        j = j + 1

    print("Lista completa:", numeros)
    print("Pares:", lista_pares)
    print("Impares:", lista_impares)
    print("Primos:", lista_primos)


# 2. Validación de fecha y cálculo de edad
def validar_fecha_y_edad():
    fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    if not re.match(r"^\d\d/\d\d/\d\d\d\d$", fecha):
        raise ValueError("Formato incorrecto, debe ser dd/mm/aaaa")

    partes = fecha.split("/")
    dia = int(partes[0])
    mes = int(partes[1])
    anio = int(partes[2])

    hoy = date.today()
    edad = hoy.year - anio
    if hoy.month < mes:
        edad = edad - 1
    elif hoy.month == mes:
        if hoy.day < dia:
            edad = edad - 1

    print("Edad aproximada:", edad)
    if edad >= 18:
        print("Adulto")
    if edad < 18:
        print("Menor")


# 3. Muestra aleatoria de lista
def lista_muestra_aleatoria():
    try:
        n = int(input("Introduce un número entero mayor que 5: "))
        if n <= 5:
            raise ValueError("El número debe ser mayor que 5")
    except ValueError as e:
        print("Error:", e)
        return

    lista = []
    i = 0
    while i < n:
        lista.append(random.randint(10, 1000))
        i = i + 1

    muestra = []
    while len(muestra) < 5:
        indice = random.randint(0, n - 1)
        if lista[indice] not in muestra:
            muestra.append(lista[indice])

    # Ordenar lista
    p = 0
    while p < len(lista):
        q = p + 1
        while q < len(lista):
            if lista[p] > lista[q]:
                temp = lista[p]
                lista[p] = lista[q]
                lista[q] = temp
            q = q + 1
        p = p + 1

    # Ordenar muestra
    p = 0
    while p < len(muestra):
        q = p + 1
        while q < len(muestra):
            if muestra[p] > muestra[q]:
                temp = muestra[p]
                muestra[p] = muestra[q]
                muestra[q] = temp
            q = q + 1
        p = p + 1

    suma_lista = 0
    i = 0
    while i < len(lista):
        suma_lista = suma_lista + lista[i]
        i = i + 1

    suma_muestra = 0
    i = 0
    while i < len(muestra):
        suma_muestra = suma_muestra + muestra[i]
        i = i + 1

    print("Lista completa:", lista)
    print("Suma lista completa:", suma_lista)
    print("Muestra de 5 elementos:", muestra)
    print("Suma muestra:", suma_muestra)


# 4. Validación de matrícula de coche
def validar_matricula():
    matricula = input("Introduce matrícula (0000ABC): ").upper()
    if not re.match(r"^\d\d\d\d[A-Z][A-Z][A-Z]$", matricula):
        raise ValueError("Matrícula inválida")

    letras = matricula[4:7]
    vocales = 0
    i = 0
    while i < len(letras):
        if letras[i] in "AEIOU":
            vocales = vocales + 1
        i = i + 1

    print("Número de vocales en matrícula:", vocales)


# 5. Estadísticas de lista aleatoria
def estadisticas_lista():
    try:
        n = int(input("Introduce un número entero mayor que 0: "))
        if n <= 0:
            raise ValueError("Debe ser mayor que 0")
    except ValueError as e:
        print("Error:", e)
        return

    lista = []
    i = 0
    while i < n:
        lista.append(random.randint(1, 1000))
        i = i + 1

    maximo = lista[0]
    minimo = lista[0]
    i = 0
    while i < len(lista):
        if lista[i] > maximo:
            maximo = lista[i]
        if lista[i] < minimo:
            minimo = lista[i]
        i = i + 1

    suma = 0
    posiciones_max = []
    posiciones_min = []
    i = 0
    while i < len(lista):
        suma = suma + lista[i]
        if lista[i] == maximo:
            posiciones_max.append(i)
        if lista[i] == minimo:
            posiciones_min.append(i)
        i = i + 1

    media = round(suma / len(lista), 2)

    print("Lista:", lista)
    print("Máximo:", maximo, "en posiciones", posiciones_max)
    print("Mínimo:", minimo, "en posiciones", posiciones_min)
    print("Media:", media)


# 6. Contador de palabras y palíndromos
def contador_palindromos():
    texto = input("Introduce un texto: ").strip()
    if texto == "":
        raise ValueError("Texto vacío")

    palabras = texto.split()
    palindromos = []
    i = 0
    while i < len(palabras):
        palabra = palabras[i]
        invertida = ""
        j = len(palabra) - 1
        while j >= 0:
            invertida = invertida + palabra[j]
            j = j - 1
        if palabra.lower() == invertida.lower():
            palindromos.append(palabra)
        i = i + 1

    print("Número de palabras:", len(palabras))
    print("Número de palíndromos:", len(palindromos))
    print("Palíndromos encontrados:", palindromos)


# 7. Calculadora avanzada con excepciones
def calculadora_avanzada():
    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
    except ValueError:
        print("Error: Debes introducir números válidos")
        return

    operacion = input("Operación (+, -, *, /, **): ")

    if operacion == "+":
        resultado = a + b
    elif operacion == "-":
        resultado = a - b
    elif operacion == "*":
        resultado = a * b
    elif operacion == "/":
        if b == 0:
            print("Error: División por cero")
            return
        resultado = a / b
    elif operacion == "**":
        resultado = a ** b
    else:
        print("Operación no válida")
        return

    print("Resultado: {:.3f}".format(resultado))


# 8. Tablero de minas simplificado
def tablero_minas():
    filas = 6
    columnas = 4
    tablero = []
    i = 0
    while i < filas:
        fila = []
        j = 0
        while j < columnas:
            fila.append(0)
            j = j + 1
        tablero.append(fila)
        i = i + 1

    try:
        m = int(input("Número de minas (1-24): "))
        if m < 1 or m > 24:
            raise ValueError("Número de minas fuera de rango")
    except ValueError as e:
        print("Error:", e)
        return

    minas_colocadas = 0
    while minas_colocadas < m:
        f = random.randint(0, filas-1)
        c = random.randint(0, columnas-1)
        if tablero[f][c] == 0:
            tablero[f][c] = 1
            minas_colocadas = minas_colocadas + 1

    i = 0
    while i < filas:
        j = 0
        linea = ""
        while j < columnas:
            linea = linea + str(tablero[i][j]) + " "
            j = j + 1
        print(linea)
        i = i + 1


# 9. Lista con transformaciones
def lista_transformaciones():
    try:
        n = int(input("Número de elementos > 0: "))
        if n <= 0:
            raise ValueError("Debe ser mayor que 0")
    except ValueError as e:
        print("Error:", e)
        return

    lista = []
    i = 0
    while i < n:
        lista.append(random.randint(50, 150))
        i = i + 1

    print("Lista original:", lista)

    lista_modificada = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            lista_modificada.append(lista[i] // 2)
        else:
            lista_modificada.append(lista[i] * 3)
        i = i + 1

    print("Lista modificada:", lista_modificada)


# 10. Extracción de fechas de un texto
def extraer_fechas():
    texto = input("Introduce un texto: ").strip()
    if texto == "":
        raise ValueError("Texto vacío")

    fechas = re.findall(r"\b\d\d/\d\d/\d\d\d\d\b", texto)
    hoy = datetime.today()

    i = 0
    while i < len(fechas):
        f = fechas[i]
        partes = f.split("/")
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
        fecha_obj = datetime(anio, mes, dia)
        dias_transcurridos = (hoy - fecha_obj).days
        print("{:<12} {:>5} días".format(f, dias_transcurridos))
        i = i + 1


# 11. Análisis completo de texto
def analisis_texto():
    texto = input("Introduce un texto: ").strip()
    if texto == "":
        raise ValueError("Texto vacío")

    vocales = 0
    consonantes = 0
    digitos = 0
    palabras = texto.split()

    i = 0
    while i < len(texto):
        letra = texto[i]
        if letra.lower() in "aeiou":
            vocales = vocales + 1
        elif letra.isalpha():
            consonantes = consonantes + 1
        elif letra.isdigit():
            digitos = digitos + 1
        i = i + 1

    print("{:<20} {:>5}".format("Palabras:", len(palabras)))
    print("{:<20} {:>5}".format("Vocales:", vocales))
    print("{:<20} {:>5}".format("Consonantes:", consonantes))
    print("{:<20} {:>5}".format("Dígitos:", digitos))


# 12. Validación y separación de correo electrónico
def validar_correo():
    correo = input("Introduce un correo: ").strip()
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
        raise ValueError("Correo inválido")

    partes = correo.split("@")
    usuario = partes[0]
    dominio_completo = partes[1]

    partes_dominio = dominio_completo.split(".")
    dominio = partes_dominio[0]
    extension = partes_dominio[-1]

    print("{:<15} {:>15}".format("Usuario:", usuario))
    print("{:<15} {:>15}".format("Dominio:", dominio))
    print("{:<15} {:>15}".format("Extensión:", extension))


# 13. Estadísticas de palabras y transformación
def palabras_transformacion():
    texto = input("Introduce un texto: ").strip()
    if texto == "":
        raise ValueError("Texto vacío")

    palabras = texto.split()
    palabras_invertidas = []

    i = 0
    while i < len(palabras):
        palabra = palabras[i]
        invertida = ""
        j = len(palabra) - 1
        while j >= 0:
            invertida = invertida + palabra[j]
            j = j - 1
        palabras_invertidas.append(invertida)
        i = i + 1

    mayusculas = 0
    mas5letras = 0
    i = 0
    while i < len(palabras):
        palabra = palabras[i]
        if palabra[0].isupper():
            mayusculas = mayusculas + 1
        if len(palabra) > 5:
            mas5letras = mas5letras + 1
        i = i + 1

    print("{:<20} {:>10}".format("Palabra invertida", "Longitud"))
    i = 0
    while i < len(palabras_invertidas):
        print("{:<20} {:>10}".format(palabras_invertidas[i], len(palabras[i])))
        i = i + 1

    print("Palabras que empiezan con mayúscula:", mayusculas)
    print("Palabras con más de 5 letras:", mas5letras)


# Llamadas de prueba (descomenta para ejecutar)
# numeros_pares_impares_primos()
# validar_fecha_y_edad()
# lista_muestra_aleatoria()
# validar_matricula()
# estadisticas_lista()
# contador_palindromos()
# calculadora_avanzada()
# tablero_minas()
# lista_transformaciones()
# extraer_fechas()
# analisis_texto()
# validar_correo()
# palabras_transformacion()