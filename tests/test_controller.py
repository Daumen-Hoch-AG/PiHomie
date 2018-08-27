import pytest
from base.base_app import create_app
from controller.controller_handler import Controller

@pytest.fixture
def client():
    test_config = "testcfg.ini"
    return create_app(Controller, test_config).test_client()

def test_base_communication(client):
    response = client.get("/api",json={"command":"test","data":{"message":"bla"}})
    assert response.status_code == 200
