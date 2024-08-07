from flask import Blueprint, request, jsonify, url_for, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.services.user_service import create_user, get_user_by_email, get_user_by_id, update_user_password
from app.models.user import User
from app.extensions import mail, jwt
from flask_mail import Message
import datetime
from itsdangerous import URLSafeTimedSerializer
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__)
serializer = URLSafeTimedSerializer('supersecretkey')

@auth_bp.route('/register', methods=['POST'])
@swag_from('docs/register.yml')
def register():
    data = request.get_json()
    if get_user_by_email(data['email']):
        return jsonify({"message": "User already exists"}), 400
    user = create_user(data['username'], data['email'], data['password'])
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
@swag_from('docs/login.yml')
def login():
    data = request.get_json()
    user = get_user_by_email(data['email'])
    if user and User.check_password(user['password'], data['password']):
        access_token = create_access_token(identity=str(user['_id']))
        refresh_token = create_refresh_token(identity=str(user['_id']))
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
@swag_from('docs/refresh.yml')
def refresh():
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
@swag_from('docs/me.yml')
def me():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    return jsonify(username=user['username'], email=user['email']), 200

@auth_bp.route('/reset_password', methods=['POST'])
@swag_from('docs/reset_password.yml')
def reset_password():
    data = request.get_json()
    user = get_user_by_email(data['email'])
    if not user:
        return jsonify({"message": "User not found"}), 404

    token = serializer.dumps(user['email'], salt='password-reset-salt')
    reset_url = url_for('auth.reset_password_token', token=token, _external=True)
    html = render_template('reset_password.html', reset_url=reset_url)
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user['email']], html=html)
    mail.send(msg)

    return jsonify({"message": "Password reset email sent"}), 200

@auth_bp.route('/reset_password/<token>', methods=['POST'])
@swag_from('docs/reset_password_token.yml')
def reset_password_token(token):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=1800)
    except Exception as e:
        return jsonify({"message": "The token is invalid or expired"}), 400

    data = request.get_json()
    update_user_password(email, data['new_password'])
    return jsonify({"message": "Password has been reset successfully"}), 200
