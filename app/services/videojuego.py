from app.models.videojuego import Videojuego

def crear_videojuego(data):
    videojuego = Videojuego(data['nombre'], data['genero'], data['precio'])
    Videojuego.videojuegos.append(videojuego)
    return videojuego

def listar_videojuegos():
    return Videojuego.videojuegos

def eliminar_videojuego(videojuego_id):
    for videojuego in Videojuego.videojuegos:
        if videojuego.id == videojuego_id:
            Videojuego.videojuegos.remove(videojuego)
            return True
    return False

def aplicar_descuento(videojuego_id, porcentaje):
    for videojuego in Videojuego.videojuegos:
        if videojuego.id == videojuego_id:
            videojuego.aplicar_descuento(porcentaje)
            return videojuego
    return None