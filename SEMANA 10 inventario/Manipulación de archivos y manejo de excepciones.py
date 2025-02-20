class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """Inicializa el inventario cargando los productos desde un archivo."""
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo de texto, manejando excepciones."""
        productos = {}
        try:
            with open(self.archivo, "r") as file:
                lines = file.readlines()
                if lines:
                    for line in lines[1:]:  # Omitir la primera línea (encabezado)
                        nombre, cantidad, precio = line.strip().split(",")
                        productos[nombre] = {"cantidad": int(cantidad), "precio": float(precio)}
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo inventario.")
        except ValueError:
            print("Error en el formato del archivo. Verifique los datos.")
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")
        return productos

    def guardar_inventario(self):
        """Guarda el inventario en un archivo de texto con formato ordenado."""
        try:
            with open(self.archivo, "w") as file:
                file.write(f"{'Producto':<20} {'Cantidad':<10} {'Precio':<10}\n")  # Encabezado
                file.write("=" * 42 + "\n")  # Línea separadora
                for nombre, datos in self.productos.items():
                    file.write(f"{nombre:<20} {datos['cantidad']:<10} ${datos['precio']:.2f}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto o actualiza uno existente, notificando el resultado."""
        if nombre in self.productos:
            self.productos[nombre]['cantidad'] += cantidad
            self.productos[nombre]['precio'] = precio
        else:
            self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado/actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario, notificando al usuario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra los productos en el inventario con formato tabulado."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            print(f"{'Producto':<20} {'Cantidad':<10} {'Precio':<10}")
            print("=" * 42)
            for nombre, datos in self.productos.items():
                print(f"{nombre:<20} {datos['cantidad']:<10} ${datos['precio']:.2f}")


# Uso del sistema de gestión de inventarios
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del sistema de gestión de inventarios.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
