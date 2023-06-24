#ACTIVIDAD ENCUESTA DOJO 
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = "pony puppy"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario", methods = ['POST'])
def formulario():
    session["username"] = request.form["name"]
    session["userlocation"] = request.form["location"]
    session["userlanguage"] = request.form["language"]
    session["usercourse"] = request.form["course"]
    session["usercomment"] = request.form["comment"]
    return redirect("/completado")

@app.route("/completado")
def completado():
    return render_template("completado.html")


if __name__ == "__main__":
    app.run(debug=True, port=5006)