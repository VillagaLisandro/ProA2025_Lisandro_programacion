class Estudiante:
    def __init__(self, id: int, nombre: str, apellido: str, año: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.año = año
    
    def obtener_nombre_completo(self):
        #imprime el nombre completo del estudiante 
        return f"{self.nombre} {self.apellido}"
    
    def actualizar_nombre(self, nuevo_nombre: str, nuevo_apellido: str):
        #Actualiza el nombre y apellido del estudiante.
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
    
    def mostrar_detalles(self):
        #Detalles del etudiante 
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Año: {self.año}"

class Materia:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
    
    def cambiar_nombre(self, nuevo_nombre: str):
        #cambiar el nombre de la materia
        
        self.nombre = nuevo_nombre
    
    def mostrar_detalles(self):
        """Devuelve los detalles de la materia como una cadena."""
        return f"ID: {self.id}, Materia: {self.nombre}"

class Calificacion:
    def __init__(self, id: int, estudiante_id: int, materia_id: int, calificacion: int, anho: int):
        self.id = id
        self.estudiante_id = estudiante_id
        self.materia_id = materia_id
        self.calificacion = calificacion
        self.anho = anho
    
    def actualizar_calificacion(self, nueva_calificacion: int):
        #actualiza la calificacion
        self.calificacion = nueva_calificacion
    
    def mostrar_detalles(self):
        #devuelve los detalles de la calificacion en una cadena
        return f"ID: {self.id}, Estudiante ID: {self.estudiante_id}, Materia ID: {self.materia_id}, Calificación: {self.calificacion}, Año: {self.anho}"
    
    def es_aprobada(self):
        #verifica la calificacion
        return self.calificacion >= 6