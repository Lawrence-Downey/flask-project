from flask import Flask, render_template, redirect, request, abort


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Home.html")


