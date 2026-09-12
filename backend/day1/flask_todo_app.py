"""
Flask CRUD API for a Todo resource.
Implements endpoints: GET /todos, POST /todos, GET /todos/<id>, PUT /todos/<id>, DELETE /todos/<id>.
Uses an in-memory list as data store.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
todos = []
next_id = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todos."""
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo."""
    global next_id
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    todo = {
        'id': next_id,
        'title': data['title'],
        'completed': data.get('completed', False)
    }
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo by ID."""
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a specific todo by ID."""
    data = request.get_json()
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    if 'title' in data:
        todo['title'] = data['title']
    if 'completed' in data:
        todo['completed'] = data['completed']
    
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a specific todo by ID."""
    global todos
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'message': 'Todo deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)