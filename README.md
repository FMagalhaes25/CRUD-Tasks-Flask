# 🍶 Flask CRUD Tasks

Uma API RESTful simples e eficiente para gerenciar tarefas, desenvolvida com Flask.

---

## 📋 Sobre o Projeto

Este projeto é uma aplicação de exemplo que demonstra um **CRUD completo** (Create, Read, Update, Delete) de tarefas usando Flask. Perfeito para aprender os conceitos fundamentais de desenvolvimento de APIs REST em Python.

---

## ✨ Funcionalidades

- ✅ **Criar** novas tarefas
- ✅ **Listar** todas as tarefas
- ✅ **Buscar** tarefa por ID
- ✅ **Atualizar** informações da tarefa
- ✅ **Deletar** tarefas
- ✅ Controle de conclusão de tarefas
- ✅ Descrições detalhadas para cada tarefa

---

## 🛠️ Tecnologias Utilizadas

- **Python** 3.x
- **Flask** 2.3.0 - Framework web minimalista
- **Flask-SQLAlchemy** 3.1.1 - ORM para banco de dados
- **Flask-Cors** 3.0.10 - Suporte a CORS
- **Werkzeug** 2.3.0 - Utilitários WSGI

---

## 📦 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passo a passo

1. **Clone o repositório:**
```bash
git clone https://github.com/FMagalhaes25/CRUD-Tasks-Flask.git
cd CRUD-Tasks-Flask
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

---

## 🚀 Como Usar

### Iniciar a aplicação

```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

---

## 📡 Endpoints da API

### 1. **Criar Tarefa**
- **Método:** `POST`
- **Rota:** `/tasks`
- **Body (JSON):**
```json
{
  "title": "Minha tarefa",
  "description": "Descrição da tarefa"
}
```
- **Resposta:**
```json
{
  "message": "Nova tarefa criada com sucesso!"
}
```

---

### 2. **Listar Todas as Tarefas**
- **Método:** `GET`
- **Rota:** `/tasks`
- **Resposta:**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Minha tarefa",
      "description": "Descrição da tarefa",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

---

### 3. **Buscar Tarefa por ID**
- **Método:** `GET`
- **Rota:** `/tasks/<id>`
- **Exemplo:** `/tasks/1`
- **Resposta:**
```json
{
  "id": 1,
  "title": "Minha tarefa",
  "description": "Descrição da tarefa",
  "completed": false
}
```

---

### 4. **Atualizar Tarefa**
- **Método:** `PUT`
- **Rota:** `/tasks/<id>`
- **Exemplo:** `/tasks/1`
- **Body (JSON):**
```json
{
  "title": "Tarefa atualizada",
  "description": "Nova descrição",
  "completed": true
}
```
- **Resposta:**
```json
{
  "message": "Tarefa atualizada com sucesso"
}
```

---

### 5. **Deletar Tarefa**
- **Método:** `DELETE`
- **Rota:** `/tasks/<id>`
- **Exemplo:** `/tasks/1`
- **Resposta:**
```json
{
  "message": "Tarefa deletada com sucesso"
}
```

---

## 📁 Estrutura do Projeto

```
Flask_Basico/
├── app.py                 # Arquivo principal da aplicação
├── requirements.txt       # Dependências do projeto
├── README.md             # Este arquivo
└── models/
    └── task.py           # Modelo da tarefa
```

---

## 🧪 Testando a API

Você pode testar a API usando:

- **cURL:**
```bash
curl -X GET http://localhost:5000/tasks
```

- **Postman:** Importe os endpoints para o Postman
- **Python requests:**
```python
import requests

response = requests.get('http://localhost:5000/tasks')
print(response.json())
```

---

## 👨‍💻 Autor

Desenvolvido como parte da **Formação Python - RocketSeat**

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.

---

**Última atualização:** 2026

