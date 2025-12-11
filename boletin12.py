#Ejercicio1

class AplicacionNotas:

    colores = [ "Amarillo", "Verde", "Blanco", "Cyan"]

    def __init__(self, titulo, descripción, color, fechaCreacion):
        self._titulo = titulo
        self._descripcion = descripción
        self._color = color
        self._fechaCreacion = fechaCreacion
        self._notasTenidas = []


        if color not in self.colores:
            raise ValueError("Este color no es válido")

    def get_titulo(self):
        return self._titulo

    def get_descripción(self):
        return self._descripcion

    def get_color(self):
        return self._color

    def get_fechaCreacion(self):
        return self._fechaCreacion

    def get_notasTenidas(self):
        return self._notasTenidas

    def eliminarNota(self, nota):
        if nota in self._notasTenidas:
            self._notasTenidas.remove(nota)
            print("La nota", nota, "ha sido eliminada")
        else:
            print("No tienes la nota", nota, "asi que no puedes eliminarla")





