from src.models.repositories.interfaces.subscribers_repository import (
    SubscribersRepositoryInterface,
)
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from http import HTTPStatus


class SubscribersManagerController:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.params["link"]
        event_id = http_request.params["event_id"]

        subs = self.__subscribers_repo.select_subscribers_by_link(link, event_id)

        return self.__format_subs_by_link(subs)

    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.params["event_id"]

        event_ranking = self.__subscribers_repo.get_ranking(event_id)

        return self.__format_event_ranking(event_ranking)

    def __format_subs_by_link(self, subscribers: list) -> HttpResponse:
        formatted_subscriber = []
        for subs in subscribers:
            formatted_subscriber.append(
                {
                    "name": subs.name,
                    "email": subs.email,
                }
            )

        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(subscribers),
                    "attributes": formatted_subscriber,
                },
                "status_code": HTTPStatus.OK,
                "message": "Subscribers found",
            },
            status_code=HTTPStatus.OK,
        )

    def __format_event_ranking(self, event_ranking: list) -> HttpResponse:
        formatted_event_ranking = []
        for position in event_ranking:
            formatted_event_ranking.append(
                {
                    "link": position.link,
                    "count_subscribers": position.count,
                }
            )

        return HttpResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "ranking": formatted_event_ranking,
                },
                "status_code": HTTPStatus.OK,
                "message": "Ranking found",
            },
            status_code=HTTPStatus.OK,
        )
