"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import jwt_required, current_user
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/register', methods=['POST'])
def register():
    processed_params = request.get_json()
    print("PARAMS", processed_params)

    # Verificar si el correo electrónico ya existe en la base de datos
    existing_user = User.query.filter_by(email=processed_params['email']).first()
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400  # Retorna un error si ya existe

    # Crear el nuevo usuario
    new_user = User(email=processed_params['email'], is_active=True)
    new_user.set_password(processed_params['password'])

    # Guardar el usuario en la base de datos
    db.session.add(new_user)
    db.session.commit()

    return jsonify([{"msg": "User was created"}]), 201  # 201 código de creación exitosa

@api.route('/login', methods=['POST'])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).one_or_none()

    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401
    
    acces_token = create_access_token(identity=user)
    return jsonify({"access_token": acces_token, "user_id": user.id})





