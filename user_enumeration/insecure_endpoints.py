from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    'alice': {'password': 'password123', 'locked': False, 'email': 'alice@example.com'},
    'bob': {'password': 'qwerty', 'locked': True, 'email': 'bob@example.com'},
}


@app.route('/insecure/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username not in USERS:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    if USERS[username]['password'] != password:
        return jsonify({'error': 'Contraseña incorrecta'}), 401
    return jsonify({'message': 'Login exitoso'})


@app.route('/insecure/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    username = data.get('username')
    if username not in USERS:
        return jsonify({'error': 'Usuario no existe'}), 404
    return jsonify({'message': 'Se ha enviado un correo para restablecer la contraseña'}), 200


import time
@app.route('/insecure/response-time', methods=['POST'])
def response_time():
    data = request.json
    username = data.get('username')
    if username in USERS:
        time.sleep(0.1)
    else:
        time.sleep(1.0)
    return jsonify({'message': 'Procesado'}), 200

if __name__ == '__main__':
    app.run(debug=True)
