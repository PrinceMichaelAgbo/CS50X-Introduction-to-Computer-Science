from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

db = SQL("sqlite:///lecture.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        if not name or not email:
            return render_template("apology.html", message = "You must submit BOTH a name and an email address")
        db.execute("INSERT INTO registrants (name, email) VALUES (:name, :email)", name=name, email=email)
        return redirect("/")