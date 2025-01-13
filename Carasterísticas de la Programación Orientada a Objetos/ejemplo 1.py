# Clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        """
        Inicializa un producto con nombre, categoría, precio y cantidad en stock.
        """
        self.nombre = nombre   # Atributo: nombre del producto
        self.categoria = categoria  # Atributo: categoría del producto (por ejemplo, 'Camisas', 'Pantalones', etc.)
        self.precio = precio   # Atributo: precio del producto
        self.stock = stock     # Atributo: cantidad de producto disponible en stock

    def vender(self, cantidad):
        """
        Realiza la venta de una cantidad específica del producto.
        """
        if self.stock >= cantidad:
            self.stock -= cantidad  # Disminuye el stock disponible
            return f"Venta exitosa de {cantidad} {self.nombre}(s)."
        else:
            return f"No hay suficiente stock de {self.nombre} para completar la venta."


# Clase Cliente
class Cliente:
    def __init__(self, nombre, saldo):
        """
        Inicializa un cliente con nombre y saldo disponible.
        """
        self.nombre = nombre  # Atributo: nombre del cliente
        self.saldo = saldo    # Atributo: saldo disponible para realizar compras

    def comprar(self, producto, cantidad):
        """
        Permite a un cliente comprar un producto.
        """
        costo_total = producto.precio * cantidad  # Calcula el costo total de la compra
        if self.saldo >= costo_total:  # Verifica si el cliente tiene suficiente saldo
            resultado_venta = producto.vender(cantidad)  # Realiza la venta del producto
            self.saldo -= costo_total  # Descuenta el costo de la compra del saldo
            return f"{self.nombre} compró {cantidad} {producto.nombre}(s). {resultado_venta} Saldo restante: ${self.saldo}"
        else:
            return f"{self.nombre} no tiene suficiente saldo para comprar {cantidad} {producto.nombre}(s)."


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    camisa = Producto("Camisa", "Ropa", 25, 10)
    pantalon = Producto("Pantalón", "Ropa", 40, 5)

    # Crear cliente
    cliente2 = Cliente("Ana García", 100)

    # Cliente realiza una compra
    print(cliente2.comprar(camisa, 2))  # Compra 2 camisas
    print(cliente2.comprar(pantalon, 3))  # Intenta comprar 3 pantalones
    print(cliente2.comprar(camisa, 1))  # Compra 1 camisa adicional
