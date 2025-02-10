class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("El producto con este ID ya existe en el inventario.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado en el inventario.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados if encontrados else "Producto no encontrado."

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de Inventario:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = int(input("Ingrese ID del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Ingrese nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Ingrese nuevo precio (deje vacío si no desea cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for producto in resultados:
                    print(producto)
            else:
                print(resultados)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
