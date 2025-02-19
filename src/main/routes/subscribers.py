from flask import Blueprint, jsonify, request
from http import HTTPStatus, HTTPMethod

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.controllers.subscribers.subscribers_creator_controller import (
    SubscribersCreatorController,
)
from src.controllers.subscribers.subscribers_manager_controller import (
    SubscribersManagerController,
)

from src.models.repositories.subscribers_repository import SubscribersRepository

subscribers_route_bp = Blueprint("subscribers_route", __name__)


@subscribers_route_bp.route("/subscriber", methods=[HTTPMethod.POST])
def create_new_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subscribers_repo = SubscribersRepository()
    subscribers_creator_controller = SubscribersCreatorController(subscribers_repo)
    http_response = subscribers_creator_controller.create(http_request)

    return jsonify(http_response.body), http_response.status_code


@subscribers_route_bp.route(
    "/subscriber/link/<link>/event/<event_id>", methods=[HTTPMethod.GET]
)
def subscribers_by_link(link: str, event_id: int):
    http_request = HttpRequest(params={"link": link, "event_id": event_id})

    subscribers_repo = SubscribersRepository()
    subscribers_manager_controller = SubscribersManagerController(subscribers_repo)
    http_response = subscribers_manager_controller.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code


@subscribers_route_bp.route(
    "/subscriber/ranking/event/<event_id>", methods=[HTTPMethod.GET]
)
def link_ranking(event_id: int):
    http_request = HttpRequest(params={"event_id": event_id})

    subscribers_repo = SubscribersRepository()
    subscribers_manager_controller = SubscribersManagerController(subscribers_repo)
    http_response = subscribers_manager_controller.get_event_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code
