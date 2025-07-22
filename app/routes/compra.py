import os
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.services import compra, videojuego, cliente

router = APIRouter(prefix="/compras")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../templates"))

@router.get("/menu")
async def menu_compras(request: Request):
    return templates.TemplateResponse("menu_compras.html", {"request": request})

@router.get("/nueva")
async def nueva_compra_form(request: Request):
    juegos = videojuego.listar_videojuegos()
    clientes = cliente.listar_clientes()
    return templates.TemplateResponse(
        "nueva_compra.html",
        {"request": request, "videojuegos": juegos, "clientes": clientes}
    )

@router.post("/nueva")
async def nueva_compra(request: Request, cliente_id: int = Form(...), videojuego_id: int = Form(...)):
    compra.registrar_compra(cliente_id, videojuego_id)
    return templates.TemplateResponse("compra_exitosa.html", {"request": request})

@router.get("/por_usuario")
async def compras_usuario_form(request: Request):
    clientes = cliente.listar_clientes()
    return templates.TemplateResponse("compras_usuario.html", {"request": request, "clientes": clientes})

@router.post("/por_usuario")
async def compras_usuario(request: Request, cliente_id: int = Form(...)):
    compras = compra.compras_por_usuario(cliente_id)
    clientes = cliente.listar_clientes()
    videojuegos = videojuego.listar_videojuegos()
    return templates.TemplateResponse(
        "lista_compras.html",
        {
            "request": request,
            "compras": compras,
            "clientes": clientes,
            "videojuegos": videojuegos
        }
    )

@router.get("/historial")
async def historial_compras(request: Request):
    compras = compra.listar_compras()
    clientes = cliente.listar_clientes()
    videojuegos = videojuego.listar_videojuegos()
    return templates.TemplateResponse(
        "lista_compras.html",
        {
            "request": request,
            "compras": compras,
            "clientes": clientes,
            "videojuegos": videojuegos
        }
    )