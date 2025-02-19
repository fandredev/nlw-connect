class HttpRequest:
    def __init__(self, params: dict = None, body: dict = None) -> None:
        self.params = params
        self.body = body
