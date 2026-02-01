"""
#EJERICIO 1:
def compararFicheros(fich1, fich2):
    try:
        with open(fich1, "rt") as f1, open(fich2, "rt") as f2:
            contenido1 = f1.read()
            contenido2 = f2.read()

            return contenido1 == contenido2
    except:
        print("Error, el fichero no existe")
        return False

#EJERCICIO 2:

try:
    with open("estadisticas.txt", "rt") as fichero:
        lineas = fichero.readlines()

    hombres = 0
    mujeres = 0
    sumaAltura = 0
    totalPersonas = 0

    for i in range(0, len(lineas), 2):
        sexo = lineas[i].replace("\n", "")
        altura = float(lineas[i + 1].replace("\n", ""))

        if sexo == "Hombre":
            hombres += 1
        elif sexo == "Mujer":
            mujeres += 1

        sumaAltura += altura
        totalPersonas += 1

    media = sumaAltura / totalPersonas

    print("Hombres:", hombres)
    print("Mujeres:", mujeres)
    print("Estatura media:", round(media,2))

except:
    print("Error, el fichero no existe")

"""
#EJERICICO 3:
"""
def iBANValido(codigo):
    codigo = codigo.replace(" ", "")
    codigo = codigo.replace("\n", "")

    if len(codigo) != 24:
        return False
    if not codigo[0:2].isalpha():
        return False
    if not codigo[2:].isdigit():
        return False

    return True

try:
    with open("codigos.txt", "rt") as fichero:
        lineas = fichero.readlines()

    correctos = 0
    incorrectos = 0

    print("Códigos correctos en el fichero codigos.txt:")
    print()
    for linea in lineas:
        codigo = linea.replace("\n", "")

        if iBANValido(codigo):
            codigo = codigo.replace(" ", "")

            pais = codigo[0:2]
            dc = codigo[2:4]
            entidad = codigo[4:8]
            sucursal = codigo[8:12]
            dcCuenta = codigo[12:14]
            numCuenta = codigo[14:]

            print("País:", pais)
            print("DC:", dc)
            print("Entidad:", entidad)
            print("Sucursal:", sucursal)
            print("DC cuenta:", dcCuenta)
            print("Número de cuenta:", numCuenta)

            print()
            correctos += 1
        else:
            incorrectos += 1

    print("Hay", correctos, "códigos correctos y", incorrectos, "incorrectos")

except:
    print("Error, el fichero no existe")



#EJERCICIO 4:
class IBAN:
    def __init__(self, codigo):
        codigo = codigo.replace(" ", "").replace("\n","")
        self.pais = codigo[0:2]
        self.dc = codigo[2:4]
        self.entidad = codigo[4:8]
        self.sucursal = codigo[8:12]
        self.dc_cuenta = codigo[12:14]
        self.num_cuenta = codigo[14:]

    def mostrar(self):
        print("País:", self.pais)
        print("DC:", self.dc)
        print("Entidad:", self.entidad)
        print("Sucursal:", self.sucursal)
        print("DC cuenta:", self.dc_cuenta)
        print("Número de cuenta:", self.num_cuenta)
        print()

    @staticmethod
    def iBANValido(codigo):
        codigo = codigo.replace(" ", "").replace("\n", "")
        return len(codigo) == 24 and codigo[0:2].isalpha() and codigo[2:].isdigit()


try:
    with open("codigos.txt", "rt") as fichero:
        lineas = fichero.readlines()

    correctos = []
    incorrectos = 0

    for linea in lineas:
        if IBAN.iBANValido(linea):
            codigoo = IBAN(linea)
            correctos.append(codigoo)
        else:
            incorrectos += 1

    print("Códigos correctos en el fichero codigos.txt:\n")

    for codigo in correctos:
        codigo.mostrar()

    print("Hay", len(correctos), "códigos correctos y", incorrectos, "incorrectos")

except:
    print("Error, el fichero no existe")

"""
#EJERICIO5

import random

def barajar_clientes(nombre_fichero_salida):
    with open("clientes.txt", "r") as fichero:
        lineas = fichero.readlines()

    nombres = []
    apellidos = []
    dnis = []

    for linea in lineas:
        nombre, apellido, dni = linea.strip().split()
        nombres.append(nombre)
        apellidos.append(apellido)
        dnis.append(dni)

    random.shuffle(nombres)
    random.shuffle(apellidos)
    random.shuffle(dnis)

    with open(nombre_fichero_salida, "w", encoding="utf-8") as f:
        for i in range(len(nombres)):
            f.write(f"{nombres[i]} {apellidos[i]} {dnis[i]}\n")


barajar_clientes("clientes_barajados.txt")



