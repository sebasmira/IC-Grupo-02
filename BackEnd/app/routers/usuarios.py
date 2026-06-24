"""
Router de endpoints para operaciones de usuarios.
Define todas las rutas HTTP de la API REST.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import app.crud as crud
import app.schemas as schemas
from app.database import get_db

# Crear router
router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "Usuario no encontrado"}}
)


@router.get("/", response_model=List[schemas.UsuarioResponse], summary="Listar todos los usuarios")
def listar_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtiene la lista completa de usuarios registrados.
    
    - **skip**: Número de registros a omitir (paginación)
    - **limit**: Máximo de registros a devolver
    """
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios


@router.get("/{usuario_id}", response_model=schemas.UsuarioResponse, summary="Obtener usuario por ID")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un usuario específico por su ID.
    
    - **usuario_id**: ID único del usuario
    """
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    
    if db_usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {usuario_id} no encontrado"
        )
    
    return db_usuario


@router.post("/", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED, summary="Crear nuevo usuario")
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario en el sistema.
    
    - **nombre**: Nombre del usuario
    - **apellido**: Apellido del usuario
    - **correo**: Email único del usuario
    - **telefono**: Número de teléfono
    - **edad**: Edad del usuario
    - **ciudad**: Ciudad de residencia
    - **rol**: Usuario o Administrador
    - **estado**: Activo o Inactivo
    - **fechaRegistro**: Fecha de registro
    """
    # Verificar si el correo ya existe
    db_usuario = crud.get_usuario_by_correo(db, correo=usuario.correo)
    
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado"
        )
    
    return crud.create_usuario(db=db, usuario=usuario)


@router.put("/{usuario_id}", response_model=schemas.UsuarioResponse, summary="Actualizar usuario")
def actualizar_usuario(
    usuario_id: int,
    usuario: schemas.UsuarioUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza la información de un usuario existente.
    
    - **usuario_id**: ID del usuario a actualizar
    - Solo se actualizan los campos enviados en el request
    """
    db_usuario = crud.update_usuario(db, usuario_id=usuario_id, usuario_update=usuario)
    
    if db_usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {usuario_id} no encontrado"
        )
    
    return db_usuario


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar usuario")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario del sistema.
    
    - **usuario_id**: ID del usuario a eliminar
    """
    eliminado = crud.delete_usuario(db, usuario_id=usuario_id)
    
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {usuario_id} no encontrado"
        )
    
    return None