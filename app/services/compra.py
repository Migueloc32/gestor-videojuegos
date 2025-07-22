from app.models.compra import Compra

def registrar_compra(cliente_id, videojuego_id):
    compra = Compra(cliente_id, videojuego_id)
    Compra.compras.append(compra)
    return compra

def listar_compras():
    return Compra.compras

def compras_por_usuario(cliente_id):
    return [c for c in Compra.compras if c.cliente_id == cliente_id]