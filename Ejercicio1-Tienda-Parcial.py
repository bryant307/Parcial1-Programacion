"""Una tienda local vende diversos productos, cada vez que un cliente
hace una compra niña mary se encarga de anotarlo en una libreta. A su
vez, con una calculadora le da el total a cada cliente y les da su
respectivo vuelto en caso de necesitarlo"""


class Tienda:
    def __init__(self): #Funcion inizializadora
        self.inventario = {} 
        self.ventas = []    

    def agregar_producto(self, producto, cantidad, precio):
        if producto in self.inventario:
            self.inventario[producto][0] += cantidad
        else:
            self.inventario[producto] = [cantidad, precio]

    def registrar_venta(self, productos_comprados, pago): #Funcion para registrar venta 
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
            print("Pago menor que el total de la compra.")
            return
        
        self.ventas.append((productos_comprados, total, pago, vuelto))
        print(f"Total de la venta: ${total:.2f}")
        print(f"Vuelto: ${vuelto:.2f}")
    
    def mostrar_inventario(self): #Funcion para mostrar inventario
        print("Inventario:")
        print('Productos disponibles')
        for producto, (cantidad, precio) in self.inventario.items():
            print(f"{producto}: Cantidad={cantidad}, Precio unitario=${precio:.2f}")

    def mostrar_ventas(self):
        print("Ventas registradas:")
        for venta in self.ventas:
            productos, total, pago, vuelto = venta
            print(f"Productos: {productos}, Total: ${total:.2f}, Pago: ${pago:.2f}, Vuelto: ${vuelto:.2f}")

    def agregar_producto_proveedor(self, producto, cantidad, precio_sugerido):
        if producto in self.inventario:
            self.inventario[producto][0] += cantidad
            self.inventario[producto][1] = precio_sugerido  # Actualizar el precio sugerido
        else:
            self.inventario[producto] = [cantidad, precio_sugerido]
        print(f"Producto {producto} actualizado con cantidad {cantidad} y precio sugerido ${precio_sugerido:.2f}")

def menu(tienda):
    while True:
        print('------- TIENDITA MARY-------')
        print("\n--- Menú ---")
        print("1. Agregar producto al inventario")
        print("2. Registrar venta")
        print("3. Mostrar inventario")
        print("4. Mostrar ventas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio unitario: "))
            tienda.agregar_producto(producto, cantidad, precio)
            print("Producto agregado al inventario.")
        
        elif opcion == "2":
            productos_comprados = {}
            while True:
                producto = input("Ingrese el nombre del producto : ")
                if producto.lower() == 'fin':
                    break
                cantidad = int(input("Ingrese la cantidad: "))
                productos_comprados[producto] = cantidad
            
            pago = float(input("Ingrese el monto pagado por el cliente: "))
            tienda.registrar_venta(productos_comprados, pago)
        
        elif opcion == "3":
            tienda.mostrar_inventario()
        
        elif opcion == "4":
            tienda.mostrar_ventas()
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

tienda = Tienda()
menu(tienda)
