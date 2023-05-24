from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from importlib import import_module

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)

# Retrasar la importación de 'client'
client = import_module('Backend.controllers.client')
