import json


class Producto:
    """
    Representa un producto en el inventario con atributos básicos como ID, nombre, cantidad y precio.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario
        self.precio = precio  # Precio unitario del producto

    def obtener_info(self):
        """Retorna la información del producto en formato de diccionario."""
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad disponible del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio


class Inventario:
    """
    Gestiona la colección de productos usando un diccionario para acceso eficiente por ID.
    """

    def __init__(self):
        self.productos = {}  # Diccionario que almacena los productos usando el ID como clave

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario si el ID no está en uso."""
        if producto.id_producto not in self.productos:
            self.productos[producto.id_producto] = producto
        else:
            print("El producto con este ID ya existe.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario usando su ID si existe."""
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("El producto no existe.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o precio de un producto específico."""
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos en el inventario por nombre y retorna la lista de coincidencias."""
        return [p.obtener_info() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        for producto in self.productos.values():
            print(producto.obtener_info())

    def guardar_en_archivo(self, archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON para persistencia de datos."""
        with open(archivo, "w") as f:
            json.dump([p.obtener_info() for p in self.productos.values()], f, indent=4)

    def cargar_desde_archivo(self, archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON, si existe."""
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {item["ID"]: Producto(**item) for item in data}
        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará un nuevo inventario.")


# Interfaz de usuario en consola
if __name__ == "__main__":
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\nGestión de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_producto(nombre)
            if productos:
                for p in productos:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

