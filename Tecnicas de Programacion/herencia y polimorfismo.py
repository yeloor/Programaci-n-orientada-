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


class Guerrero(Personaje):
    def atacar(self, enemigo, dano):
        super().atacar(enemigo, dano)
        print(f"{self.nombre} grita: ¡Por la gloria!")


class Mago(Personaje):
    def __init__(self, nombre, salud, mana):
        super().__init__(nombre, salud)
        self.mana = mana

    def lanzar_hechizo(self, enemigo, dano):
        if self.mana >= 10:
            enemigo.salud -= dano
            self.mana -= 10
            print(f"{self.nombre} lanzó un hechizo a {enemigo.nombre}, causando {dano} puntos de daño.")
            print(f"{self.nombre} tiene {self.mana} puntos de mana restantes.")
            enemigo.mostrar_estado()
        else:
            print(f"{self.nombre} no tiene suficiente mana para lanzar un hechizo.")


# Ejemplo de uso
if __name__ == "__main__":
    guerrero = Guerrero("Guerrero", 120)
    mago = Mago("Mago", 70, 50)

    guerrero.mostrar_estado()
    mago.mostrar_estado()

    guerrero.atacar(mago, 30)
    mago.lanzar_hechizo(guerrero, 25)
