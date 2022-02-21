from bookstore import db
from flask import request, jsonify
from bookstore.models import BookStoreUser
from bookstore.users import user_app


@user_app.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    email = data.get('email')
    age = data.get('age')
    mobile = data.get('mobile')
    if BookStoreUser.query.filter_by(username=username).first():
        return jsonify({"message": "Username is already Take", "data": {"username": username}})
    else:
        user = BookStoreUser(username, first_name, last_name, password, email, age, mobile)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "user is created "})


@user_app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    validate = BookStoreUser.query.filter_by(username=username, password=password).first()

    if validate:
        return jsonify({"message": " login successfully", "data": {"username": username}})
    else:
        return jsonify({"message": "User credentials invalid "})
