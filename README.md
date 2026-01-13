# Agile Task Manager

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema básico de gerenciamento de tarefas, criado como atividade prática da disciplina de Engenharia de Software – Unidade IV do Centro Universitário UNIFECAF.

O objetivo do projeto é aplicar, de forma prática, os conceitos de metodologias ágeis, versionamento de código, controle de qualidade e integração contínua utilizando a plataforma GitHub.

---

## 🎯 Objetivos

- Aplicar conceitos de Engenharia de Software e metodologias ágeis
- Utilizar GitHub para versionamento e gestão do projeto
- Implementar um sistema básico de gerenciamento de tarefas (CRUD)
- Criar e organizar tarefas usando GitHub Projects (Kanban)
- Implementar testes automatizados com Pytest
- Configurar integração contínua com GitHub Actions
- Simular gestão de mudanças no projeto

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13
- Flask
- Pytest
- GitHub Actions
- GitHub Projects (Kanban)

---

## 📂 Estrutura do Projeto

agile-task-manager/
│
├── .github/
│   └── workflow/
│       └── ci.yml          # Pipeline do GitHub Actions (testes automáticos)
│
├── src/
│   ├── app.py              # Aplicação Flask (API do sistema)
│   └── models.py           # Modelo de dados e regras de negócio
│
├── tests/
│   └── test_tasks.py       # Testes automatizados com PyTest
│
├── venv/                   # Ambiente virtual Python (não vai para o GitHub)
│
├── README.md               # Documentação principal do projeto
└── requirements.txt        # Lista de dependências (Flask, PyTest, etc)


