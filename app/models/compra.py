from datetime import datetime

class Compra:
    compras_id = 1
    compras = []

    def __init__(self, cliente_id, videojuego_id, fecha=None):
        self.id = Compra.compras_id
        Compra.compras_id += 1
        self.cliente_id = cliente_id
        self.videojuego_id = videojuego_id
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")