import sqlite3
from contextlib import closing
from flask import Flask, render_template, url_for, request



app = Flask(__name__)

conn = sqlite3.connect("movies.db")
conn.row_factory = sqlite3.Row



@app.route("/")
def home():
    imageFile = url_for('static', filename='/nowPlaying.jpg')
    width = "560"
    height = "315"
    allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    title = "Youtube Video Player"
    frameborder = "0"
    video1 = "https://www.youtube.com/embed/nVeNlaUCa2E?autoplay=1&mute=1&loop=1&controls=0"
    video2 = "https://www.youtube.com/embed/cS-NPzaDX80?autoplay=1&mute=1&loop=1&controls=0"
    video3 = "https://www.youtube.com/embed/0lq1JIWQSlc?autoplay=1&mute=1&loop=1&controls=0"
    video4 = "https://www.youtube.com/embed/N-Esh4W3dfI?autoplay=1&mute=1&loop=1&controls=0"
    video5 = "https://www.youtube.com/embed/pbFma8Bd-AI?autoplay=1&mute=1&loop=1&controls=0"
    video6 = "https://www.youtube.com/embed/uqHjMd4Oci4?autoplay=1&mute=1&loop=1&controls=0"
    return render_template("Home.html", imageFile=imageFile, width=width, height=height, allow=allow,
                           title=title, frameborder=frameborder, video1=video1, video2=video2, video3=video3,
                           video4=video4, video5=video5, video6=video6)


@app.route("/collection")
def collection(conn):
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM movies'''
        c.execute(query)
        results = c.fetchall()
    listOfMovies = []
    for row in results:
        listOfMovies.append(row)
    if conn:
        conn.close()
    width = "500"
    height = "700"

    return render_template("collection.html", listOfMovies=listOfMovies, width=width, height=height)


@app.route("/addMovie", methods=["GET", "POST"])
def addMovie(conn):
    #if request.method == "POST":
    filename = request.form.get("filename")
    movieTitle = request.form.get("movieTitle")
    runtime = request.form.get("runtime")
    starring = request.form.get("starring")
    genre = request.form.get("genre")
    boxOffice = request.form.get("boxOffice")

    with closing(conn.cursor()) as c:
        query = '''INSERT INTO movies (filename, movieTitle, runtime,
                                        starring, genre, boxOffice)
                    VALUES (?, ?, ?, ?, ?, ?)'''
        c.execute(query, (filename, movieTitle, runtime, starring, genre, boxOffice))
        conn.commit()
    return render_template("addMovie.html")


@app.route("/removeMovie")
def removeMovie():
    removeImage = url_for('static', filename='/removeMovieImage.jpg')
    width = "450"
    height = "450"
    return render_template("removeMovie.html", removeImage=removeImage, width=width, height=height)


@app.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    return render_template("login.html", boolean=True)
