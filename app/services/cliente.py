
from app.models.cliente import Cliente
from typing import List, Optional

def crear_cliente(data) -> Cliente:
    cliente = Cliente(data.nombre, data.direccion, data.telefono)
    Cliente.clientes.append(cliente)
    return cliente

def listar_clientes() -> List[Cliente]:
    return Cliente.clientes

def eliminar_cliente(cliente_id: int) -> bool:
    for cliente in Cliente.clientes:
        if cliente.id == cliente_id:
            Cliente.clientes.remove(cliente)
            return True
    return False

def aplicar_descuento(cliente_id: int) -> Optional[Cliente]:
    for cliente in Cliente.clientes:
        if cliente.id == cliente_id:
            cliente.aplicar_descuento()
            return cliente
    return None
# Precarga de clientes simulados
Cliente.clientes.extend([
    Cliente("Laura Martínez", "Calle 10 # 5-20", "3101234567"),
    Cliente("Carlos Gómez", "Carrera 45 # 22-15", "3117654321"),
    Cliente("Ana Torres", "Av. 80 # 35-40", "3128889999"),
    Cliente("Julián Ríos", "Calle 33 # 40-12", "3135678910"),
    Cliente("Mariana Díaz", "Carrera 21 # 14-33", "3147894561"),
    Cliente("Camilo Herrera", "Calle 50 # 10-77", "3156549870"),
    Cliente("Valentina Castro", "Av. Las Palmas # 33-66", "3163451234"),
    Cliente("Esteban López", "Carrera 30 # 25-10", "3178901234"),
    Cliente("Daniela Pérez", "Calle 7 # 45-11", "3181237890"),
    Cliente("Santiago Mejía", "Carrera 15 # 20-18", "3199876543"),
    Cliente("Isabela Ramírez", "Calle 44 # 50-30", "3206543210"),
    Cliente("Andrés Molina", "Carrera 8 # 55-12", "3214325678"),
    Cliente("Luisa Fernández", "Av. Nutibara # 60-90", "3225674321"),
    Cliente("Felipe Álvarez", "Calle 29 # 18-44", "3233456789"),
    Cliente("Natalia Castaño", "Carrera 70 # 33-45", "3246781234")
])
