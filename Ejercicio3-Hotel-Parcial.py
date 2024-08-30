class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo  
        self.precio_por_noche = precio_por_noche 


class Cliente:
    def __init__(self, nombre, dui, noches):
        self.nombre = nombre  
        self.dui = dui
        self.noches = noches  
        self.servicios_extras = []  

    def agregar_servicio_extra(self, servicio):
        self.servicios_extras.append(servicio)


class Factura:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente  
        self.habitacion = habitacion

    def calcular_total(self):
        costo_habitacion = self.habitacion.precio_por_noche * self.cliente.noches
        costo_servicios = sum(servicio['precio'] for servicio in self.cliente.servicios_extras)
        return costo_habitacion + costo_servicios

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


class Recepcionista:
    def __init__(self):
        self.habitaciones = [
            Habitacion("Simple", 100),
            Habitacion("Doble", 150),
            Habitacion("Suite", 300)
        ]
        self.servicios_extras = [
            {"nombre": "Piscina", "precio": 20},
            {"nombre": "Cancha de Golf", "precio": 50}
        ]

    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(self.habitaciones, start=1):
            print(f"{i}. {habitacion.tipo} - {habitacion.precio_por_noche} $ por noche")

    def mostrar_servicios_extras(self):
        print("Servicios extra disponibles:")
        for i, servicio in enumerate(self.servicios_extras, start=1):
            print(f"{i}. {servicio['nombre']} - {servicio['precio']} $")

    def crear_cliente(self):
        nombre = input("Ingrese su nombre: ")
        dni = input("Ingrese su Documento: ")
        noches = self.validar_numero("Ingrese el número de noches: ")
        return Cliente(nombre, dni, noches)

    def validar_numero(self, mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if valor > 0:
                    return valor
                else:
                    print("Por favor ingrese un número mayor que 0.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número entero.")

    def elegir_habitacion(self):
        self.mostrar_habitaciones()
        while True:
            eleccion = self.validar_numero("Elija una habitación (número): ")
            if 1 <= eleccion <= len(self.habitaciones):
                return self.habitaciones[eleccion - 1]
            else:
                print("Selección inválida. Elija un número de la lista.")

    def elegir_servicios_extras(self, cliente):
        while True:
            self.mostrar_servicios_extras()
            try:
                eleccion = int(input("Elija un servicio extra (número, 0 para terminar): "))
                if eleccion == 0:
                    print("Finalizando selección de servicios extra.")
                    break
                elif 1 <= eleccion <= len(self.servicios_extras):
                    servicio = self.servicios_extras[eleccion - 1]
                    cliente.agregar_servicio_extra(servicio)
                    print(f"Servicio '{servicio['nombre']}' agregado.")
                else:
                    print("Selección inválida. Elija un número de la lista.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

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
