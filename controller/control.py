from database.db import *
from flask import render_template, request

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")
    
def func_register_user():
    id = request.form["id"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthday = request.form["birthday"]
    print(id, name, lastname, birthday)
    confirm_user = add_user(id, name, lastname, birthday)
    if confirm_user:
        return "<h1>the user was succesfully created</h1>"
    else:
        return "<h1>Error: the user was not created</h1>"
        
def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    passw = obj_user["passw"] #es solo para una prueba
    result_data = consult_user(id)
    response = ""
    if result_data != False and len(result_data) != 0:
        response = {
            'status' : "ok",
            'name' : result_data[0][1]
        }
    else:
        response = {
            'status' : "error"
        }
    return response