from flask import Blueprint, jsonify, request
from http import HTTPStatus

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.controllers.subscribers.subscribers_creator_controller import (
    SubscribersCreatorController,
)

from src.models.repositories.subscribers_repository import SubscribersRepository

subscribers_route_bp = Blueprint("subscribers_route", __name__)


@subscribers_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subscribers_repo = SubscribersRepository()
    subscribers_creator_controller = SubscribersCreatorController(subscribers_repo)
    http_response = subscribers_creator_controller.create(http_request)

    return jsonify(http_response.body), http_response.status_code
