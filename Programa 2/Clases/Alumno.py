class Alumno (object):
    nombre = ""
    apellido = ""
    fecha = None
    listanotas = []
    def setNombre (self, n):
        self.nombre = str(n)

    def setApellido (self, t):
        self.apellido = str(t)

    def setFecha (self, q):
        self.fecha = q

    def addNota (self, nota):
        self.listanotas.append = nota

    def minNota (self):
        menor = listanotas[0]
        for valor in listanotas:
            if valor < menor:
                menor = valor
        return menor

    def maxNota (self):
        mayor = listanotas[0]
        for valor in listanotas:
            if valor < mayor:
                mayor = valor
        return mayor

