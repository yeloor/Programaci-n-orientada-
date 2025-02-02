import os
import subprocess


def mostrar_codigo(ruta_script):
    """Muestra el código de un script en la terminal."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """Ejecuta un script Python en una nueva terminal según el sistema operativo."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['python', ruta_script], shell=True)
        else:  # Linux / macOS
            subprocess.run(['python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """Menú principal para seleccionar unidades."""
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    unidades = {
        '1': 'Unidad 1', '2': 'Unidad 2', '3': 'Unidad 3',
        '4': 'Unidad 4', '5': 'Unidad 5', '6': 'Unidad 6'
    }

    while True:
        print("\n=== Menú Principal - Dashboard ===")
        for key, nombre in unidades.items():
            print(f"{key} - {nombre}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """Menú de selección de subcarpetas dentro de una unidad."""
    if not os.path.exists(ruta_unidad):
        print("\nEsta unidad no tiene subcarpetas disponibles.")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n=== Submenú - Selecciona una subcarpeta ===")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Intenta de nuevo.")


def mostrar_scripts(ruta_sub_carpeta):
    """Lista y permite seleccionar scripts Python para ver y ejecutar."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n=== Scripts Disponibles ===")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script o '0'/'9' para regresar: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("Presiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
