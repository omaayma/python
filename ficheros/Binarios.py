import pickle


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostar(self):
        print(f" {self.nombre}, {self.edad}")

try:
        fichero = open("datos.bin", "wb")
        pickle.dump(Persona("Ana", 20), fichero)


except:
        print("Error al escribir")

