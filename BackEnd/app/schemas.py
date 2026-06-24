"""
Schemas Pydantic para validación de datos.
Define cómo se reciben y envían los datos en la API.
"""

from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional


class UsuarioBase(BaseModel):
    """Schema base con campos comunes"""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del usuario")
    apellido: str = Field(..., min_length=1, max_length=100, description="Apellido del usuario")
    correo: EmailStr = Field(..., description="Correo electrónico único")
    telefono: str = Field(..., min_length=7, max_length=20, description="Número de teléfono")
    edad: int = Field(..., ge=1, le=120, description="Edad del usuario")
    ciudad: str = Field(..., min_length=1, max_length=100, description="Ciudad de residencia")
    rol: str = Field(default="Usuario", description="Rol: Usuario o Administrador")
    estado: str = Field(default="Activo", description="Estado: Activo o Inactivo")
    fechaRegistro: date = Field(..., description="Fecha de registro")


class UsuarioCreate(UsuarioBase):
    """Schema para crear un usuario (request body)"""
    pass


class UsuarioUpdate(BaseModel):
    """Schema para actualizar un usuario (campos opcionales)"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, min_length=7, max_length=20)
    edad: Optional[int] = Field(None, ge=1, le=120)
    ciudad: Optional[str] = Field(None, min_length=1, max_length=100)
    rol: Optional[str] = None
    estado: Optional[str] = None
    fechaRegistro: Optional[date] = None


class UsuarioResponse(UsuarioBase):
    """Schema para respuesta (incluye ID)"""
    id: int

    class Config:
        """Configuración para trabajar con ORM"""
        from_attributes = True  # Antes era orm_mode = True en Pydantic v1