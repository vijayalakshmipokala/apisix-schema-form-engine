import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_dependencies_field():
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
                ],
                "dependencies": {
                    "token": ["auth_method"]
                }
            },
            "timeout": {"type": "integer"}
        }
    }

    response = client.post("/form/generate", json=schema)
    assert response.status_code == 200
    data = response.json()

    # 'auth_method' must have dependencies
    auth_field = data["fields"][0]
    assert "dependencies" in auth_field
    assert auth_field["dependencies"]["token"] == ["auth_method"]

    # 'timeout' must be a primitive field
    timeout_field = data["fields"][1]
    assert timeout_field["widget"] == "number"