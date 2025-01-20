# Clase base: Persona
class Persona:
    """
    Clase base que representa a una persona con nombre y edad.
    Incluye encapsulación para proteger el atributo de edad.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad    # Atributo privado (encapsulación)

    # Método público para obtener la edad (encapsulación)
    def get_edad(self):
        return self.__edad

    # Método público para modificar la edad con validación
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

    # Método común para presentar a la persona
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.__edad} años."

# Clase derivada: Empleado
class Empleado(Persona):
    """
    Clase derivada que extiende a Persona, representando a un empleado con un puesto específico.
    """
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # Herencia: inicializar atributos de la clase base
        self.puesto = puesto  # Atributo específico de la clase derivada

    # Sobrescribir método presentarse (Polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.get_edad()} años y trabajo como {self.puesto}."

# Clase derivada: Cliente
class Cliente(Persona):
    """
    Clase derivada que extiende a Persona, representando a un cliente con un número de compras realizadas.
    """
    def __init__(self, nombre, edad, compras):
        super().__init__(nombre, edad)  # Herencia
        self.compras = compras  # Atributo específico de la clase derivada

    # Sobrescribir método presentarse (Polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.get_edad()} años y he realizado {self.compras} compras."

# Función para demostrar Polimorfismo
def mostrar_presentacion(persona):
    """
    Función que utiliza el método presentarse de diferentes objetos, mostrando polimorfismo.
    """
    print(persona.presentarse())

# Creación de instancias y demostración de funcionalidad
if __name__ == "__main__":
    # Instancia de la clase base
    persona1 = Persona("YURI", 23)
    print(persona1.presentarse())
    persona1.set_edad(25)  # Modificar edad usando encapsulación
    print(f"Edad actualizada de {persona1.nombre}: {persona1.get_edad()}")

    # Instancias de clases derivadas
    empleado1 = Empleado("Luis", 30, "Ingeniero de Software")
    cliente1 = Cliente("Ana", 28, 12)

    # Uso de polimorfismo con la función mostrar_presentacion
    print("\nDemostración de Polimorfismo:")
    mostrar_presentacion(persona1)
    mostrar_presentacion(empleado1)
    mostrar_presentacion(cliente1)
