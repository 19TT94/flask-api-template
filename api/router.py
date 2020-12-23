from api.routes.example import Example

def initialize_routes(api):
    api.add_resource(Example, '/api/v1/example')