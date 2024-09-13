from flask import Flask, render_template
from . import db

app = Flask(__name__)
db.init_app(app)
from . import auth
app.register_blueprint(auth.bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)



