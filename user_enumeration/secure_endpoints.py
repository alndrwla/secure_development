from flask import Flask, request, jsonify
import time

app = Flask(__name__)

USERS = {
    'alice': {'password': 'password123', 'locked': False, 'email': 'alice@example.com'},
    'bob': {'password': 'qwerty', 'locked': True, 'email': 'bob@example.com'},
}

generic_msg = {'message': 'Si la información es válida, se ha procesado la solicitud.'}

@app.route('/secure/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in USERS and USERS[username]['password'] == password:
        return jsonify({'message': 'Login exitoso'})
    return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401


@app.route('/secure/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    username = data.get('username')
    return jsonify(generic_msg), 200


@app.route('/secure/response-time', methods=['POST'])
def response_time():
    data = request.json
    username = data.get('username')
    user = USERS.get(username)
    dummy = 'dummy_value'
    _ = (user['password'] if user else dummy) == 'no_existe'
    return jsonify(generic_msg), 200

if __name__ == '__main__':
    app.run(debug=True)
