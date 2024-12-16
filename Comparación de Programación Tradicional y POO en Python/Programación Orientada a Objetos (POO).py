# Programación Orientada a Objetos: Usando clases y métodos para encapsular la lógica

# Clase que representa la información del clima semanal
class Clima:
    # Constructor que inicializa la lista de temperaturas
    def __init__(self):
        self.temperaturas = []  # Atributo para almacenar las temperaturas

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        # Solicitar las temperaturas para cada uno de los 7 días de la semana
        for i in range(7):
            # Entrada de datos del usuario y agregarlos a la lista
            temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temperatura)

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio(self):
        # Sumar todas las temperaturas de la lista
        total = sum(self.temperaturas)
        # Calcular el promedio dividiendo la suma entre la cantidad de días (7)
        promedio = total / len(self.temperaturas)
        return promedio  # Retornar el promedio calculado


# Clase derivada para extender la funcionalidad, ejemplo de herencia
class ClimaAvanzado(Clima):
    # Constructor que inicializa la clase base
    def __init__(self):
        super().__init__()

    # Método adicional para calcular el rango de temperaturas (máxima - mínima)
    def calcular_rango(self):
        # Calcular la diferencia entre la temperatura máxima y mínima
        return max(self.temperaturas) - min(self.temperaturas)


# Función principal que organiza el flujo del programa
def main():
    # Crear una instancia de la clase ClimaAvanzado (hereda de Clima)
    clima = ClimaAvanzado()
    # Ingresar las temperaturas mediante el método de la clase
    clima.ingresar_temperaturas()
    # Calcular el promedio de las temperaturas usando el método de la clase
    promedio = clima.calcular_promedio()
    # Calcular el rango de temperaturas usando el método de la clase derivada
    rango = clima.calcular_rango()

    # Mostrar los resultados: promedio y rango de temperaturas
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")
    print(f"El rango de temperaturas es: {rango:.2f}°C")


# Llamada a la función principal
main()
