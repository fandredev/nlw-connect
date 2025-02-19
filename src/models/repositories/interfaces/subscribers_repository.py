from abc import ABC, abstractmethod
from src.models.configs.connection import DBConnectionHandler
from src.models.entities.subscriptions import Subscriptions
from typing import Dict


class SubscribersRepositoryInterface(ABC):

    @abstractmethod
    def insert_subscriber(self, susbcriber_infos: Dict) -> None:
        pass

    @abstractmethod
    def select_subscriber(self, email: str, event_id: int) -> Subscriptions:
        pass
