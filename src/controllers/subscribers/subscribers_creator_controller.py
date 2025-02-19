from src.models.repositories.interfaces.subscribers_repository import (
    SubscribersRepositoryInterface,
)
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from http import HTTPStatus


class SubscribersCreatorController:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        subscriber_email = subscriber_info["email"]
        event_id = subscriber_info["event_id"]

        self.__check_subscriber(subscriber_email, event_id)
        self.__insert_sub(subscriber_info)
        return self.__format_response(subscriber_info)

    def __check_subscriber(self, subscriber_email: str, event_id: int) -> None:
        response = self.__subscribers_repo.select_subscriber(subscriber_email, event_id)
        if response:
            raise Exception("Subscriber already exists")

    def __insert_sub(self, subscriber_info: dict) -> None:
        self.__subscribers_repo.insert_subscriber(subscriber_info)

    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            HTTPStatus.CREATED,
            {
                "data": {
                    "Type": "Subscribers",
                    "count": 1,
                    "attributes": subscriber_info,
                },
                "status_code": HTTPStatus.CREATED,
                "message": "Subscriber created",
            },
        )
