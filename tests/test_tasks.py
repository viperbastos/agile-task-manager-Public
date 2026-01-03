import sys
import os

# Adiciona a pasta raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import app


def test_create_task():
    client = app.test_client()

    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Testing task creation",
        "priority": "Alta"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test Task"
    assert data["priority"] == "Alta"
