"""
class ClaseA:
    def __init__(self):
        self._nombre = "Clase A"


    @property
    def getNombre(self):
        return self._nombre


class ClaseB(ClaseA):
    pass

objetoa = ClaseA()
objetob = ClaseB()

print(objetoa.getNombre)
print(objetob.getNombre)





class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 56 # uso nombre sin guión bajo para accederlo fácilmente


    def cambiarNombre(self, superNombre):
        self.nombre = superNombre

class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()        # llama al constructor de ClaseA
        self.subclase = "Clase B"

    def incrementoCodigo(self):
        self.codigo +=1

objetoa = ClaseA()
objetob = ClaseB()

print(objetoa.nombre)     # Clase A
print(objetob.nombre)     # Clase A (heredado de ClaseA)
print(objetob.subclase)   # Clase B


"""

class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 56 # uso nombre sin guión bajo para accederlo fácilmente

    def queSpy(self):
        print("Soy clase A")

class ClaseB:
    def __init__(self):
        self.subclase = "Clase B"

    def queSpy(self):
        print("Soy clase B")


objetoa = ClaseA()
objetob = ClaseB()
#print(objetoa.nombre)
#print(objetoa.codigo)
#print(objetob.subclase)

print(objetoa.queSpy())
print(objetob.queSpy())








