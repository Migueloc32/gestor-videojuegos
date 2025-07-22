class Videojuego:
    videojuegos = []
    id_counter = 1

    def __init__(self, nombre, genero, precio):
        self.id = Videojuego.id_counter
        Videojuego.id_counter += 1
        self.nombre = nombre
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje / 100)