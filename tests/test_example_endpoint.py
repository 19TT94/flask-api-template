import pytest

def test_get_example_endpoint(client, app):
    # test that example api endpoint returns a 200
    assert client.get("/api/v1/example").status_code == 200

