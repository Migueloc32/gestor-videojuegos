# tests/test_cliente.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_cliente():
    response = client.post("/clientes/", json={
        "nombre": "Juan",
        "direccion": "Calle 1",
        "telefono": "3000000000"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Juan"
    assert data["id"] == 1

def test_listar_clientes():
    response = client.get("/clientes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["nombre"] == "Juan"

def test_aplicar_descuento():
    response = client.put("/clientes/1/descuento")
    assert response.status_code == 200
    assert "(DESCUENTO APLICADO)" in response.json()["nombre"]

def test_eliminar_cliente():
    response = client.delete("/clientes/1")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Cliente eliminado"

def test_eliminar_inexistente():
    response = client.delete("/clientes/999")
    assert response.status_code == 404
