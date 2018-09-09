import pytest, os
from controller.controller_handler import Controller
from base.base_app import create_app

@pytest.fixture
def client():
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
    return create_app(Controller, config_path).test_client()

def test_base_communication(client):
    response = client.get("/api",json={"command":"test","data":{"message":"bla"}})
    assert response.status_code == 200
