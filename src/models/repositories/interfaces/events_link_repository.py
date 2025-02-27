from abc import ABC, abstractmethod
from src.models.entities.events_link import EventsLink


class EventsLinkRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_id: int, subscription_id: int) -> None:
        pass

    @abstractmethod
    def select_events_link(self, event_id: id, subscription_id: int) -> EventsLink:
        pass
