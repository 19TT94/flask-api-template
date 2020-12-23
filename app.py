from flask import Flask
from flask_restful import Api

from src.router import initialize_routes

def create_app():
    app = Flask(__name__)
    api = Api(app)
    initialize_routes(api)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)