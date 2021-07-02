from flask import jsonify, current_app
from api.routes.ping import HealthCheckEndpoint
from api.routes.example import ExampleEndpoint

def initialize_routes(api) -> None:
    """Initialize routes defined for each resource"""

    # Health Check
    health_check = HealthCheckEndpoint.as_view("ping")
    api.add_url_rule("/api/v1/ping", view_func=health_check)

    # Example Routes
    api.add_url_rule("/api/v1/example", view_func=ExampleEndpoint.as_view("example"))

    @api.errorhandler(500)
    @api.errorhandler(422)
    def handle_error(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        message = messages["json"] if "json" in messages.keys() else messages
        if headers:
            current_app.logger.error(message)
            return jsonify(message), err.code, headers, 400
        else:
            current_app.logger.error(message)
            return jsonify(message), err.code, 400
