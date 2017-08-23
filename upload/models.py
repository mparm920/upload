from flask_sqlalchemy import SQLAlchemy
from upload import db
import uuid

class Users(db.Model):
   id = db.Column(db.integer, primary_key=True) 
   email = db.Column(db.String(), unique=True)
   password = db.Column(db.String())
   creationDate = db.Column(db.DateTime())
   accessDate = db.Column(db.DateTime())