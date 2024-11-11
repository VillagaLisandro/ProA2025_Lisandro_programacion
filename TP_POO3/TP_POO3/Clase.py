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

class Profesor:
    def __init__(self, dni_id: int, nombre: str, apellido: str, curso: str, estado: str, email: str):
        self.dni_id = dni_id
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.estado = estado
        self.email = email

    #mostrar información del profesor
    def mostrar_info(self):
        return f"Profesor {self.nombre} {self.apellido} (DNI: {self.dni_id}) enseña {self.curso} y está {self.estado}."

    # cambiar el estado del profesor
    def cambiar_estado(self, nuevo_estado: str):
        self.estado = nuevo_estado
        return f"El estado del profesor {self.nombre} ha sido cambiado a {nuevo_estado}."

    # curso que enseña el profesor
    def cambiar_curso(self, nuevo_curso: str):
        self.curso = nuevo_curso
        return f"El curso del profesor {self.nombre} ahora es {nuevo_curso}."

    #actualizar el email del profesor
    def actualizar_email(self, nuevo_email: str):
        self.email = nuevo_email
        return f"El email del profesor {self.nombre} ha sido actualizado a {nuevo_email}."

class Database:
    def __init__(self, connection_string):
        # Implementar la lógica para conectar a la base de datos
        # Aquí se usaría el conector específico para el tipo de base de datos
        # Ejemplo con SQLite:
        import sqlite3
        self.conn = sqlite3.connect(connection_string)
        self.cursor = self.conn.cursor()

    def ejecutar_consulta(self, query, *args):
        # Ejecutar una consulta SQL
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()