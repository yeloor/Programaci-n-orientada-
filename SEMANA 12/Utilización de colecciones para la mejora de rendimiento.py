class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre: str, id_usuario: int):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"  - {libro}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.ids_usuarios = set()

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        libro = Libro(titulo, autor, categoria, isbn)
        if isbn not in self.libros_disponibles:
            self.libros_disponibles[isbn] = libro
            print(f"Libro '{titulo}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} ya está registrado.")

    def quitar_libro(self):
        isbn = input("Ingrese el ISBN del libro a eliminar: ")
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = int(input("Ingrese el ID del usuario: "))
        if id_usuario not in self.ids_usuarios:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios_registrados[id_usuario] = usuario
            self.ids_usuarios.add(id_usuario)
            print(f"Usuario '{nombre}' registrado correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} ya está registrado.")

    def prestar_libro(self):
        id_usuario = int(input("Ingrese el ID del usuario: "))
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        if id_usuario not in self.usuarios_registrados:
            print(f"Error: Usuario con ID {id_usuario} no registrado.")
            return
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios_registrados[id_usuario].tomar_prestado(libro)
            print(f"Libro '{libro.info[0]}' prestado a {self.usuarios_registrados[id_usuario].nombre}.")
        else:
            print("Libro no disponible o ISBN incorrecto.")

    def devolver_libro(self):
        id_usuario = int(input("Ingrese el ID del usuario: "))
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            libro_devuelto = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro_devuelto:
                usuario.devolver_libro(isbn)
                self.libros_disponibles[isbn] = libro_devuelto
                print(f"Libro '{libro_devuelto.info[0]}' devuelto por {usuario.nombre}.")
            else:
                print("Este usuario no tiene prestado el libro con ese ISBN.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self):
        criterio = input("Buscar por (titulo/autor/categoria): ")
        valor = input("Ingrese el valor de búsqueda: ")
        encontrados = [libro for libro in self.libros_disponibles.values()
                       if (criterio == "titulo" and valor.lower() in libro.info[0].lower()) or
                       (criterio == "autor" and valor.lower() in libro.info[1].lower()) or
                       (criterio == "categoria" and valor.lower() in libro.categoria.lower())]
        if encontrados:
            print(f"Libros encontrados por {criterio} '{valor}':")
            for libro in encontrados:
                print(f"  - {libro}")
        else:
            print(f"No se encontraron libros con {criterio}: '{valor}'.")


# Menú interactivo
biblioteca = Biblioteca()
while True:
    print("\n--- Sistema de Biblioteca Digital ---")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Buscar libro")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        biblioteca.agregar_libro()
    elif opcion == "2":
        biblioteca.quitar_libro()
    elif opcion == "3":
        biblioteca.registrar_usuario()
    elif opcion == "4":
        biblioteca.prestar_libro()
    elif opcion == "5":
        biblioteca.devolver_libro()
    elif opcion == "6":
        biblioteca.buscar_libro()
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
