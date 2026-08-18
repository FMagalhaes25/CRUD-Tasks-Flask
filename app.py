from flask import Flask, request, jsonify
from models.task import Task


# __name__ = "__main__"
app = Flask(__name__)

# CRUD
tasks = []
task_id_control = 1

#POST
@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id= task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

# GET all
@app.route("/tasks", methods=['GET'])
def ver_tarefas():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
        
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)
        

#GET by ID
@app.route("/tasks/<int:id>", methods=['GET'])
def buscar_tarefa_por_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possível encontrar atividade"}), 404

# Somente para ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)