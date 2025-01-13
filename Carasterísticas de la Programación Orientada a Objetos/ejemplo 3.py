# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre, matricula):
        """
        Constructor para inicializar un estudiante.
        :param nombre: Nombre del estudiante.
        :param matricula: Número de matrícula del estudiante.
        """
        self.nombre = nombre  # Nombre del estudiante
        self.matricula = matricula  # Número de matrícula único
        self.calificaciones = []  # Lista de calificaciones del estudiante

    def agregar_calificacion(self, calificacion):
        """Agrega una calificación a la lista del estudiante."""
        self.calificaciones.append(calificacion)

    def promedio(self):
        """
        Calcula el promedio de las calificaciones del estudiante.
        :return: Promedio de calificaciones.
        """
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0

# Clase que representa una escuela con múltiples estudiantes
class Escuela:
    def __init__(self, nombre):
        """
        Constructor para inicializar una escuela.
        :param nombre: Nombre de la escuela.
        """
        self.nombre = nombre  # Nombre de la escuela
        self.estudiantes = []  # Lista de estudiantes en la escuela

    def agregar_estudiante(self, estudiante):
        """Agrega un estudiante a la lista de la escuela."""
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        """Muestra todos los estudiantes con sus promedios."""
        print(f"Estudiantes en {self.nombre}:")
        for est in self.estudiantes:
            print(f"- {est.nombre} (Matrícula: {est.matricula}) - Promedio: {est.promedio():.2f}")

# Ejecución del programa
escuela = Escuela("Escuela Nacional")  # Crear una escuela
# Crear estudiantes y agregar calificaciones
est1 = Estudiante("Ana López", "12345")
est1.agregar_calificacion(85)
est1.agregar_calificacion(90)

est2 = Estudiante("Carlos Pérez", "67890")
est2.agregar_calificacion(78)

# Agregar estudiantes a la escuela
escuela.agregar_estudiante(est1)
escuela.agregar_estudiante(est2)

escuela.mostrar_estudiantes()  # Mostrar los estudiantes y sus promedios
