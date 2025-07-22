# app/schemas/cliente.py

from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombre: str
    direccion: str
    telefono: str

class ClienteResponse(ClienteCreate):
    id: int
