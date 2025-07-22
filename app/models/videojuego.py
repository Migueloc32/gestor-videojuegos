class Videojuego:
    juegos_id = 1
    videojuegos = []

    def __init__(self, nombre, genero, precio):
        self.id = Videojuego.juegos_id
        Videojuego.juegos_id += 1
        self.nombre = nombre
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio = round(self.precio * (1 - porcentaje / 100), 2)