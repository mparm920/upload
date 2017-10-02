from flask_sqlalchemy import SQLAlchemy
from upload import db, bcrypt
from datetime import datetime
from flask_login import UserMixin
import uuid

class Companies(db.Model):
    __tablename__="Companies"

    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String)
    user_id = db.relationship("Users", backref="Companies")

    def __init__(self, companyName):
        self.companyName = companyName

class Users(db.Model, UserMixin):

    __tablename__ = "Users"

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    creationDate = db.Column(db.DateTime)
    accessDate = db.Column(db.DateTime)
    companyName = db.Column(db.Integer, db.ForeignKey("Companies.id"))


    def __init__(self, email, password, companyName):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.creationDate = datetime.today()
        self.accessDate = datetime.today()
        self.companyName = Companies.query.filter_by(companyName=companyName).first().id
