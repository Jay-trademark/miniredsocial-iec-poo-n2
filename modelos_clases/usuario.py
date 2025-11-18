from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(20), nullable=False)
    pwd = Column(String(64), nullable=False)
    seguidores = Column(Integer, default=0)
    siguiendo = Column(Integer, default=0)
    habilitado = Column(Boolean, default=1)

