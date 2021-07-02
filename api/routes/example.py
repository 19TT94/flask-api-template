from flask.views import MethodView
from webargs.fields import String
from webargs.flaskparser import use_args

class Example(MethodView):
    example_params = {
        "example_param": String(data_key="exampleParam")
    }

    @use_args(address_params, location="json")
    def get(self):
        return {"example": {"name": "Example Response"}}
