from src.models.repositories.interfaces.subscribers_repository import (
    SubscribersRepositoryInterface,
)
from src.models.configs.connection import DBConnectionHandler
from src.models.entities.subscriptions import Subscriptions
from typing import Dict


class SubscribersRepository(SubscribersRepositoryInterface):
    def insert_subscriber(self, susbcriber_infos: Dict) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_subscriber = Subscriptions(
                    nome=susbcriber_infos.get("name"),
                    email=susbcriber_infos.get("email"),
                    link=susbcriber_infos.get("link"),
                    event_id=susbcriber_infos.get("event_id"),
                )
                db_connection.session.add(new_subscriber)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e

    def select_subscriber(self, email: str, event_id: int) -> Subscriptions:
        with DBConnectionHandler() as db_connection:
            subscriber = (
                db_connection.session.query(Subscriptions)
                .filter(
                    Subscriptions.email == email, Subscriptions.event_id == event_id
                )
                .first()
            )
            return subscriber
