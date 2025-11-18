from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    autor = Column(Integer, nullable=False)
    contenido = Column(String(255), nullable=False)
    likes = Column(Integer, default=0)
    fecha = Column(DateTime, nullable=False, server_default=func.now())
    habilitado = Column(Boolean, default=1)