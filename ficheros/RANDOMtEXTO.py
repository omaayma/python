try:
    with open("quijote.txt", "r+") as fichero:

        fichero.seek(0)
        print("Inicio del archivo:")
        print(fichero.read(10))

        fichero.seek(100)
        print("\nDesde la posición 100:")
        print(fichero.read(100))

        print("\nPosición:", fichero.tell())

except:
    print("Error al leer el archivo")
