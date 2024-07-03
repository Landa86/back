from flask import request
from models.user import User
from extensions import db

def add_user_function():
    if request.method == "POST":
        name=request.form["name"]
        sex=request.form["sex"]
        email=request.form["email"]
        user = User(
            name=name,
            sex=sex,
            email=email
        )
        
        user.save()
        data = {
            "id":user.id,
            "name":user.name,
            "sex":user.sex,
            "email":user.email
        }
        return data
    
def edit_user_function(data):
    if request.method == "POST":
        data.name=request.form["name"]
        data.sex=request.form["sex"]
        data.email=request.form["email"]
        db.session.commit()
        return data
    
def delete_user_function(user):
    db.session.delete(user)
    db.session.commit()
