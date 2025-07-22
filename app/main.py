import os

import app
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.routes import cliente
from app.routes import cliente, videojuego

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

app.include_router(cliente.router)
app.include_router(videojuego.router)

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})
