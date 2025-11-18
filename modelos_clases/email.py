from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    habilitado = Column(Boolean, default=1)