from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

# Supongamos que tienes tus datos en la variable some_data
todos = [
    { "label": "My frist task", "done": True}
]
@app.route('/todos', methods=['GET'])
def hello_world():
    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Esta es la posición a eliminar:", position)
    if 0 <= position < len(todos):  
        del todos[position] 
    return jsonify(todos)  
# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)