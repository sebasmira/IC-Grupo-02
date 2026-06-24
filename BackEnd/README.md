# Backend - Sistema de Usuarios

API REST con FastAPI para gestión de usuarios.

## Tecnologías
- **FastAPI**: Framework web moderno
- **SQLAlchemy**: ORM para bases de datos
- **SQLite**: Base de datos (configurable)
- **Pydantic**: Validación de datos

## Instalación

1. Crear entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env según necesidades
```

4. Ejecutar servidor:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

## Endpoints

- `GET /usuarios` - Listar todos los usuarios
- `POST /usuarios` - Crear usuario
- `GET /usuarios/{id}` - Obtener usuario por ID
- `PUT /usuarios/{id}` - Actualizar usuario
- `DELETE /usuarios/{id}` - Eliminar usuario

## Documentación API
- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc