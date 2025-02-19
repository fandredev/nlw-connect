from flask import Blueprint, jsonify, request
from http import HTTPStatus
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

from src.validators.events_creator_validator import event_creator_validator

event_route_bp = Blueprint("event_route", __name__)


@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    event_creator_validator(request)
    http_request = HttpRequest(body=request.json)
    http_response = HttpResponse(
        body={"message": "Event created"}, status_code=HTTPStatus.CREATED
    )
    return jsonify(http_response.body), http_response.status_code
