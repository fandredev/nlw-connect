from src.models.configs.connection import DBConnectionHandler
from src.models.entities.events import Events

from src.models.repositories.interfaces.events_repository import (
    EventsRepositoryInterface,
)


class EventsRepository(EventsRepositoryInterface):
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_event = Events(name=event_name)
                db_connection.session.add(new_event)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e

    def select_event(self, event_name: str):
        with DBConnectionHandler() as db_connection:
            event = (
                db_connection.session.query(Events)
                .filter(Events.name == event_name)
                .first()
            )
            return event
