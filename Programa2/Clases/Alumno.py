from datetime import date


class Alumno(object):
    nombre = ""

    apellido = ""

    fecha = None

    listanotas = []

    def setNombre(self, n):
        self.nombre = str(n)

    def setApellido(self, t):
        self.apellido = str(t)

    def setFecha(self, a, b, c):
        self.fecha = date(int(a), int(b), int(c))

    def addNota(self, nota):
        self.listanotas.append(nota)

    def minNota(self):
        return min(self.listanotas)

    def maxNota(self):
        return max(self.listanotas)

    def promedio(self):
        return sum(self.listanotas) / len(self.listanotas)
