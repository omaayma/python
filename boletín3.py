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
