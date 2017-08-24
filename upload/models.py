from flask_sqlalchemy import SQLAlchemy
from upload import db
import uuid

class Users(db.Model):
    
    __tablename__ = "Users"

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    creationDate = db.Column(db.DateTime)
    accessDate = db.Column(db.DateTime)

    def __init__(self, email, password, creationDate, accessDate):
        self.email = email
        self.password = password
        self.creationDate = creationDate
        self.accessDate = accessDate