class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def atacar(self, enemigo, dano):
        enemigo.salud -= dano
        print(f"{self.nombre} atacó a {enemigo.nombre} causando {dano} puntos de daño.")
        enemigo.mostrar_estado()

    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.salud} puntos de salud restantes.")

# Ejemplo de uso
if __name__ == "__main__":
    guerrero = Personaje("Guerrero", 100)
    arquero = Personaje("Arquero", 80)

    guerrero.mostrar_estado()
    arquero.mostrar_estado()

    guerrero.atacar(arquero, 20)
