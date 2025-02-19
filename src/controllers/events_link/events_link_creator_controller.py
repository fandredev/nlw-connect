from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from http import HTTPStatus

from src.models.repositories.interfaces.events_link_repository import (
    EventsLinkRepositoryInterface,
)


class EventsLinkCreatorController:
    def __init__(self, events_link_repo: EventsLinkRepositoryInterface):
        self.__events_link_repo = events_link_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        event_link_info = http_request.body["data"]
        event_id = event_link_info["event_id"]
        subscriber_id = event_link_info["subscriber_id"]

        self.__check_event_link(event_id, subscriber_id)
        self.__insert_event_link(event_id, subscriber_id)

        new_link = self.__events_link_repo.select_events_link(event_id, subscriber_id)

        return self.__format_response(new_link, event_id, subscriber_id)

    def __check_event_link(self, event_id: int, subscriber_id: int) -> None:
        response = self.__events_link_repo.select_events_link(event_id, subscriber_id)
        if response:
            raise Exception("Link already exists")

    def __insert_event_link(self, event_id: int, subscriber_id: int) -> None:
        new_link = self.__events_link_repo.insert(event_id, subscriber_id)

        return new_link

    def __format_response(
        self, new_link: str, event_id: int, subscriber_id: int
    ) -> HttpResponse:
        return HttpResponse(
            HTTPStatus.CREATED,
            {
                "data": {
                    "Type": "Event Link",
                    "count": 1,
                    "attributes": {
                        "event_id": event_id,
                        "subscriber_id": subscriber_id,
                        "link": new_link,
                    },
                },
                "status_code": HTTPStatus.CREATED,
                "message": "Event Link created",
            },
        )
