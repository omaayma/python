""" class Perro:

    def __init__(self, secreto, secretisimo, nombre="dooby"):
        self.nombre = nombre;
        self._secreto = secreto;
        self.__secretisimo = secretisimo;

    def llamar(self):
        return "El nombre es " + self.nombre

mascota1 = Perro()
print(mascota1.llamar())

#mascota2 = Perro("Suly")
#print(mascota2.llamar())

mascota2._secreto = " es negra";



mascota1.nombre="Nuevo"
print(mascota1.llamar())

"""

class Perro:
    numPerro = 0

    def __init__(self,nombre="dooby"):
        self.nombre = nombre
        Perro.numPerro = 0

    def llamar(self):
        return "El nombre es " + self.nombre

    @classmethod
    def cuantosPerros(sls):
        return sls.numPerro

   """ @classmethod
    def ladrar ():
    return"guau""""

   def sobreCargada2(self, atributo):
       if(len(atributo)==2):
           print("Recibo un parámetro");
        elif


def



""" script en python desde consola"""





mascota1 = Perro("dooby")
mascota2 = Perro()
mascota3 = Perro("lubyy")

print(mascota3.cuantosPerros())
print(mascota1.cuantosPerros())
print(mascota1.ladrar())

#POO





