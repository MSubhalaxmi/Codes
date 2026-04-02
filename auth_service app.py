from flask import Flask, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_pw = generate_password_hash(data['password'])
    users[data['username']] = hashed_pw
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users.get(data['username'])

    if user and check_password_hash(user, data['password']):
        token = jwt.encode({
            'user': data['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(port=5001)