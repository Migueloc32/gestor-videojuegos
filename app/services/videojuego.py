from app.models.videojuego import Videojuego

# Inicializar base de datos si está vacía
if not Videojuego.videojuegos:
    juegos_iniciales = [
        ("The Legend of Zelda: Breath of the Wild", "Aventura", 59.99),
        ("Super Mario Odyssey", "Plataformas", 49.99),
        ("God of War", "Acción", 39.99),
        ("Red Dead Redemption 2", "Acción/Aventura", 59.99),
        ("Minecraft", "Sandbox", 29.99),
        ("Fortnite", "Battle Royale", 0.00),
        ("FIFA 22", "Deportes", 49.99),
        ("Call of Duty: Modern Warfare", "Shooter", 59.99),
        ("Among Us", "Party", 4.99),
        ("Grand Theft Auto V", "Acción/Aventura", 29.99),
        ("Animal Crossing: New Horizons", "Simulación", 59.99),
        ("Hollow Knight", "Metroidvania", 14.99),
        ("Stardew Valley", "Simulación", 14.99),
        ("Cyberpunk 2077", "RPG", 49.99),
        ("Celeste", "Plataformas", 19.99),
        ("Pokémon Sword", "RPG", 59.99),
        ("Overwatch", "Shooter", 39.99),
        ("Sekiro: Shadows Die Twice", "Acción/Aventura", 49.99),
        ("Mario Kart 8 Deluxe", "Carreras", 59.99),
        ("Dark Souls III", "RPG", 39.99),
        ("Fall Guys", "Party", 19.99),
        ("The Witcher 3: Wild Hunt", "RPG", 39.99),
        ("Rocket League", "Deportes", 19.99),
        ("DOOM Eternal", "Shooter", 59.99),
    ]
    for nombre, genero, precio in juegos_iniciales:
        Videojuego.videojuegos.append(Videojuego(nombre, genero, precio))

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