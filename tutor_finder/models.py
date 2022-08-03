from tutor_finder import db
from werkzeug.security import generate_password_hash, check_password_hash


user_course = db.Table('user_course',
	db.Column('user_id', db.Integer, db.ForeignKey('app_user.id')),
	db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)


class User(db.Model):
	# Table is called 'app_user' because 'user' would conflict with postgres keyword
	__tablename__ = 'app_user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True)
	email = db.Column(db.String(120), unique=True)
	password_hash = db.Column(db.String(128))
	courses = db.relationship('Course', secondary=user_course, backref='enrolled')

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
