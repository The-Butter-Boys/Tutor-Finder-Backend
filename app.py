from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tyugkyiqkxxnyi:09b421cce0bf05be569f8e957642cdad63fae40c0fdf6d92deccfe9468be8b2b@ec2-18-204-142-254.compute-1.amazonaws.com:5432/db354593uc8gce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)

    def __init__(self, username):
        self.username = username


@app.route('/users')
def users():
    return jsonify([{'name': 'Colin'}, {'name': 'Dexter'}, {'name': 'Bob'}])


