#boletín 11

#ejercicio1
class Pokemon:

    tipos = [
        "Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha",
        "Veneno", "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo",
        "Bicho", "Fantasma", "Dragón"
    ]

    def __init__(self, codigo, nombre, tipo1, tipo2=None):

        self._codigo = codigo
        self._nombre = nombre
        self._tipo1 = tipo1
        self._tipo2 = tipo2
        self._evoluciona_en = None

        if not (1 <= codigo <= 151):
            raise ValueError("El código tiene que estar entre el 1 y 151.")


        if tipo1 not in self.tipos:
            raise ValueError("Tipo 1 no válido.")

        if tipo2 is not None and tipo2 not in self.tipos:
            raise ValueError("Tipo 2 no válido.")

        if tipo2 is not None and tipo1 == tipo2:
            raise ValueError("Los dos tipos no pueden ser iguales.")

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_tipo1(self):
        return self._tipo1

    def get_tipo2(self):
        return self._tipo2

    def get_evolucion(self):
        return self._evoluciona_en

    def set_evolucion(self, pokemon_evolucionado):
        self._evoluciona_en = pokemon_evolucionado

    def evolucion(self):
        if self._evoluciona_en:
            print(self._nombre,"ha evolucionado a", self._evoluciona_en.get_nombre())
            return self._evoluciona_en
        else:
            print(self._nombre, "no puede evolucionar")
            return self


P1 = Pokemon(4, "Pokemon 1", "Agua")
P2 = Pokemon(5, "Pokemon 2", "Fuego")
P3 = Pokemon(6, "Pokemon 3", "Fuego", "Volador")

print("P1:", P1._codigo, P1._nombre, P1._tipo1)
P1.set_evolucion(P2)
P2.set_evolucion(P3)

P1 = P1.evolucion()
P1 = P1.evolucion()
P1 = P1.evolucion()





#ejerccio2
class Manga:

    generos = [ "shonen", "shojo", "seinen", "josei", "kodomo",
        "yuri", "spokon", "isekai", "hentai"]

    def __init__(self, mangaka, tituloJaponés,genero,ultimoNumero, tituloEspañol=None):
        self._mangaka = mangaka
        self._tituloJaponés = tituloJaponés
        self._genero = genero.lower()
        self._ultimoNumero = ultimoNumero
        self._tituloEspañol = tituloEspañol
        self._numerosTenidos = []

        if self._genero not in self.generos:
            raise ValueError("Género no válido.")


    def get_mangaka(self):
        return self._mangaka

    def get_tituloJaponés(self):
        return self._tituloJaponés

    def get_tituloEspañol(self):
        return self._tituloEspañol

    def get_genero(self):
        return self._genero

    def get_ultimoNumero(self):
        return self._ultimoNumero

    def get_numerosTenidos(self):
        return sorted(self._numerosTenidos) #sorted para que ordene la lista que me devuelve

    def set_tituloEspañol(self, nuevoTitulo):
        self._tituloEspañol = nuevoTitulo

    def set_ultimoNumero(self, nuevoNumero):
        self._ultimoNumero = nuevoNumero


    def comprar(self, *numeros):
        for num in numeros:
            if num in self._numerosTenidos:
                print(" Ya tienes el número", num, "comprado")
            else:
                self._numerosTenidos.append(num)
                print("Número", num,"añadido")


    def numerosFaltan(self):
        faltan = []
        for i in range(1, self._ultimoNumero + 1):
            if i not in self._numerosTenidos:
                faltan.append(i)
        return faltan


    def eliminarNumero(self, num):
        if num in self._numerosTenidos:
            self._numerosTenidos.remove(num)
            print("Número", num, "eliminado.")
        else:
            print(" No tienes el número", num,"asi que no puedes eliminarlo")



m = Manga("Manga1", "MaiManga", "shonen", 108, "MiManga")

m.comprar(1, 2, 3, 5)
m.comprar(3)
m.eliminarNumero(2)
m.eliminarNumero(20)

print("Tengo:", m.get_numerosTenidos())
print("Faltan:", m.numerosFaltan())





#ejemplo clase
import random

class Pokemon:
    def __init__(self, nombre):
        self._nombre = nombre
        self._vida = random.randint(50,100)
        self._evoluciona__ = None

    def evoluciona(self, pokemon):
        self._evoluciona__ = pokemon

    def evolucion(self):
        if self._evoluciona__ is None:
            print("Este pokemon no puede evolucionar.")
            return self
        else:
            return self._evoluciona__

    def mostrar_vida(self):
        return self._vida

    def combate(self, otro):
        self._danio = random.randint(1,10)
        if self._vida <= 0:
            print("Este pokemon no puede atacar porque perdió los puntos")
        if otro._vida < 0:
            otro._vida = 0
        print(f"{self._nombre} combate con {otro._nombre} causando {self._danio} de daño.")
        if otro._vida == 0:
            print(f"{otro._nombre} ha sido derrotado")

p1 = Pokemon("P1")
p2 = Pokemon("P2")
p3 = Pokemon("P3")
p1.evoluciona(p2)
pokemonEvolu = p1.evolucion()
print(p1._nombre, "evoluciona en", pokemonEvolu._nombre)
p1.combate(p2)
p2.combate(p3)
print(p1._nombre, "tine de vida:", p1.mostrar_vida())
print(p2._nombre, "tine de vida:", p2.mostrar_vida())
print(p3._nombre, "tine de vida:", p3.mostrar_vida())





