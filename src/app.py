# Importa o Flask e funções auxiliares
from flask import Flask, jsonify, request

# Importa a classe Task do arquivo models.py
from models import Task

# Cria a aplicação Flask
app = Flask(__name__)

# Lista que armazena as tarefas em memória
tasks = []

# Contador para gerar IDs únicos
task_id_counter = 1


# ============================
# ROTA: LISTAR TAREFAS (READ)
# ============================
@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Retorna todas as tarefas convertidas para JSON
    return jsonify([task.to_dict() for task in tasks])


# ============================
# ROTA: CRIAR TAREFA (CREATE)
# ============================
@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter

    # Obtém os dados enviados em formato JSON
    data = request.json

    # Cria uma nova tarefa
    task = Task(
        id=task_id_counter,
        title=data.get("title"),
        description=data.get("description"),
        priority=data.get("priority", "Média")
    )

    # Adiciona a tarefa à lista
    tasks.append(task)

    # Incrementa o ID
    task_id_counter += 1

    # Retorna a tarefa criada com status 201
    return jsonify(task.to_dict()), 201


# ============================
# ROTA: ATUALIZAR TAREFA (UPDATE)
# ============================
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task.id == task_id:
            data = request.json

            # Atualiza apenas os campos enviados
            task.title = data.get("title", task.title)
            task.description = data.get("description", task.description)
            task.status = data.get("status", task.status)
            task.priority = data.get("priority", task.priority)

            return jsonify(task.to_dict())

    # Caso a tarefa não exista
    return jsonify({"error": "Task not found"}), 404


# ============================
# ROTA: EXCLUIR TAREFA (DELETE)
# ============================
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    # Remove a tarefa com o ID informado
    tasks = [task for task in tasks if task.id != task_id]

    return jsonify({"message": "Task deleted"})


# ============================
# INICIALIZAÇÃO DO SERVIDOR
# ============================
if __name__ == "__main__":
    # Inicia o servidor Flask em modo de desenvolvimento
    app.run(debug=True)
