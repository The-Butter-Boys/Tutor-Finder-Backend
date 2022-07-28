from flask import jsonify, request, Response
from tutor_finder import app
from tutor_finder.models import User, Course
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash

db = SQLAlchemy(app)

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
        return Response("{response", status=399, mimetype='application/json')
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

    if Course.query.filter_by(name=name).first():
        return {'success': False}
    course = Course(department=department, number=number, name=name)
    db.session.add(course)
    db.session.commit()
    return 'response'

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    user = User.query.filter_by(username=username).first()
    password = request.json['password']

    if user and user.check_password(password):
        return {'success': True}
    else:
        return {'success': False}