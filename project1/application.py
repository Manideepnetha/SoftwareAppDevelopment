import os
import datetime

from flask import Flask, session,flash,logging,redirect,url_for
from flask_session import Session
from flask import render_template
from flask import request
import hashlib
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
import sys, os, time, calendar;
from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
db.init_app(app)
# def main():
#     db.create_all()

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
# session = db()


# @app.route("/")
# def index():
#     return "Project 1: TODO"

@app.route("/", methods = ["GET","POST"])
def register():
    db.create_all()
    if request.method == 'POST':
        data = request.form
        userdata = UserForm(request.form['name'],request.form['psw'])
        user = UserForm.query.filter_by(email=request.form['name']).first()

        if user is not None:
            print("User is already existing. Please try to register with a new")
            # var1 = "Error: User is already existing. Please try to register with a new one"
            return render_template("Register.html")
        db.session.add(userdata)
        db.session.commit()
        # print("Registration Success")
        # var1 ='Registration Success'
        return render_template("Register.html")
    else:
        return render_template("Register.html")
    
    


@app.route("/admin", methods = ["GET"])
def users_info():
    data = UserForm.query.order_by(desc(UserForm.timestamp)).all()
    print(data)
    data = UserForm.query.all()
    return render_template("admin.html",data = data) 

@app.route("/auth", methods=["GET","POST"])
def auth():
    if request.method=="POST":
        email = request.form.get("name")   
        password = request.form.get("psw")
        # PS = bcrypt.encrypt(password)
        print(password)
        ID = UserForm.query.get(email)

        if ID != None:
            if password == ID.password:
                print(password)
                session["email"]= email
                return render_template("UserPage.html")
            else:
                return "invalid password"
        else:
            return "Please check the entered email and password"

@app.route("/search", methods=["GET"])
def search():
    if session["email"] == None:
        return redirect(url_for("/logout"))
    else:
        return "Successfully"

@app.route("/logout", methods=["GET","POST"])
def logout():
    if request.method == "POST":
        session["email"] = None
        return redirect(url_for("/"))

if __name__ == "__main__":
    with app.app_context():
        main() 
