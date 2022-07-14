from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tyugkyiqkxxnyi:09b421cce0bf05be569f8e957642cdad63fae40c0fdf6d92deccfe9468be8b2b@ec2-18-204-142-254.compute-1.amazonaws.com:5432/db354593uc8gce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
	app.run()
class User(db.Model):
    # Table is called 'app_user' because 'user' would conflict with postgres keyword
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"<User {self.id}: {self.username}>"

    def to_dict(self):
        dict = {'id': self.id, 'username': self.username, 'email': self.email}
        return dict

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(64))
    number = db.Column(db.String(64))
    name = db.Column(db.String(64))

    def to_dict(self):
        dict = {'id': self.id, 'department': self.department, 'number': self.number, 'name': self.name}
        return dict


@app.route('/users')
def users():
    users = User.query.all()
    data = [user.to_dict() for user in users]
    return jsonify(data)

@app.route('/courses')
def courses():
    courses = Course.query.all()
    data = [course.to_dict() for course in courses]
    return jsonify(data)

@app.route('/users', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if User.query.filter_by(username=username).first():
        return Response("{response", status=400, mimetype='application/json')
    pw_hash = generate_password_hash(password)
    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()
    return 'response'

@app.route('/courses', methods=['POST'])
def add_course():
    department = request.json['department']
    number = request.json['number']
    name = request.json['name']

    course = Course(department=department, number=number, name=name)
    db.session.add(course)
    db.session.commit()
    return 'response'




@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    user = User.query.filter_by(username=username).first()
    if user is None:
        return {'success': False}
    password = request.json['password']
    # TODO: validate username and password
    success = user.check_password(password)
    return {'success': success}
