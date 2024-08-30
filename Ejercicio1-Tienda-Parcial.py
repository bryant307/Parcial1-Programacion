"""Una tienda local vende diversos productos, cada vez que un cliente
hace una compra niña mary se encarga de anotarlo en una libreta. A su
vez, con una calculadora le da el total a cada cliente y les da su
respectivo vuelto en caso de necesitarlo"""


class Tienda:
    def __init__(self):
        self.inventario = {}  # Diccionario para almacenar el inventario {producto: [cantidad, precio]}
        self.ventas = []      # Lista para registrar las ventas

    def agregar_producto(self, producto, cantidad, precio):
        if producto in self.inventario:
            self.inventario[producto][0] += cantidad
        else:
            self.inventario[producto] = [cantidad, precio]
    
    def registrar_venta(self, productos_comprados, pago):
        total = 0
        for producto, cantidad in productos_comprados.items():
            if producto in self.inventario and self.inventario[producto][0] >= cantidad:
                total += self.inventario[producto][1] * cantidad
                self.inventario[producto][0] -= cantidad
            else:
                print(f"Error: {producto} no disponible o cantidad insuficiente.")
                return
        
        vuelto = pago - total
        if vuelto < 0:
            print("Error: Pago insuficiente.")
            return
        
        self.ventas.append((productos_comprados, total, pago, vuelto))
        print(f"Total de la venta: ${total:.2f}")
        print(f"Vuelto: ${vuelto:.2f}")
    
    def mostrar_inventario(self):
        print("Inventario:")
        for producto, (cantidad, precio) in self.inventario.items():
            print(f"{producto}: Cantidad={cantidad}, Precio unitario=${precio:.2f}")

    def mostrar_ventas(self):
        print("Ventas registradas:")
        for venta in self.ventas:
            productos, total, pago, vuelto = venta
            print(f"Productos: {productos}, Total: ${total:.2f}, Pago: ${pago:.2f}, Vuelto: ${vuelto:.2f}")

# Ejemplo
tienda = Tienda()
tienda.agregar_producto("Pepsi 1.5L", 100, 1.50)
tienda.agregar_producto("Toztecas", 50, 0.25)

# Registrar una venta
productos_comprados = {"Manzanas": 3, "Pan": 1}
pago = 10.00
tienda.registrar_venta(productos_comprados, pago)

# Mostrar inventario y ventas
tienda.mostrar_inventario()
tienda.mostrar_ventas()
