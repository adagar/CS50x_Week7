from flask import Flask, render_template

app = Flask(__name__)


# if request is for /:
#     then send back home page
# else if request is for /zuck
#     send to zuck's home page (zuck.html)
# else if request is for /login
#     themn prompt for login info

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/zuck")
def zuck():
    return render_template("zuck.html")

@app.route("/login")
def login():
    return render_template("login.html")