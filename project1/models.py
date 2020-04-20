import sys
from flask_sqlalchemy import SQLAlchemy
# from passlib.hash import bcrypt
from datetime import datetime 
db = SQLAlchemy()

class UserForm(db.Model):

    __tablename__ = "Details"
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False)

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.timestamp = datetime.now()