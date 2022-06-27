from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tyugkyiqkxxnyi:09b421cce0bf05be569f8e957642cdad63fae40c0fdf6d92deccfe9468be8b2b@ec2-18-204-142-254.compute-1.amazonaws.com:5432/db354593uc8gce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)

    def __init__(self, username):
        self.username = username

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
    user = User(username)
    db.session.add(user)
    db.session.commit()
    return 'response'
