import os
import smtplib
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

if not os.getenv("PASSWORD:"):
    raise RuntimeError("missing PASSWORD")

students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    email = request.form.get("email")
    if not name or not dorm or not email:
        return render_template("failure.html")
    message = "You are registered got the 'Slap the banjo' bluegrass event"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("jharvard@c50.net", os.getenv("PASSWORD"))
    server.sendmail("jharvard@cs50.net", email, message)
    return render_template("success.html")