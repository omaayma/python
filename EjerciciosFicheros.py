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


#EJERICIO5

import random

def barajar_clientes(fichero_salida):
    # Leer el fichero original
    with open("clientes.txt", "r") as f:
        lineas = f.readlines()

    nombres = []
    apellidos = []
    dnis = []

    # Separar nombres, apellidos y DNIs
    for linea in lineas:
        nombre, apellido, dni = linea.split()
        nombres.append(nombre)
        apellidos.append(apellido)
        dnis.append(dni)

    # Mezclar cada lista
    random.shuffle(nombres)
    random.shuffle(apellidos)
    random.shuffle(dnis)

    # Crear nuevas combinaciones y escribir en fichero de salida
    with open(fichero_salida, "w") as f:
        for i in range(len(lineas)):
            f.write(f"{nombres[i]} {apellidos[i]} {dnis[i]}\n")

# Llamada de ejemplo
barajar_clientes("clientes_barajados.txt")

#ejercicio6
class Cliente:
    def __init__(self, linea):
        # Recibimos una línea "Nombre Apellido DNI"
        partes = linea.split()
        self.nombre = partes[0]
        self.apellido = partes[1]
        self.nif = partes[2]

    def mostrar(self):
        print(f"{self.nif} – {self.apellido}, {self.nombre}")

# Leer fichero y mostrar clientes
with open("clientes.txt", "r") as f:
    for linea in f:
        cliente = Cliente(linea.strip())
        cliente.mostrar()


#ejericicio7

nombre_buscar = input("Introduce el nombre del ciudadano: ")

encontrado = False
edad = ""
delitos = []

with open("delincuentes.txt", "r") as fichero:
    for linea in fichero:
        linea = linea.strip()

        if linea.startswith("- "):
            # Nueva persona
            delitos = []
            datos = linea[2:]          # quitamos "- "
            partes = datos.split(", ")
            nombre_actual = partes[0]
            edad = partes[1]

            if nombre_actual.lower() == nombre_buscar.lower():
                encontrado = True

        else:
            # Línea de delito
            if encontrado:
                delitos.append(linea)

# Mostrar resultado
if len(delitos) > 0:
    print("Edad:", edad, "años")
    print("Antecedentes penales:")
    for d in delitos:
        print(d)
else:
    print("Sin antecedentes penales")
"""
#ejericico8

import random

nombres = ["Ash", "Momo", "Monkey", "Naruto", "Nico", "Ken", "Roronoa", "Touka"]
apellidos = ["Ketchum", "Ayase", "D. Luffy", "Uzumaki", "Robin", "Kaneki", "Zoro", "Kirishima"]

entrada = input("Cuantos personajes tendrá tu partida: ")

if not entrada.isdigit():
    print("Error")
else:
    numero = int(entrada)

    if numero < 1 or numero > 8:
        print("Error")
    else:
        print("Personajes:")

        with open("personajes.txt", "w") as fichero:
            for i in range(numero):
                nombre = random.choice(nombres)
                apellido = random.choice(apellidos)

                nombres.remove(nombre)
                apellidos.remove(apellido)

                personaje = nombre + " " + apellido
                print(personaje)
                fichero.write(personaje + "\n")

#ejericio9
with open("alumnos.txt", "r") as fichero:
    for linea in fichero:
        linea = linea.strip()
        partes = linea.split(": ")

        nombre_completo = partes[0]
        notas_texto = partes[1].split(", ")

        aprobado = True
        suma = 0

        for nota in notas_texto:
            valor = float(nota)
            suma += valor
            if valor < 5:
                aprobado = False

        if aprobado:
            media = suma / len(notas_texto)
            media = round(media, 1)

            apellido, nombre = nombre_completo.split(", ")
            print(nombre, apellido, "–", media)


#ejericio 10
clase_a = []
clase_b = []
clase_c = []

with open("redes.txt", "r") as fichero:
    for linea in fichero:
        linea = linea.strip()

        if linea.endswith("/8"):
            clase_a.append(linea)
        elif linea.endswith("/16"):
            clase_b.append(linea)
        elif linea.endswith("/24"):
            clase_c.append(linea)

print("Redes Clase A:")
for r in clase_a:
    print(r)

print("Redes Clase B:")
for r in clase_b:
    print(r)

print("Redes Clase C:")
for r in clase_c:
    print(r)


#ejericio 11
def analizar_fichero(nombre):
    validos = 0
    invalidos = 0
    numeros = []

    try:
        with open(nombre, "r") as fichero:
            for linea in fichero:
                linea = linea.strip()
                try:
                    numero = float(linea)
                    numeros.append(numero)
                    validos += 1
                except:
                    invalidos += 1

        print("Número de datos válidos:", validos)
        print("Número de datos inválidos:", invalidos)
        print("Mínimo:", min(numeros))
        print("Máximo:", max(numeros))
        print("Media aritmética:", round(sum(numeros) / len(numeros), 3))

    except:
        print("Error al leer el fichero")

#ejericio 12
# Abrir el fichero con las soluciones
try:
    fichero_s = open("soluciones.txt", "r")
    linea_s = fichero_s.readline()
    fichero_s.close()
    linea_s = linea_s.strip()  # quitar salto de línea
    soluciones = linea_s.split(", ")
except:
    print("Fichero de soluciones no encontrado o formato incorrecto")
    exit()

# Abrir el fichero con las respuestas de los alumnos
try:
    fichero_r = open("respuestas.txt", "r")
    lineas_r = fichero_r.readlines()
    fichero_r.close()
except:
    print("Fichero de respuestas no encontrado")
    exit()

# Procesar cada alumno
for linea in lineas_r:
    linea = linea.strip()
    if ": " not in linea:
        continue  # línea incorrecta, se ignora

    partes = linea.split(": ")
    nombre = partes[0]
    resp_texto = partes[1]

    respuestas = resp_texto.split(", ")
    if len(respuestas) != len(soluciones):
        continue  # ignorar líneas con número incorrecto de respuestas

    # Calcular nota
    nota = 0
    for i in range(len(soluciones)):
        if respuestas[i] == soluciones[i]:
            nota += 1
        else:
            nota -= 0.2

    # Mostrar con dos decimales
    print(nombre + ": " + str(round(nota,2)))


#ejericio 13
fichero = "login.txt"

usuario = input("Introduce el usuario: ")
contrasena = input("Introduce la contraseña: ")

try:
    f = open(fichero, "r")
    lineas = f.readlines()
    f.close()

    if len(lineas) == 0:
        print("Fichero vacío")
    else:
        encontrado = False
        for linea in lineas:
            linea = linea.strip()
            partes = linea.split(":")
            usuario_arch = partes[0]
            contrasena_arch = partes[1]

            if usuario_arch == usuario:
                encontrado = True
                if contrasena_arch == contrasena:
                    print("Login correcto")
                else:
                    print("Contraseña incorrecta")
                break

        if not encontrado:
            print("Usuario no encontrado")
except:
    print("No se puede acceder al fichero")

#14
fichero = "login.txt"

usuario = input("Introduce el nombre del usuario: ")
contrasena1 = input("Introduce la contraseña: ")
contrasena2 = input("Vuelve a introducir la contraseña de nuevo: ")

if contrasena1 != contrasena2:
    print("Las contraseñas no son iguales. No se puede grabar la nueva cuenta")
else:
    try:
        f = open(fichero, "a")  # abrir para añadir
        f.write(usuario + ":" + contrasena1 + "\n")
        f.close()
        print("Cuenta de usuario grabada correctamente")
    except:
        print("No se puede escribir en el fichero")

#15
class Usuario:
    def __init__(self, linea):
        partes = linea.strip().split(":")
        self.usuario = partes[0]
        self.password = partes[1]

    def fortaleza(self):
        fuerza = 0
        # Más de 8 caracteres
        if len(self.password) > 8:
            fuerza += 1
        # Contiene letras
        contiene_letras = False
        contiene_mayus = False
        contiene_minus = False
        contiene_numeros = False
        contiene_otros = False
        for c in self.password:
            if c.isalpha():
                contiene_letras = True
                if c.isupper():
                    contiene_mayus = True
                else:
                    contiene_minus = True
            elif c.isdigit():
                contiene_numeros = True
            else:
                contiene_otros = True

        if contiene_letras:
            fuerza += 1
        if contiene_mayus and contiene_minus:
            fuerza += 1
        if contiene_numeros:
            fuerza += 1
        if contiene_otros:
            fuerza += 1

        print("Usuario:", self.usuario)
        print("Password:", self.password)
        print("Fortaleza de la contraseña:", fuerza)

#16
import pickle

# Crear usuarios
u1 = Usuario("josemaria:abc123")
u2 = Usuario("alberto:M4d4g4scar+")

usuarios = [u1, u2]

# Guardar en binario
try:
    f = open("login.bin", "wb")
    pickle.dump(usuarios, f)
    f.close()
except:
    print("Error al escribir el fichero binario")

# Leer y mostrar
try:
    f = open("login.bin", "rb")
    lista = pickle.load(f)
    f.close()

    print("Número de cuentas encontradas:", len(lista))
    print("Listado de cuentas:")
    for u in lista:
        u.fortaleza()
except:
    print("Error al leer el fichero binario")

#17
origen = "origen.txt"
destino = "salida.txt"

try:
    f = open(origen, "r")
    lineas = f.readlines()
    f.close()

    f_dest = open(destino, "w")
    for linea in lineas:
        linea = linea.strip()
        partes = linea.split(";")
        if len(partes) != 3:
            print("Línea errónea:", linea)
            continue

        nombre_apellido = partes[0]
        cargo = partes[1]
        salario = partes[2]

        if "," not in nombre_apellido:
            print("Línea errónea:", linea)
            continue

        nombre, apellido = nombre_apellido.split(", ")

        try:
            float(salario)
        except:
            print("Línea errónea:", linea)
            continue

        # Línea correcta
        f_dest.write(linea + "\n")
    f_dest.close()
except:
    print("Error al abrir fichero")

#18
fichero = "empleados.txt"

try:
    f = open(fichero, "r")
    lineas = f.readlines()
    f.close()

    nuevas_lineas = []
    for linea in lineas:
        linea = linea.strip()
        partes = linea.split(";")
        nombre_completo = partes[0]
        partes_nombre = nombre_completo.split(", ")
        # Mostrar nombre completo invertido
        mostrar_nombre = partes_nombre[1] + " " + partes_nombre[0]

        edad = 0
        while True:
            edad_input = input(mostrar_nombre + ". ¿Cuál es su edad? ")
            if edad_input.isdigit():
                edad = int(edad_input)
                if edad >= 18 and edad <= 66:
                    break
            print("Edad incorrecta, intente de nuevo")

        nueva_linea = linea + ";" + str(edad)
        nuevas_lineas.append(nueva_linea)

    # Guardar cambios
    f = open(fichero, "w")
    for l in nuevas_lineas:
        f.write(l + "\n")
    f.close()
except:
    print("Error con el fichero")

#19
class Empleado:
    def __init__(self, linea):
        partes = linea.strip().split(";")
        apellidos, nombre = partes[0].split(", ")
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = partes[1]
        self.salario = float(partes[2])
        self.edad = int(partes[3])

    def mostrar(self):
        print("Empleado:", self.nombre, self.apellidos)
        print("Cargo:", self.cargo)
        años_jubilacion = 67 - self.edad
        print("Años hasta su jubilación ordinaria:", años_jubilacion)
        salario_anual = self.salario * 14
        print("Salario neto anual:", round(salario_anual,2))


#20
import pickle

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
        pickle.dump(lista, f)
        f.close()

        # Mostrar todos los empleados
        for e in lista:
            print(e.nombre, e.apellidos, "(", e.edad, ")")

    except:
        print("Error al manejar el fichero binario")

# Ejemplo de uso
# e1 = Empleado("Imedio, Demetrio;Programador;1599.56;34")
# grabarEmpleado("empleados.bin", e1)

#21
entrada = "pokemon_in.txt"
salida = "pokemon_out.txt"

try:
    f = open(entrada, "r")
    lineas = f.readlines()
    f.close()

    f_out = open(salida, "w")
    total_correctos = 0

    for linea in lineas:
        linea = linea.strip()
        pokemons = linea.split("; ")
        correcto = True
        for p in pokemons:
            partes = p.split(" ")
            if len(partes) < 2:
                correcto = False
                break
            try:
                numero = int(partes[0])
                if numero < 1 or numero > 151:
                    correcto = False
            except:
                correcto = False
        if correcto:
            total_correctos += len(pokemons)
            f_out.write(linea + "\n")
        else:
            print("Línea erronea detectada:", linea)
            print("El número de la pokedex no es de la primera generación")

    f_out.close()
    print("Se han grabado", total_correctos, "pokemons correctos en el fichero de salida")
except:
    print("Error con el fichero")

#22
fichero = salida

# Leer fichero y guardar información
pokedex = {}
try:
    f = open(fichero, "r")
    lineas = f.readlines()
    f.close()

    for linea in lineas:
        linea = linea.strip()
        pokemons = linea.split("; ")
        for p in pokemons:
            partes = p.split(" ")
            numero = int(partes[0])
            nombre = " ".join(partes[1:])
            pokedex[numero] = nombre
            pokedex[nombre.lower()] = numero

    while True:
        consulta = input("Introduce el pokemon en el que estás interesado: ")
        if consulta.lower() == "exit":
            print("Gracias por consultar la pokedex")
            break

        if consulta.isdigit():
            num = int(consulta)
            if num in pokedex:
                nombre = pokedex[num]
                print(nombre + ". Su número de la Pokedex es el", num)
                # Evoluciones simplificadas
                print("No evoluciona de ningún otro. No evoluciona a ningún otro")
            else:
                print("Ese Pokemon no está registrado en la pokedex")
        else:
            if consulta.lower() in pokedex:
                num = pokedex[consulta.lower()]
                print(consulta + ". Su número de la Pokedex es el", num)
                print("No evoluciona de ningún otro. No evoluciona a ningún otro")
            else:
                print("Eso no parece corresponder a un nombre de pokemon o código de la pokedex")
except:
    print("Error con el fichero")


#23
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
        print(f"{self.numero}. {self.nombre}", end="")
        if self.evoluciona_de:
            print("- Evoluciona de", self.evoluciona_de.nombre, end="")
        else:
            print("- No se conoce de donde evoluciona", end="")
        if self.evoluciona_a:
            print("- Evoluciona en", self.evoluciona_a.nombre, end="")
        else:
            print("- No se conoce a donde evoluciona", end="")
        print("- Tipos:", ", ".join(self.tipos))

#24
import pickle
import random

fichero = "opciones.bin"

def grabarFichero(fichero, *pokemons):
    try:
        try:
            f = open(fichero, "rb")
            lista = pickle.load(f)
            f.close()
        except:
            lista = []

        for p in pokemons:
            lista.append(p)

        f = open(fichero, "wb")
        pickle.dump(lista, f)
        f.close()
    except:
        print("Error al grabar fichero")

def combate(fichero):
    try:
        f = open(fichero, "rb")
        lista = pickle.load(f)
        f.close()

        if len(lista) < 4:
            print("No hay suficientes pokemons")
            return

        seleccion = random.sample(lista, 4)
        print("El jugador 1 combate con", seleccion[0].nombre, "y", seleccion[1].nombre)
        print("El jugador 2 combate con", seleccion[2].nombre, "y", seleccion[3].nombre)
    except:
        print("Error con el fichero o contenido no válido")
