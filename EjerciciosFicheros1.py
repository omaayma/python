# =======================================================
# EJERCICIO 1 – Comparar ficheros
# =======================================================
def compararFicheros(fich1, fich2):
    try:
        fichero1 = open(fich1, "r")
        fichero2 = open(fich2, "r")

        contenido1 = fichero1.read()
        contenido2 = fichero2.read()

        fichero1.close()
        fichero2.close()

        if contenido1 == contenido2:
            return True
        else:
            return False
    except:
        print("Algún fichero no existe o hay un error")
        return False

# =======================================================
# EJERCICIO 2 – Estadísticas de altura
# =======================================================
try:
    fichero = open("estadisticas.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    hombres = 0
    mujeres = 0
    sumaAltura = 0
    totalPersonas = 0

    i = 0
    while i < len(lineas):
        sexo = lineas[i].replace("\n", "")
        altura = float(lineas[i+1].replace("\n",""))

        if sexo == "Hombre":
            hombres = hombres + 1
        elif sexo == "Mujer":
            mujeres = mujeres + 1

        sumaAltura = sumaAltura + altura
        totalPersonas = totalPersonas + 1
        i = i + 2

    media = sumaAltura / totalPersonas
    print("Hombres:", hombres)
    print("Mujeres:", mujeres)
    print("Estatura media:", round(media,2))

except:
    print("Error, no se pudo abrir el fichero")

# =======================================================
# EJERCICIO 3 – Validar IBAN
# =======================================================
def iBANValido(codigo):
    codigoLimpio = ""
    for letra in codigo:
        if letra != " " and letra != "\n":
            codigoLimpio = codigoLimpio + letra

    if len(codigoLimpio) != 24:
        return False
    if not (codigoLimpio[0].isalpha() and codigoLimpio[1].isalpha()):
        return False
    for i in range(2, 24):
        if not codigoLimpio[i].isdigit():
            return False
    return True

try:
    fichero = open("codigos.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    correctos = 0
    incorrectos = 0

    for linea in lineas:
        if iBANValido(linea):
            print("IBAN correcto:", linea)
            correctos = correctos + 1
        else:
            print("IBAN incorrecto:", linea)
            incorrectos = incorrectos + 1

    print("Códigos correctos:", correctos)
    print("Códigos incorrectos:", incorrectos)
except:
    print("Error, no se pudo abrir el fichero")

# =======================================================
# EJERCICIO 4 – Clase IBAN
# =======================================================
class IBAN:
    def __init__(self, codigo):
        codigoLimpio = ""
        for letra in codigo:
            if letra != " " and letra != "\n":
                codigoLimpio = codigoLimpio + letra

        self.pais = codigoLimpio[0:2]
        self.dc = codigoLimpio[2:4]
        self.entidad = codigoLimpio[4:8]
        self.sucursal = codigoLimpio[8:12]
        self.dcCuenta = codigoLimpio[12:14]
        self.numCuenta = codigoLimpio[14:]

    def mostrar(self):
        print("País:", self.pais)
        print("DC:", self.dc)
        print("Entidad:", self.entidad)
        print("Sucursal:", self.sucursal)
        print("DC Cuenta:", self.dcCuenta)
        print("Número de cuenta:", self.numCuenta)
        print()

try:
    fichero = open("codigos.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    for linea in lineas:
        if iBANValido(linea):
            iban = IBAN(linea)
            iban.mostrar()
except:
    print("Error al abrir el fichero")

# =======================================================
# EJERCICIO 5 – Barajar clientes
# =======================================================
import random

try:
    fichero = open("clientes.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    nombres = []
    apellidos = []
    dnis = []

    for linea in lineas:
        partes = linea.split()
        nombres.append(partes[0])
        apellidos.append(partes[1])
        dnis.append(partes[2])

    random.shuffle(nombres)
    random.shuffle(apellidos)
    random.shuffle(dnis)

    fichero_salida = open("clientes_barajados.txt", "w")
    i = 0
    while i < len(lineas):
        fichero_salida.write(nombres[i] + " " + apellidos[i] + " " + dnis[i] + "\n")
        i = i + 1
    fichero_salida.close()
except:
    print("Error con el fichero")

# =======================================================
# EJERCICIO 6 – Mostrar clientes
# =======================================================
class Cliente:
    def __init__(self, linea):
        partes = linea.split()
        self.nombre = partes[0]
        self.apellido = partes[1]
        self.nif = partes[2]

    def mostrar(self):
        print(self.nif, "-", self.apellido + ",", self.nombre)

try:
    fichero = open("clientes.txt", "r")
    for linea in fichero:
        linea = linea.replace("\n","")
        cliente = Cliente(linea)
        cliente.mostrar()
    fichero.close()
except:
    print("Error al abrir fichero")

# =======================================================
# EJERCICIO 7 – Buscar delincuente
# =======================================================
nombre_buscar = input("Introduce el nombre del ciudadano: ")
encontrado = False
edad = ""
delitos = []

try:
    fichero = open("delincuentes.txt", "r")
    for linea in fichero:
        linea = linea.replace("\n","")
        if linea[0:2] == "- ":
            delitos = []
            partes = linea[2:].split(", ")
            nombre_actual = partes[0]
            edad = partes[1]
            if nombre_actual.lower() == nombre_buscar.lower():
                encontrado = True
        else:
            if encontrado:
                delitos.append(linea)
    fichero.close()

    if encontrado and len(delitos) > 0:
        print("Edad:", edad, "años")
        print("Antecedentes penales:")
        i = 0
        while i < len(delitos):
            print(delitos[i])
            i = i + 1
    else:
        print("Sin antecedentes penales")
except:
    print("Error con el fichero")

# =======================================================
# EJERCICIO 8 – Generar personajes
# =======================================================
import random

nombres = ["Ash", "Momo", "Monkey", "Naruto", "Nico", "Ken", "Roronoa", "Touka"]
apellidos = ["Ketchum", "Ayase", "D. Luffy", "Uzumaki", "Robin", "Kaneki", "Zoro", "Kirishima"]

entrada = input("Cuantos personajes tendrá tu partida: ")

if entrada.isdigit():
    numero = int(entrada)
    if numero < 1 or numero > 8:
        print("Error")
    else:
        fichero = open("personajes.txt", "w")
        i = 0
        while i < numero:
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            nombres.remove(nombre)
            apellidos.remove(apellido)
            personaje = nombre + " " + apellido
            print(personaje)
            fichero.write(personaje + "\n")
            i = i + 1
        fichero.close()
else:
    print("Error")

# =======================================================
# EJERCICIO 9 – Alumnos aprobados
# =======================================================
try:
    fichero = open("alumnos.txt", "r")
    for linea in fichero:
        linea = linea.replace("\n","")
        partes = linea.split(": ")
        nombre_completo = partes[0]
        notas = partes[1].split(", ")

        suma = 0
        aprobado = True
        i = 0
        while i < len(notas):
            nota = float(notas[i])
            suma = suma + nota
            if nota < 5:
                aprobado = False
            i = i + 1

        if aprobado:
            media = suma / len(notas)
            media = round(media,1)
            apellido, nombre = nombre_completo.split(", ")
            print(nombre, apellido, "-", media)
    fichero.close()
except:
    print("Error con el fichero")

# =======================================================
# EJERCICIO 10 – Redes por clase
# =======================================================
clase_a = []
clase_b = []
clase_c = []

try:
    fichero = open("redes.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    i = 0
    while i < len(lineas):
        linea = lineas[i].replace("\n","")
        if linea.endswith("/8"):
            clase_a.append(linea)
        elif linea.endswith("/16"):
            clase_b.append(linea)
        elif linea.endswith("/24"):
            clase_c.append(linea)
        i = i + 1

    print("Redes Clase A:")
    i = 0
    while i < len(clase_a):
        print(clase_a[i])
        i = i + 1

    print("Redes Clase B:")
    i = 0
    while i < len(clase_b):
        print(clase_b[i])
        i = i + 1

    print("Redes Clase C:")
    i = 0
    while i < len(clase_c):
        print(clase_c[i])
        i = i + 1
except:
    print("Error al abrir fichero")

# =======================================================
# EJERCICIO 11 – Analizar fichero de números
# =======================================================
def analizar_fichero(nombre):
    validos = 0
    invalidos = 0
    numeros = []

    try:
        fichero = open(nombre, "r")
        lineas = fichero.readlines()
        fichero.close()

        i = 0
        while i < len(lineas):
            linea = lineas[i].replace("\n","")
            try:
                numero = float(linea)
                numeros.append(numero)
                validos = validos + 1
            except:
                invalidos = invalidos + 1
            i = i + 1

        print("Número de datos válidos:", validos)
        print("Número de datos inválidos:", invalidos)
        if validos > 0:
            print("Mínimo:", min(numeros))
            print("Máximo:", max(numeros))
            print("Media aritmética:", round(sum(numeros)/len(numeros),3))
    except:
        print("Error al abrir fichero")

# =======================================================
# EJERCICIO 12 – Corregir respuestas
# =======================================================
try:
    # Leer soluciones
    fichero_s = open("soluciones.txt", "r")
    linea_s = fichero_s.readline()
    fichero_s.close()

    linea_s = linea_s.replace("\n","")
    soluciones = linea_s.split(", ")

    # Leer respuestas alumnos
    fichero_r = open("respuestas.txt", "r")
    lineas_r = fichero_r.readlines()
    fichero_r.close()

    i = 0
    while i < len(lineas_r):
        linea = lineas_r[i].replace("\n","")
        if ": " in linea:
            partes = linea.split(": ")
            nombre = partes[0]
            respuestas = partes[1].split(", ")

            if len(respuestas) == len(soluciones):
                nota = 0
                j = 0
                while j < len(soluciones):
                    if respuestas[j] == soluciones[j]:
                        nota = nota + 1
                    else:
                        nota = nota - 0.2
                    j = j + 1
                print(nombre + ": " + str(round(nota,2)))
        i = i + 1
except:
    print("Error con los ficheros")

# =======================================================
# EJERCICIO 13 – Login sencillo
# =======================================================
usuario = input("Introduce el usuario: ")
contrasena = input("Introduce la contraseña: ")

try:
    fichero = open("login.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    encontrado = False
    i = 0
    while i < len(lineas):
        linea = lineas[i].replace("\n","")
        partes = linea.split(":")
        if partes[0] == usuario:
            encontrado = True
            if partes[1] == contrasena:
                print("Login correcto")
            else:
                print("Contraseña incorrecta")
            break
        i = i + 1

    if not encontrado:
        print("Usuario no encontrado")
except:
    print("No se puede acceder al fichero")

# =======================================================
# EJERCICIO 14 – Registrar usuario
# =======================================================
usuario = input("Introduce el nombre del usuario: ")
contrasena1 = input("Introduce la contraseña: ")
contrasena2 = input("Vuelve a introducir la contraseña: ")

if contrasena1 != contrasena2:
    print("Las contraseñas no coinciden. No se puede grabar")
else:
    try:
        fichero = open("login.txt", "a")
        fichero.write(usuario + ":" + contrasena1 + "\n")
        fichero.close()
        print("Cuenta grabada correctamente")
    except:
        print("Error al escribir el fichero")

# =======================================================
# EJERCICIO 15 – Clase Usuario y fortaleza
# =======================================================
class Usuario:
    def __init__(self, linea):
        partes = linea.split(":")
        self.usuario = partes[0]
        self.password = partes[1]

    def fortaleza(self):
        fuerza = 0
        if len(self.password) > 8:
            fuerza = fuerza + 1

        letras = False
        mayus = False
        minus = False
        numeros = False
        otros = False

        i = 0
        while i < len(self.password):
            c = self.password[i]
            if c.isalpha():
                letras = True
                if c.isupper():
                    mayus = True
                else:
                    minus = True
            elif c.isdigit():
                numeros = True
            else:
                otros = True
            i = i + 1

        if letras:
            fuerza = fuerza + 1
        if mayus and minus:
            fuerza = fuerza + 1
        if numeros:
            fuerza = fuerza + 1
        if otros:
            fuerza = fuerza + 1

        print("Usuario:", self.usuario)
        print("Password:", self.password)
        print("Fortaleza:", fuerza)

# =======================================================
# EJERCICIO 16 – Guardar y leer usuarios en binario
# =======================================================
import pickle

u1 = Usuario("josemaria:abc123")
u2 = Usuario("alberto:M4d4g4scar+")

usuarios = [u1,u2]

try:
    fichero = open("login.bin", "wb")
    pickle.dump(usuarios,fichero)
    fichero.close()
except:
    print("Error al escribir el fichero binario")

try:
    fichero = open("login.bin", "rb")
    lista = pickle.load(fichero)
    fichero.close()

    i = 0
    while i < len(lista):
        lista[i].fortaleza()
        i = i + 1
except:
    print("Error al leer fichero binario")

# =======================================================
# EJERCICIO 17 – Validar empleados
# =======================================================
try:
    fichero = open("origen.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    fichero_dest = open("salida.txt", "w")
    i = 0
    while i < len(lineas):
        linea = lineas[i].replace("\n","")
        partes = linea.split(";")
        if len(partes) == 3:
            if ", " in partes[0]:
                try:
                    float(partes[2])
                    fichero_dest.write(linea + "\n")
                except:
                    print("Salario incorrecto:", linea)
            else:
                print("Nombre incorrecto:", linea)
        else:
            print("Línea incorrecta:", linea)
        i = i + 1
    fichero_dest.close()
except:
    print("Error al abrir fichero")

# =======================================================
# EJERCICIO 18 – Pedir edad y guardar
# =======================================================
try:
    fichero = open("empleados.txt", "r")
    lineas = fichero.readlines()
    fichero.close()

    nuevas_lineas = []
    i = 0
    while i < len(lineas):
        linea = lineas[i].replace("\n","")
        partes = linea.split(";")
        nombre_completo = partes[0]
        nombre, apellido = nombre_completo.split(", ")

        edad = 0
        while True:
            edad_input = input(nombre + " " + apellido + ". Edad: ")
            if edad_input.isdigit():
                edad = int(edad_input)
                if edad >= 18 and edad <= 66:
                    break
            print("Edad incorrecta")

        nueva_linea = linea + ";" + str(edad)
        nuevas_lineas.append(nueva_linea)
        i = i + 1

    fichero = open("empleados.txt", "w")
    i = 0
    while i < len(nuevas_lineas):
        fichero.write(nuevas_lineas[i] + "\n")
        i = i + 1
    fichero.close()
except:
    print("Error con el fichero")

# =======================================================
# EJERCICIO 19 – Clase Empleado
# =======================================================
class Empleado:
    def __init__(self, linea):
        partes = linea.split(";")
        apellidos, nombre = partes[0].split(", ")
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = partes[1]
        self.salario = float(partes[2])
        self.edad = int(partes[3])

    def mostrar(self):
        print("Empleado:", self.nombre, self.apellidos)
        print("Cargo:", self.cargo)
        print("Años hasta jubilación:", 67 - self.edad)
        print("Salario neto anual:", round(self.salario * 14,2))

# =======================================================
# EJERCICIO 20 – Guardar empleados en binario
# =======================================================
def grabarEmpleado(fichero_binario, empleado):
    try:
        try:
            f = open(fichero_binario, "rb")
            lista = pickle.load(f)
            f.close()
        except:
            lista = []

        lista.append(empleado)

        f = open(fichero_binario, "wb")
        pickle.dump(lista,f)
        f.close()

        i = 0
        while i < len(lista):
            print(lista[i].nombre, lista[i].apellidos, "(", lista[i].edad, ")")
            i = i + 1
    except:
        print("Error con el fichero binario")

# =======================================================
# EJERCICIO 21 – Pokémon correctos
# =======================================================
entrada = "pokemon_in.txt"
salida = "pokemon_out.txt"

try:
    f = open(entrada,"r")
    lineas = f.readlines()
    f.close()

    f_out = open(salida,"w")
    total_correctos = 0

    i = 0
    while i < len(lineas):
        linea = lineas[i].replace("\n","")
        pokemons = linea.split("; ")
        correcto = True
        j = 0
        while j < len(pokemons):
            partes = pokemons[j].split(" ")
            if len(partes) < 2:
                correcto = False
            else:
                try:
                    numero = int(partes[0])
                    if numero < 1 or numero > 151:
                        correcto = False
                except:
                    correcto = False
            j = j + 1

        if correcto:
            total_correctos = total_correctos + len(pokemons)
            f_out.write(linea + "\n")
        else:
            print("Línea erronea:", linea)
        i = i + 1
    f_out.close()
    print("Se grabaron", total_correctos, "pokemons")
except:
    print("Error con el fichero")

# =======================================================
# EJERCICIO 22 – Consultar Pokedex
# =======================================================
pokedex = {}
try:
    f = open(salida,"r")
    lineas = f.readlines()
    f.close()

    i = 0
    while i < len(lineas):
        linea = lineas[i].replace("\n","")
        pokemons = linea.split("; ")
        j = 0
        while j < len(pokemons):
            partes = pokemons[j].split(" ")
            numero = int(partes[0])
            nombre = ""
            k = 1
            while k < len(partes):
                nombre = nombre + partes[k] + " "
                k = k + 1
            nombre = nombre[:-1]  # quitar último espacio
            pokedex[numero] = nombre
            pokedex[nombre.lower()] = numero
            j = j + 1
        i = i + 1

    while True:
        consulta = input("Introduce Pokémon (exit para salir): ")
        if consulta.lower() == "exit":
            print("Gracias por consultar")
            break
        if consulta.isdigit():
            num = int(consulta)
            if num in pokedex:
                print(pokedex[num], "- número", num)
            else:
                print("No encontrado")
        else:
            if consulta.lower() in pokedex:
                print(consulta, "- número", pokedex[consulta.lower()])
            else:
                print("No encontrado")
except:
    print("Error con el fichero")

# =======================================================
# EJERCICIO 23 – Clase Pokémon
# =======================================================
class Pokemon:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre
        self.evoluciona_a = None
        self.evoluciona_de = None
        self.tipos = []

    def evoluciona(self, otro):
        self.evoluciona_a = otro
        otro.evoluciona_de = self

    def tipo(self, tipo):
        self.tipos.append(tipo)

    def mostrar(self):
        print(self.numero, self.nombre, end=" ")
        if self.evoluciona_de:
            print("- Evoluciona de", self.evoluciona_de.nombre, end=" ")
        else:
            print("- No se conoce de dónde evoluciona", end=" ")
        if self.evoluciona_a:
            print("- Evoluciona en", self.evoluciona_a.nombre, end=" ")
        else:
            print("- No se conoce a dónde evoluciona", end=" ")
        print("- Tipos:", self.tipos)

# =======================================================
# EJERCICIO 24 – Guardar y combate Pokémon
# =======================================================
import random

fichero = "opciones.bin"

def grabarFichero(fichero, pokemons):
    try:
        try:
            f = open(fichero,"rb")
            lista = pickle.load(f)
            f.close()
        except:
            lista = []

        i = 0
        while i < len(pokemons):
            lista.append(pokemons[i])
            i = i + 1

        f = open(fichero,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar fichero")

def combate(fichero):
    try:
        f = open(fichero,"rb")
        lista = pickle.load(f)
        f.close()

        if len(lista) < 4:
            print("No hay suficientes pokemons")
            return

        seleccion = []
        i = 0
        while len(seleccion) < 4:
            num = random.randint(0,len(lista)-1)
            if lista[num] not in seleccion:
                seleccion.append(lista[num])

        print("Jugador 1:", seleccion[0].nombre, "y", seleccion[1].nombre)
        print("Jugador 2:", seleccion[2].nombre, "y", seleccion[3].nombre)
    except:
        print("Error con el fichero o contenido")
