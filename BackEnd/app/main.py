"""
Aplicación principal FastAPI.
Punto de entrada del backend, configura CORS, routers y base de datos.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from app.database import engine, Base
from app.routers import usuarios

# Cargar variables de entorno
load_dotenv()

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear aplicación FastAPI
app = FastAPI(
    title="Sistema de Usuarios API",
    description="API REST para gestión de usuarios con FastAPI y SQLAlchemy",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS (permitir frontend)
origins = os.getenv("CORS_ORIGINS", "http://localhost:5500").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(usuarios.router)


@app.get("/", tags=["Health Check"])
def root():
    """
    Endpoint raíz para verificar que la API está funcionando.
    """
    return {
        "mensaje": "API de Usuarios funcionando correctamente",
        "version": "1.0.0",
        "documentacion": "/docs"
    }


@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Health check para verificar el estado del servicio.
    """
    return {"status": "healthy", "service": "usuarios-api"}