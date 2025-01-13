"""
Este programa permite gestionar información básica de un estudiante y calcular su promedio de calificaciones.
Se utilizan diferentes tipos de datos y se siguen las convenciones de nomenclatura en Python.
"""


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de calificaciones.
    :param notas: Lista de números flotantes que representan las calificaciones.
    :return: Float, el promedio de las calificaciones.
    """
    # Retorna el promedio calculando la suma de notas dividida por su cantidad
    return sum(notas) / len(notas)


def main():
    """
    Función principal que recoge información del estudiante, procesa los datos y muestra los resultados.
    """
    print("Bienvenido al sistema de gestión de información estudiantil.\n")

    # Recopilar información del estudiante
    estudiante_nombre = input("Por favor, ingresa tu nombre: ")  # Tipo string
    estudiante_edad = int(input("Ingresa tu edad: "))  # Tipo entero
    es_mayor_de_edad = estudiante_edad >= 18  # Tipo boolean

    # Solicitar calificaciones
    print("\nIngresa tus tres calificaciones (una por vez):")
    calificacion_1 = float(input("Calificación 1: "))
    calificacion_2 = float(input("Calificación 2: "))
    calificacion_3 = float(input("Calificación 3: "))

    # Guardar las calificaciones en una lista
    notas = [calificacion_1, calificacion_2, calificacion_3]  # Tipo lista de flotantes

    # Calcular el promedio de las calificaciones
    promedio = calcular_promedio(notas)

    # Mostrar resultados
    print(f"\nHola, {estudiante_nombre}.")
    print(f"Tienes {estudiante_edad} años. {'Eres mayor de edad.' if es_mayor_de_edad else 'No eres mayor de edad.'}")
    print(f"Tus calificaciones son: {notas}")
    print(f"Tu promedio de calificaciones es: {promedio:.2f}")

    # Verificar si el estudiante aprobó
    aprobado = promedio >= 7.0  # Tipo boolean
    print("¡Felicidades, aprobaste!" if aprobado else "Lo siento, no aprobaste. Sigue esforzándote.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
