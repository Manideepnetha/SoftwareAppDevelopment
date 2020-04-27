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

# import sys
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class  Star(db.Model):

    _tablename_ = "User Review"
    UserName = db.Column(db.String, nullable=False, primary_key=True)
    Book_ID = db.Column(db.Integer, primary_key=True)
    Rating = db.Column(db.String, nullable=False)
    Feedback = db.Column(db.String(140),nullable=False)
    
    def _init_(self,UserName, Book_ID, Rating, Feedback) :
        self.UserName = UserName
        self.Book_ID = Book_ID
        self.Rating = Rating
        self.Feedback = Feedback