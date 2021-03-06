from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '17e5fa9c145c7b2f39e931363a21ed38'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yash:Splender99#@localhost:3306/flaskdb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskwebapp import routes