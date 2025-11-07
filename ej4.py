fraccion = input("Escribe tu fracción:")

if len(fraccion) == 3 and fraccion[2] == '/':
    numerador = fraccion[:2]
    denominador = fraccion[3:]

    if numerador.isdigit() and denominador.isdigit():
        numerador = int(numerador)
        denominador = int(denominador)


print("El valor de tu fracción es:",round((numerador/denominador),3))

