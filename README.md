FastAPI + SQLAlchemy CRUD
Este proyecto es una API REST completa construida con Python y FastAPI, diseñada para demostrar cómo integrar una base de datos relacional utilizando SQLAlchemy (ORM). Implementa operaciones CRUD (Crear, Leer, Actualizar, Borrar) para gestionar usuarios y elementos, con relaciones entre tablas y hashing de contraseñas.

🚀 Tecnologías Utilizadas
FastAPI: Framework web moderno y de alto rendimiento para construir APIs.

SQLAlchemy: ORM (Object Relational Mapper) para interactuar con la base de datos usando objetos Python.

Pydantic: Validación de datos y gestión de esquemas.

Passlib & Bcrypt: Para el hashing seguro de contraseñas.

SQLite: Base de datos por defecto (fácilmente migrable a PostgreSQL o MySQL).

📂 Estructura del Proyecto
El proyecto sigue una arquitectura modular y escalable:

main.py: Punto de entrada de la aplicación y definición de endpoints (rutas).

models.py: Modelos de la base de datos (tablas SQLAlchemy).

schemas.py: Esquemas de Pydantic para validación de datos (request/response).

crud.py: Lógica de negocio y operaciones directas a la base de datos.

database.py: Configuración de la conexión a la base de datos (SessionLocal y engine).

🛠️ Instalación y Uso
Clonar el repositorio:

Bash

git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
Crear un entorno virtual:

Bash

python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
Instalar dependencias: Asegúrate de instalar las versiones compatibles (especialmente bcrypt):

Bash

pip install fastapi uvicorn sqlalchemy pydantic passlib "bcrypt==3.2.0"
Ejecutar el servidor:

Bash

uvicorn main:app --reload
Acceder a la documentación: Abre tu navegador en http://127.0.0.1:8000/docs. Verás la interfaz interactiva de Swagger UI generada automáticamente.

🔗 Endpoints Principales
Usuarios (/users)
POST /users/: Crear un nuevo usuario (con contraseña hasheada).

GET /users/: Obtener lista de usuarios.

GET /users/{user_id}: Obtener un usuario específico.

DELETE /users/{user_id}: Eliminar un usuario (borrado en cascada de sus items).

Items (/items)
POST /users/{user_id}/items/: Crear un item asociado a un usuario.

GET /items/: Listar todos los items.

PUT /items/{item_id}: Actualizar la información de un item.

DELETE /items/{item_id}: Eliminar un item.

🛡️ Seguridad
El proyecto implementa seguridad básica mediante Hashing de contraseñas. Las contraseñas nunca se guardan en texto plano en la base de datos; se utiliza el algoritmo Bcrypt antes de almacenarlas.
