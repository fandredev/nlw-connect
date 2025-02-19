from src.models.configs.base import Base
from sqlalchemy import Column, Integer, String


class Events(Base):
    __tablename__ = "Events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
