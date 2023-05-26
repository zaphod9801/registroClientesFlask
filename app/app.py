from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
import os
from importlib import import_module
from dotenv import load_dotenv


load_dotenv()  # carga las variables de entorno desde .env

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_COOKIE_CSRF_PROTECT"] = True
jwt = JWTManager(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)

# Retrasar la importación de modulos
client = import_module('Backend.controllers.client')
city = import_module('Backend.controllers.city')
user = import_module('Backend.controllers.user')

# Crear una instancia de la clase LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(name):
    return user.query.get(name)
