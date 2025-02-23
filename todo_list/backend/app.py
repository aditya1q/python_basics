from flask import Flask, jsonify, request # imports the Flask class.
from flask_cors import CORS

app = Flask(__name__) # Creates a Flask application instance. __name__ tells Flask where to look for templates and static files relative to this file.
CORS(app)  # Enable CORS for all routes

todos = []
next_id = 1

@app.route('/api/todos', methods=["GET"]) # Defines a route (URL) for the home page (/).
def get_todos():  # A function (called a view) that returns the text to display.
    return jsonify(todos)


@app.route('/api/todos', methods=["POST"])
def add_todos():
    global next_id
    task = request.json.get('task')  # Get task from JSON body
    if not task:
        return jsonify({"error":"Task is required"}), 400
    todo = {"id":next_id, "task":task, "done":False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todos(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo['done'] = request.json.get('done', todo['done']) # Toggle done status
    return jsonify(todo)


@app.route('/api/todos/<int:todo_id>', methods=["DELETE"])
def delete_todos(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Starts the Flask development server with debug mode on (auto-reloads on code changes).