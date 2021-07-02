from flask.views import MethodView
from webargs.fields import String
from webargs.flaskparser import use_args

class ExampleEndpoint(MethodView):
    example_params = {
        "example_param": String(data_key="exampleParam")
    }

    @use_args(example_params, location="json")
    def get(self, args: dict) -> dict:
        return {"example": {"name": "Example Response"}}, 200
