from cerberus import Validator


def event_creator_validator(request: any) -> bool:
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "schema": {
                    "name": {"type": "string", "required": True, "empty": False},
                },
            }
        }
    )
    response = body_validator.validate(request.json)

    if response is False:
        print(body_validator.errors)
