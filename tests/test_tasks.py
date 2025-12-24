# Importa a aplicação Flask
from src.app import app


# Teste para verificar se a criação de tarefas funciona corretamente
def test_create_task():
    # Cria um cliente de teste do Flask
    client = app.test_client()

    # Simula uma requisição POST para criar uma tarefa
    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Testing task creation",
        "priority": "Alta"
    })

    # Verifica se o status retornado é 201 (Criado)
    assert response.status_code == 201

    # Obtém o JSON retornado pela API
    data = response.get_json()

    # Valida os dados retornados
    assert data["title"] == "Test Task"
    assert data["priority"] == "Alta"
