from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tyugkyiqkxxnyi:09b421cce0bf05be569f8e957642cdad63fae40c0fdf6d92deccfe9468be8b2b@ec2-18-204-142-254.compute-1.amazonaws.com:5432/db354593uc8gce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    # Table is called 'app_user' because 'user' would conflict with postgres keyword
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"<User {self.id}: {self.username}>"

    def to_dict(self):
        dict = {'id': self.id, 'username': self.username}
        return dict


@app.route('/users')
def users():
    users = User.query.all()
    data = [user.to_dict() for user in users]
    return jsonify(data)

@app.route('/users', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    pw_hash = generate_password_hash(password)
    # user = User(username)
    # db.session.add(user)
    # db.session.commit()
    print(pw_hash)
    return jsonify({'username': username, 'password': password, 'password_hash': pw_hash, 'email': email})

# @app.route('/users/login')
# def login():
#     username = request.json['username']
#     password = request.json['password']
#     pw_hash = generate_password_hash(password)
#     success = check_password_hash(pwhash, password)
