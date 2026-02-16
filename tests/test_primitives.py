from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_primitives_only():
    schema = {
        "type": "object",
        "properties": {
            "timeout": {"type": "integer"},
            "enable": {"type": "boolean"},
            "username": {"type": "string"}
        },
        "required": ["timeout"]
    }

    response = client.post("/form/generate", json=schema)
    assert response.status_code == 200

    data = response.json()

    assert data["type"] == "object"
    assert len(data["fields"]) == 3

    fields = {f["name"]: f for f in data["fields"]}

    assert fields["timeout"]["widget"] == "number"
    assert fields["timeout"]["required"] is True

    assert fields["enable"]["widget"] == "checkbox"
    assert fields["enable"]["required"] is False

    assert fields["username"]["widget"] == "text"
    assert fields["username"]["required"] is False