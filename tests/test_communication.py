import pytest
from PiHomie import create_app

@pytest.fixture
def client():
    return create_app().test_client()

def test_base_communication(client):
    response = client.get("/api",json={"command":"test","data":{"message":"bla"}})
    assert response.status_code == 200
