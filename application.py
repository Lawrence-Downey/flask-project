from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    imageFile = url_for('static', filename='/nowPlaying.jpg')
    return render_template("Home.html", imageFile=imageFile)


@app.route("/collection")
def collection():
    #toyStoryPoster = url_for('static', filename='static/ToyStoryPoster.jpg')
    tmntPoster = url_for('static', filename='/teenageMutantNinjaTurtlesPoster.jpg')
    grinchPoster = url_for('static', filename='/howTheGrinchStoleChristmasPoster.jpg')
    homeAlonePoster = url_for('static', filename='/homeAlonePoster.jpg')
    return render_template("collection.html", tmntPoster=tmntPoster,
                           grinchPoster=grinchPoster, homeAlonePoster=homeAlonePoster)


@app.route("/addMovie")
def addMovie():
    return render_template("addMovie.html")


@app.route("/removeMovie")
def removeMovie():
    return render_template("removeMovie.html")
