from flask import jsonify, request, Response
from tutor_finder import app, db
from tutor_finder.models import User, Course
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
 
# db = SQLAlchemy(app)



@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	email = request.json.get('email', None)
	password = request.json.get('password', None)
	# Validate request has both username and password
	if not username or not email or not password:
		return {'response': 'Missing data'}, 400
	
	# Check if user exists with username
	if User.query.filter_by(username=username).first():
		return {'response': 'Username taken'}, 400
	
	# Check if user exists with email
	if User.query.filter_by(email=email).first():
		return {'response': 'Email already in use'}, 400
	
	# TODO: Password validation

	# Create the user
	user = User(username, email, password)
	db.session.add(user)
	db.session.commit()

	# Create a token so user can be automatically logged in after registering
	token = create_access_token(identity=user.id)

	return {'token': token, 'user': user.to_dict()}, 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if not username or not password:
		return {'response': 'Missing data'}, 400
	
	user = User.query.filter_by(username=username).first()

	# Check if username doesn't match existing user
	if not user:
		return {'response': 'Username not found'}, 400
	
	# Check if password is correct
	if not user.check_password(password):
		return {'response': 'Password is incorrect'}, 400
	
	# At this point, user has valid login credentials, so create a token
	token = create_access_token(identity=user.id)
	return {'token': token, 'user': user.to_dict()}, 200

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
	current_user_id = get_jwt_identity()

# Test data for logged in users; returns data specific to the user
@app.route('/test', methods=['GET'])
@jwt_required()
def test():
	current_user_id = get_jwt_identity()
	user = User.query.filter_by(id=current_user_id).first()
	return jsonify(username=user.username, email=user.email, id=user.id), 200

@app.route('/user', methods=['GET'])
@jwt_required()
def get_current_user():
	"""
	Return username associated with current token
	"""
	current_user_id = get_jwt_identity()
	user = User.query.filter_by(id=current_user_id).first()
	return {'user': user.to_dict()}, 200

@app.route('/user/courses', methods=['GET'])
@jwt_required()
def get_current_users_courses():
	"""
	Return all courses of current user
	"""
	current_user_id = get_jwt_identity()
	user = User.query.filter_by(id=current_user_id).first()
	courses = [course.to_dict() for course in user.courses]
	return {'user': user.to_dict(), 'courses': courses}

@app.route('/user/courses', methods=['POST'])
@jwt_required()
def add_user_course():
	"""
	Add course to user_course table for current user
	"""
	course_id = request.json.get('course_id')
	if not course_id:
		return {'response': 'Missing data'}, 400
	current_user_id = get_jwt_identity()
	user = User.query.filter_by(id=current_user_id).first()
	course = Course.query.filter_by(id=course_id).first()
	print(f'\nuser: {user.to_dict()}\n')
	print(f'\ncourse: {course}\n')
	user.courses.append(course)
	db.session.commit()
	print(f'\nuser.courses:{user.courses}\n')
	# TODO: better response
	return {'response': 'Success??'}, 200
	


@app.route('/courses', methods=['GET'])
def get_all_courses():
	courses = [course.to_dict() for course in Course.query.all()]
	return {'courses': courses}


@app.route('/courses', methods=['POST'])
@jwt_required()
def add_course():
	department = request.json.get('department')
	number = request.json.get('number')
	name = request.json.get('name')

	if not department or not number or not name:
		return {'response': 'Missing data'}, 400

	# TODO: duplicate validation code. use number? name? 

	course = Course(department=department, number=number, name=name)
	db.session.add(course)
	db.session.commit()
	return jsonify(department=department, number=number, name=name), 200

########## routes made before are below ##########


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
