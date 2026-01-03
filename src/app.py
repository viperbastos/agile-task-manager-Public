from flask import Flask, jsonify, request
from .models import Task  # IMPORT RELATIVO CORRETO

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return jsonify({"status": "API funcionando"})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        priority=data.get("priority", "Média")
    )
    tasks.append(task)
    return jsonify(task.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)
