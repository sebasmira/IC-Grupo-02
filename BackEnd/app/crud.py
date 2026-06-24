"""
Operaciones CRUD (Create, Read, Update, Delete) para usuarios.
Maneja todas las operaciones de base de datos.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

import app.models as models
import app.schemas as schemas


def get_usuario(db: Session, usuario_id: int) -> Optional[models.Usuario]:
    """
    Obtener un usuario por ID.
    
    Args:
        db: Sesión de base de datos
        usuario_id: ID del usuario a buscar
    
    Returns:
        Usuario encontrado o None
    """
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()


def get_usuario_by_correo(db: Session, correo: str) -> Optional[models.Usuario]:
    """
    Obtener un usuario por correo electrónico.
    
    Args:
        db: Sesión de base de datos
        correo: Correo del usuario a buscar
    
    Returns:
        Usuario encontrado o None
    """
    return db.query(models.Usuario).filter(models.Usuario.correo == correo).first()


def get_usuarios(db: Session, skip: int = 0, limit: int = 100) -> List[models.Usuario]:
    """
    Obtener lista de usuarios con paginación.
    
    Args:
        db: Sesión de base de datos
        skip: Número de registros a saltar
        limit: Máximo de registros a devolver
    
    Returns:
        Lista de usuarios
    """
    return db.query(models.Usuario).offset(skip).limit(limit).all()


def create_usuario(db: Session, usuario: schemas.UsuarioCreate) -> models.Usuario:
    """
    Crear un nuevo usuario en la base de datos.
    
    Args:
        db: Sesión de base de datos
        usuario: Datos del usuario a crear
    
    Returns:
        Usuario creado con su ID
    """
    db_usuario = models.Usuario(**usuario.model_dump())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def update_usuario(
    db: Session, 
    usuario_id: int, 
    usuario_update: schemas.UsuarioUpdate
) -> Optional[models.Usuario]:
    """
    Actualizar un usuario existente.
    
    Args:
        db: Sesión de base de datos
        usuario_id: ID del usuario a actualizar
        usuario_update: Datos a actualizar (solo campos enviados)
    
    Returns:
        Usuario actualizado o None si no existe
    """
    db_usuario = get_usuario(db, usuario_id)
    
    if db_usuario is None:
        return None
    
    # Actualizar solo los campos que se enviaron
    update_data = usuario_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_usuario, key, value)
    
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def delete_usuario(db: Session, usuario_id: int) -> bool:
    """
    Eliminar un usuario de la base de datos.
    
    Args:
        db: Sesión de base de datos
        usuario_id: ID del usuario a eliminar
    
    Returns:
        True si se eliminó, False si no existía
    """
    db_usuario = get_usuario(db, usuario_id)
    
    if db_usuario is None:
        return False
    
    db.delete(db_usuario)
    db.commit()
    return True