from src.models.repositories.interfaces.subscribers_repository import (
    SubscribersRepositoryInterface,
)
from src.models.configs.connection import DBConnectionHandler
from src.models.entities.subscriptions import Subscriptions
from typing import Dict, List, Tuple

from sqlalchemy import func, desc


class SubscribersRepository(SubscribersRepositoryInterface):
    def insert_subscriber(self, susbcriber_infos: Dict) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_subscriber = Subscriptions(
                    name=susbcriber_infos.get("name"),
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

    def select_subscribers_by_link(
        self, link: str, event_id: int
    ) -> List[Subscriptions]:
        with DBConnectionHandler() as db_connection:
            subscribers = (
                db_connection.session.query(Subscriptions)
                .filter(Subscriptions.link == link, Subscriptions.event_id == event_id)
                .all()
            )
            return subscribers

    def get_ranking(self, event_id: int) -> Tuple[Subscriptions]:
        with DBConnectionHandler() as db_connection:
            subscribers = (
                db_connection.session.query(
                    Subscriptions.link, func.count(Subscriptions.link).label("count")
                )
                .filter(
                    Subscriptions.event_id == event_id, Subscriptions.link.isnot(None)
                )
                .group_by(Subscriptions.link)
                .order_by(
                    desc("count"),
                )
                .all()
            )
            return subscribers
