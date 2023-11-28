import sys
sys.path.append(".")
from main import app

def test_create_user_api():
    response = app.test_client().post("/register-customer", json={
        "name": "nimra",
        "email": "n@gmail.com",
        "password": "123"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["id"] > 0

def test_login_user_api():
    response = app.test_client().post("/login", json={
        "email": "n@gmail.com",
        "password": "123"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["message"] == "user login successfully"
    assert "token" in data