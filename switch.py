opcion = input("P para jugar, S para salir: ")
match opcion:
    case "p":
        print("Has elegido jugar")
    case "s":
        print("Has elegido salir")
    case _: #por defecto
        print("Opción no válida")
print(" ")
