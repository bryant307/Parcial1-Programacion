"""Una tienda local vende diversos productos, cada vez que un cliente
hace una compra niña mary se encarga de anotarlo en una libreta. A su
vez, con una calculadora le da el total a cada cliente y les da su
respectivo vuelto en caso de necesitarlo"""


class Tienda:
    def __init__(self):
        self.inventario = {}
        self.venta = []

    def agregando_producto(self, nombre, cantidad, precio_venta):
        if nombre in self.inventario:
            self.inventario[nombre]['cantidad'] += cantidad
        else:
            self.inventario[nombre] = {'cantidad': cantidad, precio_venta}