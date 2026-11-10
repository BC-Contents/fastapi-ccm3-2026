# 📚 API de Gestión de Librería con FastAPI y SQLite (Arquitectura MVC)

Este repositorio contiene un proyecto didáctico y funcional para una clase de formación en **FastAPI**, utilizando **SQLite** como base de datos y **SQLAlchemy** como ORM, estructurado bajo un patrón de arquitectura limpio basado en **MVC** (*Model-View-Controller*).

> **Nota:** Siguiendo las buenas prácticas de la industria, **todo el código está escrito en inglés**, mientras que esta guía y la documentación están redactadas en español para facilitar el aprendizaje paso a paso. La capa de presentación (*Frontend*) se desarrollará de forma independiente consumiendo esta API REST.

---

## 📑 Tabla de Contenidos
1. [Arquitectura y Estructura del Proyecto](#-arquitectura-y-estructura-del-proyecto)
2. [Requisitos Previos](#-requisitos-previos)
3. [Guía de Instalación Paso a Paso](#-guía-de-instalación-paso-a-paso)
4. [Construcción del Proyecto Paso a Paso (Archivo por Archivo)](#-construcción-del-proyecto-paso-a-paso-archivo-por-archivo)
5. [Cómo Arrancar el Servidor](#-cómo-arrancar-el-servidor)
6. [Pruebas Interactivas con Swagger UI](#-pruebas-interactivas-con-swagger-ui)
7. [Ejemplos de Peticiones y Respuestas (JSON)](#-ejemplos-de-peticiones-y-respuestas-json)
8. [Preguntas Frecuentes y Resolución de Problemas](#-preguntas-frecuentes-y-resolución-de-problemas)

---

## 🏗 Arquitectura y Estructura del Proyecto

El proyecto está organizado en módulos desacoplados para mantener el código ordenado y escalable:

```text
fastapi-class/
│
├── main.py                     # Punto de entrada de la aplicación FastAPI
│
├── config/
│   ├── __init__.py
│   └── config_variables.py     # Carga y centralización de variables de entorno (.env)
│
├── database/
│   ├── __init__.py
│   └── database.py             # Conexión SQLAlchemy, creación de motor y sesiones
│
├── models/
│   ├── __init__.py
│   └── libro_model.py          # Modelo ORM (SQLAlchemy) para la tabla 'books'
│
├── schemas/
│   ├── __init__.py
│   └── libro_schema.py         # Modelos de validación y serialización de datos (Pydantic)
│
├── controllers/
│   ├── __init__.py
│   └── libro_controller.py     # Lógica de negocio y consultas a base de datos (CRUD)
│
├── routes/
│   ├── __init__.py
│   └── routes.py               # Definición de endpoints HTTP y enrutador (APIRouter)
│
├── .env                        # Variables de entorno activas (opcional)
├── .env.example                # Plantilla de variables de entorno de ejemplo
├── .gitignore                  # Exclusión de carpetas temporales, venv y base de datos
├── requirements.txt            # Lista de dependencias del proyecto
└── db.sqlite3                  # Base de datos SQLite (se genera automáticamente al iniciar)
```

### ¿Cómo fluye una petición en esta arquitectura?
1. El cliente (navegador, frontend o Swagger) envía una petición HTTP a `routes/routes.py`.
2. Las rutas validan los datos de entrada usando los esquemas de Pydantic (`schemas/libro_schema.py`).
3. La ruta delega la operación al controlador (`controllers/libro_controller.py`) inyectando la sesión de base de datos (`database/database.py`).
4. El controlador interactúa con el modelo ORM (`models/libro_model.py`) para leer o escribir en SQLite.
5. El resultado se serializa y se devuelve en formato JSON según el esquema de respuesta.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.10 o superior** (puedes verificarlo ejecutando `python3 --version` o `python --version`).
- **pip** (administrador de paquetes de Python).
- Un editor de código como **VS Code**, **Cursor** o **PyCharm**.

---

## 🚀 Guía de Instalación Paso a Paso

### Paso 1: Clonar o situarte en el directorio del proyecto
Abre tu terminal y dirígete a la carpeta del proyecto:
```bash
cd /ruta/hacia/fastapi-class
```

### Paso 2: Crear el Entorno Virtual
Un entorno virtual aísla las librerías del proyecto del resto del sistema.
```bash
python3 -m venv venv
```
*(En Windows puedes usar `python -m venv venv`)*.

### Paso 3: Activar el Entorno Virtual
- **En macOS y Linux:**
  ```bash
  source venv/bin/activate
  ```
- **En Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **En Windows (Símbolo del sistema / CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```

> 💡 *Sabrás que está activado porque verás `(venv)` al principio de la línea de tu terminal.*

### Paso 4: Instalar las Dependencias

Con el entorno virtual activado, existen dos maneras de instalar las dependencias: **de forma manual (paquete por paquete)** o **de forma automática (mediante `requirements.txt`)**.

#### Opción A: Instalación Manual (Paso a Paso)
Si estás aprendiendo desde cero o creando el proyecto paso a paso, puedes instalar cada librería por separado con `pip`:

1. **Instalar FastAPI** (el framework web principal):
   ```bash
   pip install fastapi
   ```

2. **Instalar Uvicorn** (el servidor ASGI de alto rendimiento para ejecutar FastAPI):
   ```bash
   pip install "uvicorn[standard]"
   ```
   > 💡 *Nota: Usamos comillas `"uvicorn[standard]"` para evitar que la terminal (especialmente `zsh` en Mac o Linux) interprete los corchetes como caracteres especiales.*

3. **Instalar SQLAlchemy** (el ORM para gestionar la base de datos SQLite con objetos en Python):
   ```bash
   pip install sqlalchemy
   ```

4. **Instalar Pydantic** (para la validación estricta de datos y tipado de esquemas):
   ```bash
   pip install pydantic
   ```

5. **Instalar Python-Dotenv** (para leer las variables de configuración del archivo `.env`):
   ```bash
   pip install python-dotenv
   ```

*(O si prefieres instalar todos los paquetes manualmente en un solo comando):*
```bash
pip install fastapi "uvicorn[standard]" sqlalchemy pydantic python-dotenv
```

> 📌 **Tip para la clase:** Una vez instalados de forma manual, puedes congelar las versiones exactas en el archivo `requirements.txt` ejecutando:
> ```bash
> pip freeze > requirements.txt
> ```

---

#### Opción B: Instalación Automática (Recomendada si ya tienes el repositorio)
Si ya has clonado o descargado este proyecto y ya cuentas con el archivo `requirements.txt`, puedes instalar todo de una sola vez ejecutando:

```bash
pip install -r requirements.txt
```

Resumen de las dependencias instaladas:
- `fastapi`: Framework web moderno y asíncrono.
- `uvicorn[standard]`: Servidor para levantar la aplicación.
- `sqlalchemy`: ORM para interactuar con SQLite mediante clases y modelos.
- `pydantic`: Validación de datos para peticiones y respuestas.
- `python-dotenv`: Manejo de configuraciones por entorno.

### Paso 5: Configurar las Variables de Entorno (Opcional)
El proyecto ya cuenta con un archivo `.env` configurado. Si deseas personalizarlo, puedes copiar `.env.example`:
```bash
cp .env.example .env
```

Contenido de `.env`:
```env
APP_TITLE="Library Management API"
APP_VERSION="1.0.0"
APP_DESCRIPTION="A simple and educational REST API for managing books in a library using FastAPI and SQLite."
DATABASE_NAME="db.sqlite3"
DATABASE_URL="sqlite:///./db.sqlite3"
```

---

## 🛠 Construcción del Proyecto Paso a Paso (Archivo por Archivo)

A continuación, construiremos el proyecto en el orden lógico en que se relacionan las dependencias, explicando el **porqué** y el **cómo** de cada línea de código.

---

### 🟢 Paso 1: Configuración del Proyecto (`config/config_variables.py`)

#### ¿Por qué este archivo primero?
Toda aplicación profesional debe desacoplar sus variables de configuración (credenciales, claves de API, URLs de base de datos, títulos) del código fuente. En lugar de exponer o repetir manualmente cada variable en el código, este archivo carga dinámicamente todas las variables definidas en `.env` dentro del espacio de nombres del módulo.

#### Código (`config/config_variables.py`):
```python
from dotenv import dotenv_values

# Load all variables from .env dynamically into this module's namespace
globals().update(dotenv_values(".env"))
```

#### Explicación paso a paso:
1. `dotenv_values(".env")`: Lee el archivo `.env` en la raíz del proyecto y devuelve un diccionario con todas las claves y valores definidos allí, sin exponer valores sensibles ni valores por defecto en el código fuente.
2. `globals().update(...)`: Inyecta automáticamente cada clave del `.env` como una variable global dentro del módulo `config_variables`. Así puedes importar directamente cualquier variable (como `APP_TITLE`, `DATABASE_URL`, etc.) sin tener que declararla ni repetirla una por una.

---

### 🟢 Paso 2: Conexión y Sesiones de Base de Datos (`database/database.py`)

#### ¿Por qué este archivo?
Necesitamos configurar el motor (*Engine*) de SQLAlchemy y la factoría de sesiones que permitirá a la API abrir y cerrar transacciones con SQLite.

#### Código (`database/database.py`):
```python
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from config.config_variables import DATABASE_URL

# Motor de conexión con SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Factoría generadora de sesiones por cada petición HTTP
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Clase base para los modelos declarativos de SQLAlchemy
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Dependencia generadora que abre una sesión de base de datos
    y garantiza que se cierre al finalizar la petición HTTP.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### Explicación paso a paso:
1. `connect_args={"check_same_thread": False}`: **Crucial para SQLite**. Por defecto, SQLite solo permite interactuar desde el mismo hilo donde se creó. FastAPI es asíncrono y multitarea, por lo que esta bandera permite compartir la conexión de forma segura entre hilos de FastAPI.
2. `SessionLocal`: Es una clase constructora de sesiones. `autocommit=False` garantiza que nosotros controlemos explícitamente cuándo guardar datos con `commit()`.
3. `Base = declarative_base()`: Es la clase padre que usará nuestro modelo ORM para registrar la tabla y sus columnas.
4. `get_db()`: Utiliza la palabra clave `yield`. Cuando entra una petición, abre la sesión con `db = SessionLocal()`, entrega la sesión a la ruta, y gracias al bloque `finally: db.close()`, **siempre se cierra la conexión**, evitando fugas de memoria o bloqueos en la base de datos.

---

### 🟢 Paso 3: Modelo de Datos ORM (`models/libro_model.py`)

#### ¿Por qué este archivo?
Define cómo es la tabla en la base de datos a nivel relacional. SQLAlchemy traducirá esta clase de Python a sentencias SQL `CREATE TABLE books (...)`.

#### Código (`models/libro_model.py`):
```python
from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base


class Book(Base):
    """
    Modelo ORM de SQLAlchemy que representa la tabla 'books'.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(150), nullable=False, index=True)
    author = Column(String(100), nullable=False, index=True)
    pages = Column(Integer, nullable=True)
    is_available = Column(Boolean, default=True, nullable=False)

    def __repr__(self) -> str:
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"
```

#### Explicación paso a paso:
1. `class Book(Base)`: Hereda de `Base` para que SQLAlchemy sepa que es una tabla gestionada.
2. `__tablename__ = "books"`: Nombre exacto de la tabla física en SQLite.
3. `id`: Entero, clave primaria autoincremental (`primary_key=True, autoincrement=True`).
4. `title` y `author`: Cadenas de texto obligatorias (`nullable=False`) con índices (`index=True`) para búsquedas rápidas.
5. `pages`: Entero opcional (`nullable=True`).
6. `is_available`: Booleano para el estado de disponibilidad del libro con valor predeterminado `True`.

---

### 🟢 Paso 4: Esquemas de Validación y Tipado (`schemas/libro_schema.py`)

#### ¿Por qué este archivo?
Existe una diferencia clave en FastAPI:
- **Modelo ORM (SQLAlchemy):** Modela cómo se guardan los datos en el disco (SQLite).
- **Esquema Pydantic:** Modela cómo viajan los datos por la red (JSON). Valida tipos, límites, valores obligatorios y oculta campos sensibles.

#### Código (`schemas/libro_schema.py`):
```python
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    """
    Esquema base con los atributos comunes del libro.
    """
    title: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Title of the book",
        examples=["Don Quixote"]
    )
    author: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Author of the book",
        examples=["Miguel de Cervantes"]
    )
    pages: Optional[int] = Field(
        None,
        gt=0,
        description="Total page count of the book",
        examples=[863]
    )
    is_available: bool = Field(
        default=True,
        description="Flag indicating if the book is currently available in the library",
        examples=[True]
    )


class BookCreate(BookBase):
    """
    Esquema para crear un nuevo libro (POST).
    """
    pass


class BookUpdate(BaseModel):
    """
    Esquema para actualizar un libro existente (PUT).
    Todos los campos son opcionales.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=150)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    pages: Optional[int] = Field(None, gt=0)
    is_available: Optional[bool] = Field(None)


class BookResponse(BookBase):
    """
    Esquema de salida devuelto al cliente. Incluye el ID asignado por la base de datos.
    """
    id: int = Field(..., description="Unique database identifier", examples=[1])

    # Habilita la lectura directa desde objetos ORM de SQLAlchemy
    model_config = ConfigDict(from_attributes=True)
```

#### Explicación paso a paso:
1. `Field(...)`: Los puntos suspensivos `...` indican que el campo es **obligatorio**.
2. `gt=0`: Validación automática de Pydantic para asegurar que las páginas sean un número mayor a 0 (*greater than 0*).
3. `BookCreate`: Hereda de `BookBase` porque al crear un libro se requieren los datos base pero **no** el `id` (que lo genera la base de datos).
4. `BookUpdate`: Define todos los campos como `Optional` para permitir actualizar solo el título, solo las páginas o varios campos a la vez.
5. `model_config = ConfigDict(from_attributes=True)`: Permite a Pydantic leer atributos de un objeto de SQLAlchemy (ej: `book.title`) y serializarlo a JSON automáticamente.

---

### 🟢 Paso 5: Controlador con Lógica de Negocio y Control de Errores (`controllers/libro_controller.py`)

#### ¿Por qué este archivo?
Siguiendo la arquitectura MVC, las rutas no deben contener consultas SQL directas ni lógica compleja. El controlador concentra las operaciones CRUD y el **manejo riguroso de errores y transacciones**.

#### Código (`controllers/libro_controller.py`):
```python
from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models.libro_model import Book
from schemas.libro_schema import BookCreate, BookUpdate


def get_all_books(db: Session, skip: int = 0, limit: int = 100) -> List[Book]:
    """
    Obtiene el listado paginado de libros con control de errores de base de datos.
    """
    try:
        return db.query(Book).offset(skip).limit(limit).all()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error while retrieving books: {str(error)}"
        )


def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
    """
    Busca un libro por su ID único.
    """
    try:
        return db.query(Book).filter(Book.id == book_id).first()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error while retrieving book {book_id}: {str(error)}"
        )


def create_book(db: Session, book_data: BookCreate) -> Book:
    """
    Inserta un nuevo libro en la base de datos con transacción segura y rollback ante fallos.
    """
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        pages=book_data.pages,
        is_available=book_data.is_available,
    )
    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except SQLAlchemyError as error:
        db.rollback()  # Revierte la transacción para no dejar la sesión corrupta
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error while creating book: {str(error)}"
        )


def update_book(db: Session, book_id: int, book_data: BookUpdate) -> Optional[Book]:
    """
    Actualiza los campos modificados de un libro existente.
    """
    existing_book = get_book_by_id(db, book_id)
    if not existing_book:
        return None

    # Extrae únicamente los campos enviados en la petición
    update_fields = book_data.model_dump(exclude_unset=True)
    for field, value in update_fields.items():
        setattr(existing_book, field, value)

    try:
        db.commit()
        db.refresh(existing_book)
        return existing_book
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error while updating book {book_id}: {str(error)}"
        )


def delete_book(db: Session, book_id: int) -> bool:
    """
    Elimina un libro de la base de datos por su ID.
    """
    existing_book = get_book_by_id(db, book_id)
    if not existing_book:
        return False

    try:
        db.delete(existing_book)
        db.commit()
        return True
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error while deleting book {book_id}: {str(error)}"
        )
```

#### Explicación del Control de Errores y Transacciones:
1. **`db.rollback()`**: Si ocurre un fallo en `db.commit()` (por ejemplo, base de datos bloqueada, disco sin espacio o error de concurrencia), el bloque `except SQLAlchemyError` revierte la operación. Esto evita que la sesión quede en estado inconsistente.
2. **`raise HTTPException(500, ...)`**: Informa de forma estructurada al cliente de la API que ocurrió un error interno de servidor en lugar de que el servidor se caiga silenciosamente.
3. **`book_data.model_dump(exclude_unset=True)`**: Solo actualiza las propiedades que el usuario envió explícitamente, sin sobreescribir con `None` los campos que no se querían modificar.

---

### 🟢 Paso 6: Rutas y Endpoints HTTP (`routes/routes.py`)

#### ¿Por qué este archivo?
Define la interfaz REST accesible mediante peticiones HTTP. Asigna a cada URL su verbo HTTP (`GET`, `POST`, `PUT`, `DELETE`), valida entradas mediante dependencias y esquemas, y responde con los códigos de estado HTTP correctos.

#### Código (`routes/routes.py`):
```python
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.libro_schema import BookCreate, BookUpdate, BookResponse
import controllers.libro_controller as controller

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get(
    "/",
    response_model=List[BookResponse],
    summary="Get all books",
    description="Retrieve a list of books with optional pagination."
)
def read_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of records to return"),
    db: Session = Depends(get_db)
):
    return controller.get_all_books(db=db, skip=skip, limit=limit)


@router.get(
    "/{book_id}",
    response_model=BookResponse,
    summary="Get a book by ID",
    description="Retrieve specific details of a single book by its ID."
)
def read_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = controller.get_book_by_id(db=db, book_id=book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return book


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    description="Add a new book entry to the library catalog."
)
def create_new_book(
    book_data: BookCreate,
    db: Session = Depends(get_db)
):
    return controller.create_book(db=db, book_data=book_data)


@router.put(
    "/{book_id}",
    response_model=BookResponse,
    summary="Update an existing book",
    description="Update one or more attributes of an existing book."
)
def update_existing_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db)
):
    updated_book = controller.update_book(db=db, book_id=book_id, book_data=book_data)
    if not updated_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return updated_book


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a book",
    description="Permanently remove a book from the library by its ID."
)
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    deleted = controller.delete_book(db=db, book_id=book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return None
```

#### Explicación de los Códigos de Estado y Manejo de Errores:
- **`200 OK`**: Respuesta estándar con datos (ej: `GET /books/`).
- **`201 CREATED`**: Indica que un nuevo recurso se creó exitosamente (`POST /books/`).
- **`204 NO CONTENT`**: Indica que el recurso se eliminó correctamente y no hay cuerpo que retornar (`DELETE /books/{id}`).
- **`404 NOT FOUND`**: Se lanza con `HTTPException(404, ...)` si el libro solicitado no existe.
- **`422 UNPROCESSABLE ENTITY`**: FastAPI lo genera automáticamente si los datos enviados no coinciden con los tipos definidos en los esquemas Pydantic.
- **`Depends(get_db)`**: Inyecta una sesión limpia de base de datos para la petición y la cierra al finalizar.

---

### 🟢 Paso 7: Entrada Principal y Arranque Automático (`main.py`)

#### ¿Por qué este archivo?
Es el punto de entrada de la aplicación. Aquí ensamblamos FastAPI, configuramos **CORS** para que cualquier frontend pueda conectarse sin problemas de seguridad de origen cruzado, y definimos el evento `lifespan` para que el archivo `db.sqlite3` se cree de forma automática.

#### Código (`main.py`):
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.config_variables import APP_TITLE, APP_VERSION, APP_DESCRIPTION
from database.database import Base, engine
from routes.routes import router as books_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestor del ciclo de vida (Lifespan).
    Crea las tablas en SQLite automáticamente al arrancar la aplicación.
    """
    # Base.metadata.create_all comprueba si la tabla 'books' existe; si no, la crea
    Base.metadata.create_all(bind=engine)
    yield
    # Lógica de cierre o limpieza (si fuera necesaria)


# Inicialización de la aplicación FastAPI
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    lifespan=lifespan
)

# Configuración de CORS (permite que el frontend independiente haga peticiones)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar el router de libros
app.include_router(books_router)


@app.get("/", tags=["Health Check"])
def read_root():
    """
    Ruta raíz para comprobar que el servidor está online y redirigir a la documentación.
    """
    return {
        "status": "online",
        "message": f"Welcome to {APP_TITLE}",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
```

#### Explicación paso a paso:
1. `@asynccontextmanager async def lifespan(app: FastAPI)`: Es la forma moderna recomendada por FastAPI para ejecutar tareas de inicio y cierre.
2. `Base.metadata.create_all(bind=engine)`: **¡Aquí ocurre la magia de SQLite!** Inspecciona todas las clases que heredan de `Base` (en nuestro caso `Book`), se conecta a `db.sqlite3` y ejecuta la sentencia `CREATE TABLE IF NOT EXISTS books (...)`. Por eso el archivo `db.sqlite3` se crea solo la primera vez que arrancas el servidor.
3. `CORSMiddleware`: Dado que el frontend se programará por separado, esta configuración previene errores de política *Cross-Origin Resource Sharing* cuando una aplicación web en otro puerto (por ejemplo `localhost:3000` o `localhost:5173`) intente consultar la API.

---

## ⚡ Cómo Arrancar el Servidor

Asegúrate de tener el entorno virtual activado y ejecuta:

```bash
uvicorn main:app --reload
```

### ¿Qué significan estos argumentos?
- `main`: Nombre del archivo `main.py`.
- `app`: Instancia de `FastAPI()` creada dentro de `main.py`.
- `--reload`: Modo de recarga en caliente; el servidor se reinicia automáticamente cada vez que guardas cambios en el código.

Verás una salida similar a esta:
```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...]
INFO:     Application startup complete.
```

> 🎯 Al arrancar, observarás que el archivo **`db.sqlite3`** se crea automáticamente en la raíz de tu proyecto.

---

## 🧪 Pruebas Interactivas con Swagger UI

FastAPI incluye documentación interactiva generada automáticamente. Con el servidor en ejecución, abre tu navegador web y visita:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** (Swagger UI)

O la alternativa interactiva en:
👉 **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)** (ReDoc)

Desde Swagger UI puedes probar cada endpoint haciendo clic en **"Try it out"**, completando los datos y pulsando **"Execute"**.

---

## 📦 Ejemplos de Peticiones y Respuestas (JSON)

### 1. Crear un nuevo libro (`POST /books/`)
- **URL**: `http://127.0.0.1:8000/books/`
- **Método**: `POST`
- **Cuerpo (Body JSON)**:
```json
{
  "title": "Cien años de soledad",
  "author": "Gabriel García Márquez",
  "pages": 417,
  "is_available": true
}
```
- **Respuesta (Código 201 Created)**:
```json
{
  "title": "Cien años de soledad",
  "author": "Gabriel García Márquez",
  "pages": 417,
  "is_available": true,
  "id": 1
}
```

---

### 2. Listar todos los libros (`GET /books/`)
- **URL**: `http://127.0.0.1:8000/books/?skip=0&limit=10`
- **Método**: `GET`
- **Respuesta (Código 200 OK)**:
```json
[
  {
    "title": "Cien años de soledad",
    "author": "Gabriel García Márquez",
    "pages": 417,
    "is_available": true,
    "id": 1
  }
]
```

---

### 3. Obtener un libro por su ID (`GET /books/{book_id}`)
- **URL**: `http://127.0.0.1:8000/books/1`
- **Método**: `GET`
- **Respuesta (Código 200 OK)**:
```json
{
  "title": "Cien años de soledad",
  "author": "Gabriel García Márquez",
  "pages": 417,
  "is_available": true,
  "id": 1
}
```
*(Si no existe, devuelve `404 Not Found`)*:
```json
{
  "detail": "Book with id 99 not found"
}
```

---

### 4. Actualizar un libro (`PUT /books/{book_id}`)
- **URL**: `http://127.0.0.1:8000/books/1`
- **Método**: `PUT`
- **Cuerpo (Body JSON)** (solo necesitas enviar los campos a modificar):
```json
{
  "pages": 471,
  "is_available": false
}
```
- **Respuesta (Código 200 OK)**:
```json
{
  "title": "Cien años de soledad",
  "author": "Gabriel García Márquez",
  "pages": 471,
  "is_available": false,
  "id": 1
}
```

---

### 5. Eliminar un libro (`DELETE /books/{book_id}`)
- **URL**: `http://127.0.0.1:8000/books/1`
- **Método**: `DELETE`
- **Respuesta**: Código HTTP `204 No Content` (sin contenido en el cuerpo).

---

## ❓ Preguntas Frecuentes y Resolución de Problemas

#### 1. ¿Dónde puedo ver los datos guardados en SQLite?
Puedes utilizar extensiones de VS Code como **SQLite Viewer** o herramientas de escritorio gratuitas como **DB Browser for SQLite** para inspeccionar visualmente el archivo `db.sqlite3`.

#### 2. ¿Cómo reiniciar la base de datos desde cero?
Si deseas borrar todos los registros y reiniciar las tablas, simplemente detén el servidor (`Ctrl + C`), elimina el archivo `db.sqlite3` y vuelve a arrancar con `uvicorn main:app --reload`.

#### 3. Error `ModuleNotFoundError: No module named 'fastapi'`
Asegúrate de haber activado el entorno virtual (`source venv/bin/activate` o `.\venv\Scripts\activate`) antes de ejecutar el servidor.
