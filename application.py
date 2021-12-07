from flask import Flask, render_template


app = Flask(__name__)


@app.route("/Home")
def home():
    return render_template("Home.html")

@app.route("/collection")
def collection():
    return render_template("collection.html")

