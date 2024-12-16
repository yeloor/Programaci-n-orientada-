# Programación Tradicional: Utilizando funciones para la entrada de datos y cálculo del promedio

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Crear una lista vacía para almacenar las temperaturas de cada día
    temperaturas = []
    # Solicitar las temperaturas para cada uno de los 7 días de la semana
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))  # Entrada de datos del usuario
        temperaturas.append(temperatura)  # Agregar la temperatura a la lista
    return temperaturas  # Retornar la lista de temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    # Sumar todas las temperaturas de la lista
    total = sum(temperaturas)
    # Calcular el promedio dividiendo la suma por la cantidad de elementos (7 días)
    promedio = total / len(temperaturas)
    return promedio  # Retornar el promedio calculado

# Función principal que organiza el flujo del programa
def main():
    # Obtener las temperaturas de la semana llamando a la función ingresar_temperaturas
    temperaturas = ingresar_temperaturas()
    # Calcular el promedio semanal usando la función calcular_promedio
    promedio = calcular_promedio(temperaturas)
    # Mostrar el resultado con un formato adecuado (2 decimales)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Llamada a la función principal para ejecutar el programa
main()
