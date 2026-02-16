import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_oneof_field():
    schema = {
        "type": "object",
        "properties": {
            "auth_method": {
                "oneOf": [
                    {
                        "title": "Basic Auth",
                        "properties": {
                            "username": {"type": "string"},
                            "password": {"type": "string"}
                        }
                    },
                    {
                        "title": "Token Auth",
                        "properties": {
                            "token": {"type": "string"}
                        }
                    }
                ]
            }
        }
    }

    response = client.post("/form/generate", json=schema)
    assert response.status_code == 200
    data = response.json()

    # The 'auth_method' should have a widget of "oneOf" and two options
    assert data["fields"][0]["name"] == "auth_method"
    assert data["fields"][0]["widget"] == "oneOf"
    assert len(data["fields"][0]["options"]) == 2
    # Each option should have fields
    for option in data["fields"][0]["options"]:
        assert "fields" in option