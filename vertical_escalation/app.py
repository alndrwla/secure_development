
"""
API vulnerable to vertical privilege escalation.
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated users and roles
users = {
    'alice': {'role': 'user'},
    'bob': {'role': 'admin'}
}

# Nuevo endpoint para ver los roles de los usuarios
@app.route('/users-roles', methods=['GET'])
def users_roles():
    return jsonify({user: info['role'] for user, info in users.items()})


@app.route('/resource-insecure', methods=['POST'])
def resource_insecure():
    data = request.get_json()
    user = data.get('user')
    new_role = data.get('new_role')
    target = data.get('target')
    # Vulnerability: allows changing the role of any user
    if target and new_role and target in users:
        users[target]['role'] = new_role
    if user and user in users:
        if users[user]['role'] == 'admin':
            return jsonify({'message': 'Access to admin resources granted.'})
        else:
            return jsonify({'message': 'Access denied.'}), 403
    return jsonify({'message': 'Invalid data.'}), 400

# Vulnerable endpoint
@app.route('/resource', methods=['POST'])
def resource():
    data = request.get_json()
    user = data.get('user')
    # Vulnerability: role can be modified from the client
    if 'role' in data:
        users[user]['role'] = data['role']
    if users[user]['role'] == 'admin':
        return jsonify({'message': 'Access to admin resources granted.'})
    else:
        return jsonify({'message': 'Access denied.'}), 403

# Secure endpoint
@app.route('/resource-secure', methods=['POST'])
def resource_secure():
    data = request.get_json()
    user = data.get('user')
    # Role cannot be modified from the request
    if not user or user not in users:
        return jsonify({'message': 'Invalid user.'}), 400
    if users[user]['role'] == 'admin':
        return jsonify({'message': 'Access to admin resources granted.'})
    else:
        return jsonify({'message': 'Access denied.'}), 403

if __name__ == '__main__':
    app.run(debug=True)
