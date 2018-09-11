import pytest, os, shutil
from controller.controller_handler import Controller
from base.base_app import create_app

@pytest.fixture(scope="module")
def client():
    os.makedirs("./log/pihomie", exist_ok=True)
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
    
    yield create_app(Controller, config_path).test_client()
    
    shutil.rmtree("./log")

def test_base_communication(client):
    response = client.get("/api",json={"command":"test","data":{"message":"bla"}})
    assert response.status_code == 200

def test_logging():
    is_teststring_present = False
    with open("./log/pihomie/info.log") as lf:
        for idx, line in enumerate(lf):
            if "Test handled\n" in line.split(' : '):
                is_teststring_present = True
            
    assert is_teststring_present
