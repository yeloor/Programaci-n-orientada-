# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa una habitación con número, tipo y precio.
        """
        self.numero = numero  # Atributo: número de habitación
        self.tipo = tipo      # Atributo: tipo de habitación (por ejemplo, 'Individual', 'Doble', etc.)
        self.precio = precio  # Atributo: precio de la habitación por noche
        self.ocupada = False  # Atributo: indica si la habitación está ocupada o no

    def reservar(self):
        """
        Marca la habitación como ocupada y devuelve un mensaje si se puede reservar.
        """
        if not self.ocupada:
            self.ocupada = True  # Se marca la habitación como ocupada
            return f"Habitación {self.numero} ({self.tipo}) ha sido reservada."
        else:
            return f"Habitación {self.numero} ya está ocupada."

    def liberar(self):
        """
        Marca la habitación como disponible y devuelve un mensaje si se puede liberar.
        """
        if self.ocupada:
            self.ocupada = False  # Se marca la habitación como disponible
            return f"Habitación {self.numero} ha sido liberada."
        else:
            return f"Habitación {self.numero} ya está disponible."


# Clase Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        """
        Inicializa un cliente con nombre y cédula.
        """
        self.nombre = nombre  # Atributo: nombre del cliente
        self.cedula = cedula  # Atributo: cédula o ID del cliente

    def realizar_reserva(self, habitacion):
        """
        Realiza la reserva de una habitación.
        """
        return habitacion.reservar()  # Llama al método de reservar de la clase Habitacion

    def cancelar_reserva(self, habitacion):
        """
        Cancela la reserva de una habitación.
        """
        return habitacion.liberar()  # Llama al método de liberar de la clase Habitacion


# Clase Hotel
class Hotel:
    def __init__(self, nombre):
        """
        Inicializa el hotel con un nombre y una lista de habitaciones.
        """
        self.nombre = nombre  # Atributo: nombre del hotel
        self.habitaciones = []  # Atributo: lista de habitaciones disponibles en el hotel

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación al hotel.
        """
        self.habitaciones.append(habitacion)  # Añade una habitación a la lista de habitaciones

    def mostrar_habitaciones_disponibles(self):
        """
        Muestra las habitaciones disponibles.
        """
        disponibles = [h for h in self.habitaciones if not h.ocupada]  # Filtra las habitaciones disponibles
        if disponibles:
            # Devuelve una lista de habitaciones disponibles con sus precios y tipos
            return [f"Habitación {h.numero} ({h.tipo}) - ${h.precio}" for h in disponibles]
        else:
            return "No hay habitaciones disponibles."


# Ejemplo de uso
if __name__ == "__main__":
    # Crear hotel y habitaciones
    hotel = Hotel("Hotel Paraíso")
    habitacion1 = Habitacion(101, "Simple", 50)
    habitacion2 = Habitacion(102, "Doble", 80)
    habitacion3 = Habitacion(103, "Suite", 150)

    # Agregar habitaciones al hotel
    hotel.agregar_habitacion(habitacion1)
    hotel.agregar_habitacion(habitacion2)
    hotel.agregar_habitacion(habitacion3)

    # Crear un cliente
    cliente1 = Cliente("Yuri Loor", "1317215265")

    # Cliente realiza una reserva
    print(cliente1.realizar_reserva(habitacion1))  # Reserva la habitación 101
    print(hotel.mostrar_habitaciones_disponibles())  # Muestra las habitaciones disponibles después de la reserva
    # Cliente cancela la reserva
    print(cliente1.cancelar_reserva(habitacion1))  # Cancela la reserva de la habitación 101
    print(hotel.mostrar_habitaciones_disponibles())  # Muestra las habitaciones disponibles después de la cancelación
