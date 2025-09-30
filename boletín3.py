"""
#Ejercicio1

while True:
    contraseña1 = input("Introduce la contraseña: ")
    contraseña2 = input("Repite la contraseña: ")
    if contraseña1== contraseña2:
        print("Las contraseñas coinciden")
        break
    else:
        print("Las contraseñas no coinciden")

#Ejercicio2

intentosInvalidos = 0

while True:
    contraseña1 = input("Introduce la contraseña: ")
    contraseña2 = input("Repite la contraseña: ")
    if contraseña1 == contraseña2:
        print(f"Contraseñas coinciden. Intentos inválidos: ", intentosInvalidos)
        break
    else:
        print("Las contraseñas no coinciden")
        intentosInvalidos += 1



#Ejercicio3

nombre = input("Introduce tu nombre: ")
apellidos = input("Introduce tus apellidos: ")

# apellidos separadas por espacio
apellidosTotal = apellidos.split()

if len(apellidosTotal) >= 2:
    apellido1 = apellidosTotal[-2]
    apellido2 = apellidosTotal[-1]
    resultado = (apellido1 + " "+ apellido2 + " ") + ", "+ nombre
else:
    print("Introduce tu nombre y apellidos")

print(resultado)


#Ejercicio4
cadenaTexto = input("Introduce una cadena de texto:")
sinEspacios= cadenaTexto.replace(" ", "")
numEspacios= cadenaTexto.count(" ")

print("La cadena sin espacios es :" + sinEspacios)
print("El número de espacios que hay en la cadena son:" + str(numEspacios))


#Ejercicio5

cadena = input("Introduce una cadena de texto: ")
print(cadena[::-1])


#Ejercicio6
cadena = input("Introduce una cadena: ")

pares = cadena[0::2]
impares = cadena[1::2]

print("Letras en posición par: ", pares)
print("Letras en posición impar: ", impares)


#Ejercicio7

cadena = input("Introduce una cadena: ")
sustituciones = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 
                 'A':'4', 'E':'3', 'I':'1', 'O':'0'}
resultado = ""

for c in cadena:
    if c in sustituciones:
        resultado += sustituciones[c]
    else:
        resultado += c
print(resultado)


#Ejercicio8
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
resultado = ""

for c in cadena:
    if c not in vocales:
        resultado += c
print(resultado)


#Ejercicio9

destino = input("Elige un destino (Francia, Italia, Chile, Japón): ")
match destino:
    case "Francia":
        print("La capital es París")
    case "Italia":
        print("La capital es Roma")
    case "Chile":
        print("La capital es Santiago de Chile")
    case "Japón":
        print("La capital es Tokio")
    case _:
        print("Destino no válido")


#Ejercicio10
nif = input("Introduce un NIF: ")
letra = nif[8]

esLetra = (letra >= 'A' and letra <= 'Z') or (letra >= 'a' and letra <= 'z')

if len(nif) == 9 and nif[:8].isdigit() and esLetra:
    print("NIF correcto")
else:
    print("NIF incorrecto")



#Ejercicio11

nie = input("Introduce un NIF o NIE: ")

if len(nie) == 9 and ('A' <= nie[-1] <= 'Z'):
    if nie[0] in "XYZ":
        if nie[1:8].isdigit():
            print("NIE válido")
        else:
            print("NIE incorrecto")
    else:
        if nie[:8].isdigit():
            print("NIF válido")
        else:
            print("NIF incorrecto")
else:
    print("Formato incorrecto")


#Ejercicio12

matricula = input("Introduce matrícula: ")
letrasValidas = "BCDFGHJKLMNPRSTVWXYZ"

if len(matricula) == 7:
    numeros = matricula[:4]
    letras = matricula[4:]

    if numeros.isdigit():
        valido = True
        for c in letras:
            if c not in letrasValidas:
                valido = False
                break
        if valido:
            print("Matrícula válida")
        else:
            print("Matrícula no válida")
    else:
        print("Matrícula no válida")
else:
    print("Longitud incorrecta")

"""
#Ejercicio13
matricula = input("Introduce matrícula: ")
letrasValidas = "BCDFGHJKLMNPRSTVWXYZ"

if len(matricula) == 8 and (matricula[4] == ' ' or matricula[4] == '-'):
    matricula = matricula[:4] + matricula[5:]


if len(matricula) == 7:
    numeros = matricula[:4]
    letras = matricula[4:]

    if numeros.isdigit():
        valido = True
        for c in letras:
            if c not in letrasValidas:
                valido = False
                break
        if valido:
            print("Matrícula válida")
        else:
            print("Matrícula no válida")
    else:
        print("Matrícula no válida")
else:
    print("Longitud incorrecta")

