from flask_sqlalchemy import SQLAlchemy
from upload import db, bcrypt
from datetime import datetime
from flask_login import UserMixin
import uuid

class Users(db.Model, UserMixin):

    __tablename__ = "Users"

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    creationDate = db.Column(db.DateTime)
    accessDate = db.Column(db.DateTime)

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.creationDate = datetime.today()
        self.accessDate = datetime.today()
