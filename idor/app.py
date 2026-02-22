from dotenv import load_dotenv
from flask import Flask, jsonify, abort
from flask import request
from functools import wraps

import jwt
import os
import re
import uuid

load_dotenv()
SECRET_KEY = os.environ.get("JWT_SECRET")

app = Flask(__name__)

def require_jwt(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            abort(401, description="Token requerido")
        token = token.replace("Bearer ", "")
        if not decode_token(token):
            abort(401, description="Token inválido")
        return f(*args, **kwargs)
    return decorated_function

def slugify(name):
    return re.sub(r'[^a-zA-Z0-9]+', '-', name.lower()).strip('-')

users = {
    1: {"id": 1, "name": "Alice", "company": "Empresa A", "email": "alice@empresaA.com", "uuid": "10001", "slug": slugify("Alice")},
    2: {"id": 2, "name": "Bob", "company": "Empresa A", "email": "bob@empresaA.com", "uuid": "10002", "slug": slugify("Bob")},
    3: {"id": 3, "name": "Eve", "company": "Empresa B", "email": "eve@empresaB.com", "uuid": "10003", "slug": slugify("Eve")},
    4: {"id": 4, "name": "David", "company": "Empresa B", "email": "david@empresaB.com", "uuid": "10004", "slug": slugify("David")}
}


def decode_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data
    except Exception:
        return None


@app.route("/user/slug/<slug>", methods=["GET"])
@require_jwt
def get_user_by_slug_endpoint(slug):
    for user in users.values():
        if user["slug"] == slug:
            return jsonify(user)
    abort(404, description="User not found")

@app.route("/user/<int:user_id>", methods=["GET"])
@require_jwt
def get_user_by_id(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        abort(404, description="User not found")


@app.route("/user/email/<email>", methods=["GET"])
@require_jwt
def get_user_by_email(email):
    for user in users.values():
        if user["email"] == email:
            return jsonify(user)
    abort(404, description="User not found")


@app.route("/user/uuid/<uuid_str>", methods=["GET"])
@require_jwt
def get_user_by_uuid(uuid_str):
    for user in users.values():
        if user["uuid"] == uuid_str:
            return jsonify(user)
    abort(404, description="User not found")
    

@app.route("/secure/user/<int:user_id>", methods=["GET"])
@require_jwt
def secure_get_user_by_id(user_id):
    token = request.headers.get("Authorization").replace("Bearer ", "")
    data = decode_token(token)
    user = users.get(user_id)
    if user and data and data.get("company") == user["company"]:
        return jsonify(user)
    else:
        abort(403, description="No autorizado para acceder a este recurso")

if __name__ == "__main__":
    if not SECRET_KEY:
        print("ERROR: Debes definir la variable de entorno JWT_SECRET antes de iniciar el servidor.")
        exit(1)

    token = jwt.encode({"company": "Empresa A"}, SECRET_KEY, algorithm="HS256")
    print(f"JWT para Empresa A: {token}")
    app.run(debug=True)
