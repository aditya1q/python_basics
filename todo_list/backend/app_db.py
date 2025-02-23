from flask import Flask, jsonify, request # imports the Flask class.
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__) # Creates a Flask application instance. __name__ tells Flask where to look for templates and static files relative to this file.
CORS(app)  # Enable CORS for all routes

# Connect to MongoDB (local)
client = MongoClient('mongodb://localhost:27017/') # local mongodb
# create db
db = client['todo_db']  # Access the 'todo_db' database
# create collection
todo_collection = db['todos']

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = list(todo_collection.find())
    # Convert ObjectId to string for JSON serialization
    for todo in todos:
        todo['id'] = str(todo['_id'])
        todo.pop('_id')
    return jsonify(todos)

@app.route('/api/todos', methods=["POST"])
def add_todos():
    data = request.json or {}
    task = data.get('task')  # Get task from JSON body
    if not task:
        return jsonify({"error":"Task is required"}), 400
    
    todo = {"task":task, "done":False}
    result = todo_collection.insert_one(todo)
    todo['id'] = str(result.inserted_id) # Use _id as 'id'
    todo.pop('_id')
    return jsonify(todo), 201

@app.route('/api/todos/<string:todo_id>', methods=['PUT'])
def update_todos(todo_id):
    try:
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})

        if not todo:
            return jsonify({"error": "Todo not found"}), 404
        data = request.json or {}
        new_done =data.get('done', todo['done'])
        todo_collection.update_one(
            {"_id": ObjectId(todo_id)},
            {"$set": {"done": new_done}},
        )
        todo['done'] = new_done
        todo['id'] = str(todo['_id'])
        todo.pop('_id')
        return jsonify(todo)
    except ValueError:
        return jsonify({"error": "Invalid todo ID"}), 400

@app.route('/api/todos/<string:todo_id>', methods=["DELETE"])
def delete_todos(todo_id):
    try:
        result = todo_collection.delete_one({"_id": ObjectId(todo_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Todo not found"}), 404
        return '', 204
    except ValueError:
        return jsonify({"error": "Invailid Todo ID"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Starts the Flask development server with debug mode on (auto-reloads on code changes).