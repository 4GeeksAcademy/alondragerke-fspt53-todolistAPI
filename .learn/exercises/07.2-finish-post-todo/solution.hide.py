from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    
    todos.append(request_body)
    resp = jsonify(todos)
    resp.status_code = 201
    return resp

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
