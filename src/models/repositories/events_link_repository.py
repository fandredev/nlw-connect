import random


from src.models.configs.connection import DBConnectionHandler
from src.models.entities.events_link import EventsLink


class EventsLinkRepository:
    def insert(self, event_id: int, subscription_id: int) -> str:
        with DBConnectionHandler() as db_connection:
            try:
                link_final = "".join(random.choices("0123456789", k=7))
                formatted_link = f"event-{event_id}-{subscription_id}-{link_final}"
                new_events_link = EventsLink(
                    event_id=event_id,
                    subscription_id=subscription_id,
                    link=formatted_link,
                )
                db_connection.session.add(new_events_link)
                db_connection.session.commit()

                return formatted_link
            except Exception as e:
                db_connection.session.rollback()
                raise e

    def select_events_link(self, event_id: int, subscription_id: int) -> EventsLink:
        with DBConnectionHandler() as db_connection:
            event = (
                db_connection.session.query(EventsLink)
                .filter(
                    EventsLink.event_id == event_id,
                    EventsLink.subscription_id == subscription_id,
                )
                .first()
            )
            return event
