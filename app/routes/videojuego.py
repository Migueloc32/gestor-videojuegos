import os
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.services import videojuego

router = APIRouter(prefix="/videojuegos")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../templates"))

@router.get("/menu")
async def menu_videojuegos(request: Request):
    return templates.TemplateResponse("menu_videojuegos.html", {"request": request})

@router.get("/lista")
async def lista_videojuegos(request: Request):
    videojuegos_lista = videojuego.listar_videojuegos()
    return templates.TemplateResponse(
        "lista_videojuegos.html",
        {"request": request, "videojuegos": videojuegos_lista}
    )

@router.get("/nuevo")
async def nuevo_videojuego_form(request: Request):
    return templates.TemplateResponse("nuevo_videojuego.html", {"request": request})

@router.post("/nuevo")
async def nuevo_videojuego(
    request: Request,
    nombre: str = Form(...),
    genero: str = Form(...),
    precio: float = Form(...)
):
    videojuego.crear_videojuego({"nombre": nombre, "genero": genero, "precio": precio})
    return RedirectResponse(url="/videojuegos/lista", status_code=303)

@router.get("/eliminar")
async def eliminar_videojuego_form(request: Request):
    return templates.TemplateResponse("eliminar_videojuego.html", {"request": request})

@router.post("/eliminar")
async def eliminar_videojuego(request: Request, id: int = Form(...)):
    resultado = videojuego.eliminar_videojuego(id)
    mensaje = "Videojuego eliminado" if resultado else "ID no encontrado"
    videojuegos_lista = videojuego.listar_videojuegos()
    return templates.TemplateResponse(
        "lista_videojuegos.html",
        {"request": request, "videojuegos": videojuegos_lista, "mensaje": mensaje}
    )

@router.get("/descuento")
async def descuento_videojuego_form(request: Request):
    return templates.TemplateResponse("descuento_videojuego.html", {"request": request})

@router.post("/descuento")
async def descuento_videojuego(request: Request, id: int = Form(...), porcentaje: float = Form(...)):
    v = videojuego.aplicar_descuento(id, porcentaje)
    mensaje = "Descuento aplicado" if v else "ID no encontrado"
    videojuegos_lista = videojuego.listar_videojuegos()
    return templates.TemplateResponse(
        "lista_videojuegos.html",
        {"request": request, "videojuegos": videojuegos_lista, "mensaje": mensaje}
    )

# Endpoints API JSON
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