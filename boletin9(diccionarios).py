clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

def mostrar_clientes(dic):
    # Convertimos "Apellido, Nombre" → ("Nombre", "Apellido", edad)
    lista = []
    for clave, edad in dic.items():
        apellido, nombre = clave.split(", ")
        lista.append((nombre, apellido, edad))

    # Ordenamos por nombre
    lista.sort()

    # Mostramos
    for nombre, apellido, edad in lista:
        print(f"{nombre} {apellido} ({edad})")

mostrar_clientes(clientes)



def nuevoCliente(dic, nombre, apellido, edad):
    clave = f"{apellido}, {nombre}"

    if clave in dic:
        print("Este cliente ya existe.")
        op = input("¿Quieres sobreescribir la edad? (s/n): ")
        if op.lower() != "s":
            print("No se ha modificado.")
            return

    dic[clave] = edad
    print("Cliente añadido o actualizado.")


def cumpleCliente(dic, nombre, apellido):
    clave = f"{apellido}, {nombre}"

    if clave in dic:
        dic[clave] += 1
        print(f"Ahora {nombre} {apellido} tiene {dic[clave]} años.")
    else:
        print("Este cliente no existe.")


texto = input("Introduce tu texto: ")

palabras = texto.split()
diccionario = {}

for p in palabras:
    if p not in diccionario:
        diccionario[p] = 0
    diccionario[p] += 1

print("Diccionario:", diccionario)


frutas = {
    "Aguacate": 4.35,
    "Mandarina": 2.60,
    "Kiwi": 3.75,
    "Naranja": 1.80
}

while True:
    fruta = input("¿Qué fruta quieres comprar? ")

    if fruta.lower() == "fin":
        break

    if fruta not in frutas:
        print("Lo siento mucho pero no vendemos esa fruta")
        continue

    try:
        kilos = float(input("¿Cuántos kilos quieres? "))
        precio = kilos * frutas[fruta]
        print(f"{kilos} de {fruta} cuestan {precio:.2f} €")
    except:
        print("No has introducido bien la cantidad que quieres")
