# Classe Task representa uma tarefa do sistema
class Task:
    def __init__(self, id, title, description, status="To Do", priority="Média"):
        # Identificador único da tarefa
        self.id = id

        # Título da tarefa
        self.title = title

        # Descrição detalhada da tarefa
        self.description = description

        # Status da tarefa no Kanban (To Do, In Progress, Done)
        self.status = status

        # Prioridade da tarefa (Baixa, Média, Alta)
        self.priority = priority

    # Converte o objeto Task em um dicionário
    # Isso facilita o retorno em formato JSON
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
