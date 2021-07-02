from flask import jsonify
from flask.views import MethodView

class HealthCheckEndpoint(MethodView):
    def get(self) -> dict:
        # TODO: add after db connection established or remove
        # try:
        #     db.session.execute("select 1")
        # except Exception as e:
        #     return jsonify({ "error": str(e) }), 400

        return jsonify({ "message": "Health check passed" }), 200
