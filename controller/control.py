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
    resultado = add_user(id, name, lastname, birthday)
    return "ok"
    
#@app.route("/consult_user", methods=["post"])    
#def consult_user():
 #   print(id, name, lastname, birthday)
  #  return "ok"