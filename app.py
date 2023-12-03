from flask import Flask
from config import Config
from models import db
from views import user
from flask_migrate import Migrate
# from models import User

application = Flask(__name__)
application.config.from_object(Config)

db.init_app(application)
application.register_blueprint(user)
migrate = Migrate(application, db)

from flask import Flask, request, jsonify
from views import user
