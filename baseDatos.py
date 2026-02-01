import mysql.connector

# Algunos ejemplos extras de acceso a bases de datos desde python
# Usamos la base de datos pokemondb
# Por claridad, cada ejemplo está en un bloque try/excep diferente

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    sql = "SELECT nombre, peso, altura FROM pokemon WHERE peso > 200"
    cursor.execute(sql)

    for fila in cursor:
        print(fila)

    sql = "UPDATE pokemon SET peso=350 WHERE peso > 250"
    cursor.execute(sql)
    # el metodo rowcount nos devuelve, en updates y deletes, el número de filas involucradas
    # en select no lo hace con 'nonbuffered' cursors que son los que estamos viendo
    # existe la opción de usar buffered cursors, pero no los vamos a ver
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")
    # recuerda que si no ejecutamos un commit no se guardan los cambios
    # en este ejemplo está comentado y no se guardan
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)



try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    # Podemos parametrizar el select igual que con los statement de JDBC
    sql = "SELECT nombre, peso, altura FROM pokemon WHERE peso > %s AND nombre = %s"
    datos = (250,'Snorlax')
    # cada elemento de la tupla datos se sustituye en orden por el %s del query
    cursor.execute(sql, datos)

    for fila in cursor:
        print(fila)

    # También podemos lanzar múltiples querys (no válido con SELECT)
    sql = "INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
    datos = [(200, 'Pepe Potamo', 50, 30), (201, 'Inés Perado', 33, 600), (202,'Benito Camelas', 412, 30)]
    # En este caso, cada tupla se corresponde con un query diferente
    # Fíjate que usamos executemany y no execute
    cursor.executemany(sql, datos)
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")

    cursor.execute("SELECT * FROM pokemon WHERE numero_pokedex >=200")
    for fila in cursor:
        print(fila)

    # tampoco guardamos los cambios, que no queremos cargarnos una base de datos tan bonita :-)
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)



try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()
    # Activamos la posibilidad de ver los warnings
    # En este ejemplo no provocamos ninguno, así que al final no veremos nada...
    cursor.get_warnings = True

    sql = "SELECT numero_pokedex, nombre FROM pokemon where numero_pokedex <=10"
    cursor.execute(sql)
    # Con fetchmany podemos indicar cuantas filas leer
    dosFilas = cursor.fetchmany(size=2)
    # y luego leer las restantes a partir de donde nos hemos quedado
    restantes = cursor.fetchall()
    print(dosFilas)
    print(restantes)

    # volvemos a ejecutar la query
    cursor.execute(sql)
    # y ahora vamos a ver otro método de leer una a una las filas de la query
    fila = cursor.fetchone()
    # fetchone sería igual que fila =cursor.fetchmany(size=1)
    # y luego iteramos con un bucle
    while fila is not None:
        print(fila)
        fila = cursor.fetchone()

    # si hubiera warnings los veríamos aquí
    print(cursor._warnings)

    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)



#1
import mysql.connector  # Importamos el módulo para conectar con MySQL

# Conectamos con la base de datos
conexion = mysql.connector.connect(
    host="localhost",    # Servidor MySQL (localhost si es tu PC)
    user="root",         # Usuario de MySQL
    password="1234",     # Contraseña de MySQL
    database="pokemondb" # Nombre de la base de datos
)

cursor = conexion.cursor()  # Creamos un cursor para ejecutar consultas

# Ejecutamos la consulta para sacar nombres de Pokémon con altura > 1.5
cursor.execute("SELECT nombre FROM pokemons WHERE altura > 1.5")

# Guardamos todos los resultados
filas = cursor.fetchall()  # fetchall devuelve una lista de tuplas

# Mostramos los nombres
print("Pokémons con altura mayor a 1.5:")
for fila in filas:
    print(fila[0])  # Cada fila es una tupla, fila[0] es el nombre

# Cerramos el cursor y la conexión
cursor.close()
conexion.close()

#2
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pokemondb"
)

cursor = conexion.cursor()

# Consulta para actualizar nombres a mayúsculas donde el peso > 200
cursor.execute("UPDATE pokemons SET nombre = UPPER(nombre) WHERE peso > 200")

# Guardamos los cambios
conexion.commit()

# Mostramos cuántos registros fueron modificados
print("Número de registros modificados:", cursor.rowcount)

cursor.close()
conexion.close()

#3
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pokemondb"
)

cursor = conexion.cursor()

# Pedimos datos al usuario
nombre = input("Introduce el nombre del Pokémon: ")
peso = float(input("Introduce el peso del Pokémon: "))
altura = float(input("Introduce la altura del Pokémon: "))

# Buscamos el código más alto para asignar el siguiente consecutivo
cursor.execute("SELECT MAX(codigo) FROM pokemons")
ultimo = cursor.fetchone()[0]  # fetchone devuelve una tupla
nuevo_codigo = ultimo + 1  # sumamos 1 para tener el siguiente código

# Insertamos el nuevo Pokémon
cursor.execute(
    "INSERT INTO pokemons (codigo, nombre, peso, altura) VALUES (%s, %s, %s, %s)",
    (nuevo_codigo, nombre, peso, altura)
)

conexion.commit()
print("Pokémon añadido con código", nuevo_codigo)

cursor.close()
conexion.close()

#4
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pokemondb"
)

cursor = conexion.cursor()

# Pedimos datos al usuario
nombre = input("Introduce el nombre del Pokémon: ")
peso = float(input("Introduce el peso del Pokémon: "))
altura = float(input("Introduce la altura del Pokémon: "))

# Buscamos el código más alto para asignar el siguiente consecutivo
cursor.execute("SELECT MAX(codigo) FROM pokemons")
ultimo = cursor.fetchone()[0]  # fetchone devuelve una tupla
nuevo_codigo = ultimo + 1  # sumamos 1 para tener el siguiente código

# Insertamos el nuevo Pokémon
cursor.execute(
    "INSERT INTO pokemons (codigo, nombre, peso, altura) VALUES (%s, %s, %s, %s)",
    (nuevo_codigo, nombre, peso, altura)
)

conexion.commit()
print("Pokémon añadido con código", nuevo_codigo)

cursor.close()
conexion.close()



#chinook
Ejercicio 1: Listar clientes de un país

Enunciado:
Muestra todos los clientes que viven en un país concreto (por ejemplo, "USA"). Solo mostrar el nombre y el país.

import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="Chinook"
)

cursor = conexion.cursor()

pais = input("Introduce el país de los clientes a listar: ")

# Consulta SQL para obtener clientes de un país
sql = "SELECT FirstName, LastName, Country FROM Customers WHERE Country = %s"
cursor.execute(sql, (pais,))

print("\nClientes en", pais, ":")
for fila in cursor:
    print(fila[0], fila[1], "-", fila[2])

# Cerrar conexión
cursor.close()
conexion.close()

Ejercicio 2: Contar clientes por país

Enunciado:
Cuenta cuántos clientes hay en cada país y muéstralo por pantalla.

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="Chinook"
)
cursor = conexion.cursor()

# Consulta SQL para contar clientes por país
sql = "SELECT Country, COUNT(*) FROM Customers GROUP BY Country"
cursor.execute(sql)

print("Número de clientes por país:")
for fila in cursor:
    print(fila[0], ":", fila[1])

cursor.close()
conexion.close()

Ejercicio 3: Listar canciones de un álbum

Enunciado:
Dado un AlbumId, mostrar todas las canciones que pertenecen a ese álbum con su nombre y duración.

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="Chinook"
)
cursor = conexion.cursor()

album_id = input("Introduce el AlbumId: ")

sql = "SELECT Name, Milliseconds FROM Tracks WHERE AlbumId = %s"
cursor.execute(sql, (album_id,))

print("\nCanciones del álbum", album_id, ":")
for fila in cursor:
    duracion_segundos = fila[1] // 1000
    print(fila[0], "-", duracion_segundos, "segundos")

cursor.close()
conexion.close()

Ejercicio 4: Actualizar el nombre de un artista

Enunciado:
Cambia el nombre de un artista dado su ArtistId.

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="Chinook"
)
cursor = conexion.cursor()

artist_id = input("Introduce el ArtistId del artista a modificar: ")
nuevo_nombre = input("Introduce el nuevo nombre del artista: ")

sql = "UPDATE Artists SET Name = %s WHERE ArtistId = %s"
cursor.execute(sql, (nuevo_nombre, artist_id))
conexion.commit()

print("Nombre del artista actualizado correctamente.")

cursor.close()
conexion.close()

Ejercicio 5: Insertar un nuevo cliente

Enunciado:
Pide nombre, apellido, email y país, e inserta un nuevo cliente en la tabla Customers.

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="Chinook"
)
cursor = conexion.cursor()

nombre = input("Nombre: ")
apellido = input("Apellido: ")
email = input("Email: ")
pais = input("País: ")

sql = "INSERT INTO Customers (FirstName, LastName, Email, Country) VALUES (%s, %s, %s, %s)"
cursor.execute(sql, (nombre, apellido, email, pais))
conexion.commit()

print("Cliente agregado correctamente con CustomerId:", cursor.lastrowid)

cursor.close()
conexion.close()

Ejercicio 6: Eliminar un cliente por CustomerId

Enunciado:
Pide un CustomerId y elimina ese cliente de la tabla Customers.

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="Chinook"
)
cursor = conexion.cursor()

customer_id = input("Introduce el CustomerId del cliente a eliminar: ")

sql = "DELETE FROM Customers WHERE CustomerId = %s"
cursor.execute(sql, (customer_id,))
conexion.commit()

print("Cliente eliminado correctamente.")

cursor.close()
conexion.close()
