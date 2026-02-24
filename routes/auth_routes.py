from flask import Blueprint, render_template, request, redirect, session
from database.db import users
import bcrypt

auth = Blueprint("auth", __name__)


# ================= REGISTER =================
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Hash password
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        users.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password,
            "role": "user"
        })

        return redirect("/login")

    return render_template("register.html")



# ================= LOGIN =================
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = users.find_one({"email": email})

        if user and user["password"] == password:

            session["user"] = email
            session["role"] = user.get("role", "user")

            return redirect("/")

        else:
            return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")


# ================= LOGOUT =================
@auth.route("/logout")
def logout():

    session.clear()
    return redirect("/login")