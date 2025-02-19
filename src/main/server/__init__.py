from src.main.routes.events import event_route_bp
from src.main.routes.subscribers import subscribers_route_bp
from flask import Flask


app = Flask(__name__)


app.register_blueprint(event_route_bp)
app.register_blueprint(subscribers_route_bp)
