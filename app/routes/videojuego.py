import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services import videojuego

router = APIRouter(prefix="/videojuegos")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../templates"))

@router.get("/menu")
async def menu_videojuegos(request: Request):
    return templates.TemplateResponse("menu_videojuegos.html", {"request": request})

@router.get("/")
def listar():
    return [vars(v) for v in videojuego.listar_videojuegos()]

@router.post("/")
def crear(data: dict):
    v = videojuego.crear_videojuego(data)
    return vars(v)

@router.delete("/{videojuego_id}")
def eliminar(videojuego_id: int):
    if videojuego.eliminar_videojuego(videojuego_id):
        return {"mensaje": "Videojuego eliminado"}
    return {"mensaje": "No encontrado"}

@router.put("/{videojuego_id}/descuento")
def descuento(videojuego_id: int, porcentaje: float):
    v = videojuego.aplicar_descuento(videojuego_id, porcentaje)
    if v:
        return vars(v)
    return {"mensaje": "No encontrado"}