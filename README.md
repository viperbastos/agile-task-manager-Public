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
