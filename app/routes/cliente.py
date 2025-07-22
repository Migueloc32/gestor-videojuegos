# app/routes/cliente_route.py

from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

from starlette.responses import RedirectResponse

from app.schemas.cliente import ClienteCreate, ClienteResponse
from app.services import cliente as cliente_service
from models.cliente import Cliente
from services.cliente import eliminar_cliente

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "..", "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/menu", response_class=HTMLResponse)
async def menu_clientes(request: Request):
    return templates.TemplateResponse("menu_clientes.html", {"request": request})

@router.get("/formulario", response_class=HTMLResponse)
async def formulario_cliente(request: Request):
    return templates.TemplateResponse("formulario_cliente.html", {"request": request})

@router.post("/crear", response_class=HTMLResponse)
async def crear_cliente(
    request: Request,
    nombre: str = Form(...),
    direccion: str = Form(...),
    telefono: str = Form(...)
):
    cliente_data = ClienteCreate(
        nombre=nombre,
        direccion=direccion,
        telefono=telefono
    )
    nuevo = cliente_service.crear_cliente(cliente_data)

    return templates.TemplateResponse("registro_exitoso.html", {
        "request": request,
        "cliente": vars(nuevo)
    })

@router.get("/lista", response_class=HTMLResponse)
async def ver_clientes(request: Request):
    clientes = cliente_service.listar_clientes()
    return templates.TemplateResponse("lista_clientes.html", {
        "request": request,
        "clientes": clientes
    })


@router.post("/eliminar")
async def eliminar_cliente_route(cliente_id: int = Form(...)):
    eliminado = eliminar_cliente(cliente_id)
    if eliminado:
        print(f"Cliente con ID {cliente_id} eliminado exitosamente.")
    else:
        print(f"No se encontró cliente con ID {cliente_id}.")
    return RedirectResponse(url="/clientes/lista", status_code=303)

@router.put("/{cliente_id}/descuento", response_model=ClienteResponse)
def aplicar_descuento(cliente_id: int):
    cliente = cliente_service.aplicar_descuento(cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return vars(cliente)


@router.post("/eliminar-todos")
async def eliminar_todos():
    Cliente.clientes.clear()
    return RedirectResponse(url="/clientes/lista", status_code=303)


