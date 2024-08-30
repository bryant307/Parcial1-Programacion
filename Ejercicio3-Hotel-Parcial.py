class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo  # Tipo de habitación (por ejemplo, Simple, Doble, Suite)
        self.precio_por_noche = precio_por_noche  # Precio por noche de la habitación

# Definimos la clase Cliente para manejar los detalles del cliente
class Cliente:
    def __init__(self, nombre, dui, noches):
        self.nombre = nombre  
        self.dui = dui
        self.noches = noches  
        self.servicios_extras = []  

    # Método para agregar un servicio extra a la lista del cliente
    def agregar_servicio_extra(self, servicio):
        self.servicios_extras.append(servicio)

class Factura:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente  
        self.habitacion = habitacion

    
    def calcular_total(self):
        costo_habitacion = self.habitacion.precio_por_noche * self.cliente.noches
        costo_servicios = sum(servicio['precio'] for servicio in self.cliente.servicios_extras)
        return costo_habitacion + costo_servicios  # Retorna el total de la factura

    # Método para mostrar la factura detallada
    def mostrar_factura(self):
        print(f"Factura para {self.cliente.nombre}")
        print(f"Documento: {self.cliente.dui}")
        print(f"Tipo de habitación: {self.habitacion.tipo}")
        print(f"Noches: {self.cliente.noches}")
        print(f"Precio por noche: {self.habitacion.precio_por_noche} $")
        print(f"Servicios extra:")
        for servicio in self.cliente.servicios_extras:
            print(f" - {servicio['nombre']}: {servicio['precio']} $")
        print(f"Total: {self.calcular_total()} $")

# Definimos la clase Recepcionista para manejar las interacciones con el cliente
class Recepcionista:
    def __init__(self):
        # Lista de habitaciones disponibles con su tipo y precio
        self.habitaciones = [
            Habitacion("Simple", 100),
            Habitacion("Doble", 150),
            Habitacion("Suite", 300)
        ]
        # Lista de servicios extras disponibles con su nombre y precio
        self.servicios_extras = [
            {"nombre": "Piscina", "precio": 20},
            {"nombre": "Cancha de Golf", "precio": 50}
        ]

    # Método para mostrar las habitaciones disponibles
    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(self.habitaciones, start=1):
            print(f"{i}. {habitacion.tipo} - {habitacion.precio_por_noche} $ por noche")

    # Método para mostrar los servicios extras disponibles
    def mostrar_servicios_extras(self):
        print("Servicios extra disponibles:")
        for i, servicio in enumerate(self.servicios_extras, start=1):
            print(f"{i}. {servicio['nombre']} - {servicio['precio']} $")

    # Método para crear un nuevo cliente solicitando sus datos
    def crear_cliente(self):
        nombre = input("Ingrese su nombre: ")
        dni = input("Ingrese su DNI: ")
        noches = int(input("Ingrese el número de noches: "))
        return Cliente(nombre, dni, noches)

    # Método para que el cliente elija una habitación
    def elegir_habitacion(self):
        self.mostrar_habitaciones()  # Mostramos las opciones de habitaciones
        eleccion = int(input("Elija una habitación (número): ")) - 1
        return self.habitaciones[eleccion]

    # Método para que el cliente elija los servicios extras
    def elegir_servicios_extras(self, cliente):
        while True:
            self.mostrar_servicios_extras()  # Mostramos las opciones de servicios extras
            eleccion = int(input("Elija un servicio extra (número, 0 para terminar): "))
            if eleccion == 0:  # Si elige 0, termina la selección de servicios extras
                break
            servicio = self.servicios_extras[eleccion - 1]
            cliente.agregar_servicio_extra(servicio)  # Agregamos el servicio extra al cliente

    # Método para generar y mostrar la factura al cliente
    def generar_factura(self, cliente, habitacion):
        factura = Factura(cliente, habitacion)
        factura.mostrar_factura()


def main():
    recepcionista = Recepcionista()
    cliente = recepcionista.crear_cliente()
    habitacion = recepcionista.elegir_habitacion()
    recepcionista.elegir_servicios_extras(cliente)
    recepcionista.generar_factura(cliente, habitacion)


if __name__ == "__main__":
    main()