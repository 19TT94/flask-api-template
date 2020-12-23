from flask_restful import Resource

class Example(Resource):
    def get(self):
        return {"example": {"name": "Example Response"}}