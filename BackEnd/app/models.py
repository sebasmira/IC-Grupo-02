"""
Modelos de base de datos usando SQLAlchemy ORM.
Define la estructura de la tabla 'usuarios'.
"""

from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Usuario(Base):
    """
    Modelo de Usuario para la base de datos.
    Representa la tabla 'usuarios' con todos sus campos.
    """
    
    __tablename__ = "usuarios"

    # Campos de la tabla
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False, index=True)
    telefono = Column(String(20), nullable=False)
    edad = Column(Integer, nullable=False)
    ciudad = Column(String(100), nullable=False)
    rol = Column(String(50), nullable=False, default="Usuario")
    estado = Column(String(20), nullable=False, default="Activo")
    fechaRegistro = Column(Date, nullable=False)

    def __repr__(self):
        """Representación en string del usuario"""
        return f"<Usuario(id={self.id}, nombre={self.nombre}, correo={self.correo})>"