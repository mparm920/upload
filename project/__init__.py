import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#config
app.config.from_object(os.environ['APP_SETTINGS'])
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from project.user.views import user_blueprint
from project.login.views import login_blueprint
from project.upload.views import upload_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(upload_blueprint)