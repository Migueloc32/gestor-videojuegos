# Gestor de Videojuegos - Documentación de la API

Este sistema permite gestionar una tienda de videojuegos, incluyendo el manejo de clientes, videojuegos y compras. La API implementada con **FastAPI** permite realizar operaciones CRUD, consultar listados y realizar transformaciones sobre los recursos.

---
##   Felipe Aristizabal|faristizabalg@unal.edu.co 
## **David Gavalo Molina|dgavalo@unal.edu.co**
## **Juan Miguel Ochoa Agudelo| jochoaag@unal.edu.co**

## **Requisitos del sistema**

- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2 (para vistas, si usas plantillas)
- (Opcional) pytest para pruebas unitarias

---

## **Casos de Uso (Ejemplos Propuestos)**

### 1. **Gestión de Videojuegos**
- **Listado de videojuegos:** Obtener el listado completo de videojuegos registrados.
- **Creación de videojuegos:** Agregar un nuevo videojuego a la tienda.
- **Eliminación de videojuegos:** Quitar un videojuego de la tienda.
- **Transformación:** Modificar el precio de un videojuego (aplicar descuentos u ofertas).

### 2. **Gestión de Clientes**
- **Listado de clientes:** Consultar todos los clientes registrados.
- **Creación de clientes:** Registrar un nuevo cliente.
- **Eliminación de clientes:** Eliminar un cliente del sistema.
- **Transformación:** Modificar la información de un cliente (por ejemplo, actualizar dirección o teléfono).

### 3. **Gestión de Compras**
- **Listado de compras:** Ver el historial de compras realizadas.
- **Creación de compra:** Registrar una nueva compra asociando un cliente y un videojuego.
- **Eliminación de compra:** Eliminar una compra del historial.
- **Transformación:** Modificar la fecha o el cliente asociado a una compra (opcional).

---

## **Endpoints principales de la API**

> Todos los endpoints están documentados automáticamente en **Swagger UI** en `/docs` y en Redoc en `/redoc` cuando corres el servidor FastAPI.

### **Videojuegos**
- `GET /videojuegos/`  
  Listar todos los videojuegos.
- `POST /videojuegos/`  
  Crear un nuevo videojuego.
- `DELETE /videojuegos/{videojuego_id}`  
  Eliminar un videojuego.
- `PUT /videojuegos/{videojuego_id}/precio`  
  Modificar el precio de un videojuego.

### **Clientes**
- `GET /clientes/`  
  Listar todos los clientes.
- `POST /clientes/`  
  Crear un nuevo cliente.
- `DELETE /clientes/{cliente_id}`  
  Eliminar un cliente.
- `PUT /clientes/{cliente_id}`  
  Modificar información de un cliente.

### **Compras**
- `GET /compras/`  
  Listar historial de compras.
- `POST /compras/`  
  Registrar una nueva compra.
- `DELETE /compras/{compra_id}`  
  Eliminar una compra.
- `PUT /compras/{compra_id}`  
  Modificar datos de una compra.

---

## **Breve Descripción de Funcionalidades**

- **Videojuegos:** Permite registrar, consultar, eliminar y actualizar videojuegos, incluyendo la posibilidad de cambiar precios (aplicar descuentos).
- **Clientes:** Permite registrar, consultar, eliminar y actualizar la información de los clientes de la tienda.
- **Compras:** Permite registrar, consultar, eliminar y editar compras, asociando un cliente y un videojuego en cada transacción.

---

## **Pruebas Unitarias**

Las pruebas unitarias se implementan usando `pytest` y cubren los casos de uso principales:
- Crear, listar, eliminar y modificar videojuegos.
- Crear, listar, eliminar y modificar clientes.
- Crear, listar, eliminar y modificar compras.

---

## **Acceso a la documentación interactiva**

Cuando el servidor está corriendo, accede a:
- [http://localhost:8000/docs](http://localhost:8001/docs) (Swagger UI)
- [http://localhost:8000/redoc](http://localhost:8001/redoc) (Redoc)

---

## **Ejemplo de ejecución**

```bash
uvicorn main:app --reload
