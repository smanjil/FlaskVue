
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object('config')

db = SQLAlchemy(app)

from app import models, views

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
