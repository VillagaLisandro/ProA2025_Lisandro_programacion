class Estudiante:
    def __init__(self, id: int, nombre: str, apellido: str, año: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.año = año

class Materia:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class Calificacion:
    def __init__(self, id: int, estudiante_id: int, materia_id: int, calificacion: int, anho: int):
        self.id = id
        self.estudiante_id = estudiante_id
        self.materia_id = materia_id
        self.calificacion = calificacion
        self.anho = anho
