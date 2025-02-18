from src.models.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Subscriptions(Base):
    __tablename__ = "Inscrições"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
