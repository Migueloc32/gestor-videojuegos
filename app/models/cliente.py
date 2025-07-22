class Cliente:
    contador_id = 1
    clientes = []

    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.id = Cliente.contador_id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        Cliente.contador_id += 1

    def aplicar_descuento(self):
        self.nombre += " (DESCUENTO APLICADO)"
