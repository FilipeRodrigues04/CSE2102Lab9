import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "my_server", Path(__file__).with_name("my-server.py")
)
my_server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_server)
app = my_server.app


def test_login_success():
    client = app.test_client()

    response = client.post(
        "/login",
        data={
            "id": "phillip.bradford@uconn.edu",
            "uuid-token": "925a4dfa-86b7-4c06-8f3e-fdccb0a748b2",
        },
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["message"] == "Token accepted"


def test_login_missing_fields():
    client = app.test_client()

    response = client.post("/login", data={"id": "phillip.bradford@uconn.edu"})

    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"


def test_login_invalid_token():
    client = app.test_client()

    response = client.post(
        "/login",
        data={
            "id": "phillip.bradford@uconn.edu",
            "uuid-token": "not-a-real-token",
        },
    )

    assert response.status_code == 403
    data = response.get_json()
    assert data["status"] == "fail"
