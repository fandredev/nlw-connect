from src.models.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class EventsLink(Base):
    __tablename__ = "Events_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey("Events.id"))
    subscription_id = Column(Integer, ForeignKey("Subscriptions.id"))
    link = Column(String, nullable=False)
