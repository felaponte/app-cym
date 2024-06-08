from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register_page")
def register_page():
    return render_template("register.html")
    
@app.route("/register_user", methods=["post"])    
def register_user():
    id = request.form["id"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthday = request.form["birthday"]
    print(id, name, lastname, birthday)
    return "ok"
    
if __name__ == "__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host, port)