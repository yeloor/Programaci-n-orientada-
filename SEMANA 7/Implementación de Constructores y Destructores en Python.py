class FileHandler:
    def __init__(self, filename, mode='r'):
        """
        Este programa muestra cómo abrir , escribir , leer y cerrar un archivo de texto usando constructores y destructores en Python.
        Este método se ejecuta automáticamente cuando se crea una instancia de la clase.

        Abre el archivo en el modo especificado (por defecto, 'r' para lectura).
        Si el archivo no se puede abrir, captura la excepción y la maneja.

        :param filename: Nombre del archivo a manejar.
        :param mode: Modo de apertura del archivo ('r', 'w', 'a', etc.), por defecto es 'r'.
        """
        self.filename = filename  # Atributo que guarda el nombre del archivo
        self.mode = mode  # Atributo que guarda el modo en que se abrirá el archivo
        self.file = None  # Atributo que almacenará la referencia al archivo abierto

        try:
            # Intentamos abrir el archivo en el modo indicado
            self.file = open(self.filename, self.mode)
            print(f"Archivo '{self.filename}' abierto en modo '{self.mode}'.")
        except Exception as e:
            # Si hay un error al abrir el archivo, se maneja aquí
            print(f"Error al abrir el archivo '{self.filename}': {e}")
            self.file = None

    def write_data(self, data):
        """
        Método para escribir datos en el archivo si está abierto en modo escritura.

        Este método no puede escribir en archivos abiertos en modo lectura o si el archivo no está abierto correctamente.

        :param data: Datos a escribir en el archivo.
        """
        if self.file and not self.file.closed and 'w' in self.mode:
            self.file.write(data)
            print(f"Datos escritos en el archivo '{self.filename}'.")
        else:
            print("No se puede escribir en el archivo. Asegúrate de que está abierto en modo escritura.")

    def read_data(self):
        """
        Método para leer datos del archivo si está abierto en modo lectura.

        Este método solo funciona si el archivo está en modo lectura ('r') y está abierto correctamente.

        :return: Contenido del archivo o None si no se puede leer.
        """
        if self.file and not self.file.closed and 'r' in self.mode:
            return self.file.read()
        else:
            print("No se puede leer del archivo. Asegúrate de que está abierto en modo lectura.")
            return None

    def __del__(self):
        """
        Destructor que cierra el archivo si está abierto.

        Este método se ejecuta automáticamente cuando el objeto es destruido o eliminado.
        Se asegura de que el archivo se cierre adecuadamente para liberar recursos.

        Si el archivo no está abierto, no realiza ninguna acción.
        """
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.filename}' cerrado.")
        else:
            print(f"El archivo '{self.filename}' ya estaba cerrado o no fue abierto correctamente.")


# Ejemplo de uso:
# 1. Crear una instancia de la clase FileHandler para abrir un archivo en modo escritura.
file_handler = FileHandler('example.txt', 'w')  # Constructor __init__ se ejecuta aquí.
file_handler.write_data("Hola, este es un archivo de prueba.\n")
# Destructor __del__ se ejecuta automáticamente cuando el objeto se destruye.
del file_handler  # Llamada explícita al destructor para cerrar el archivo.

# 2. Crear una instancia de FileHandler para leer datos del archivo.
file_handler = FileHandler('example.txt', 'r')  # Constructor __init__ se ejecuta aquí.
content = file_handler.read_data()
print(f"Contenido leído: {content}")
# Destructor __del__ se ejecuta automáticamente cuando el objeto se destruye.
del file_handler  # Llamada explícita al destructor para cerrar el archivo.
