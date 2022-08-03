from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tyugkyiqkxxnyi:09b421cce0bf05be569f8e957642cdad63fae40c0fdf6d92deccfe9468be8b2b@ec2-18-204-142-254.compute-1.amazonaws.com:5432/db354593uc8gce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['JWT_SECRET_KEY'] = 'super-secret' # FIXME: change this. config file?
jwt = JWTManager(app)

import tutor_finder.routes