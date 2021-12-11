import os
import sqlite3
from contextlib import closing
from flask import Flask, render_template, url_for, request, flash
from werkzeug.utils import secure_filename, redirect


app = Flask(__name__)
app.config["UPLOAD_PATH"] = "static"
app.secret_key = "Jiggs Dinner"
conn = sqlite3.connect("movies.db", check_same_thread=False)
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
def collection():
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM movies'''
        c.execute(query)
        results = c.fetchall()
    listOfMovies = []
    for row in results:
        listOfMovies.append(row)
    width = "500"
    height = "700"

    return render_template("collection.html", listOfMovies=listOfMovies, width=width, height=height)

@app.route("/addMovie")
def addMovie():
    return render_template("addMovie.html")

@app.route("/addMovie", methods=["POST"])
def newMovie():
    uploadFile = request.files["file"]
    filename = secure_filename(uploadFile.filename)
    movieTitle = request.values["movieTitle"]
    runtime = request.values["runtime"]
    starring = request.values["starring"]
    genre = request.values["genre"]
    boxOffice = request.values["boxOffice"]
    uploadFile.save(os.path.join(app.config["UPLOAD_PATH"], filename))

    with closing(conn.cursor()) as c:
        query = '''INSERT INTO movies (filename, movieTitle, runtime,
                                        starring, genre, boxOffice)
                    VALUES (?, ?, ?, ?, ?, ?)'''
        c.execute(query, (filename, movieTitle, runtime, starring, genre, boxOffice))
        conn.commit()
    return redirect("/")

@app.route("/removeMovie")
def removeMovie():
    return render_template("removeMovie.html")

@app.route("/removeMovie", methods=["GET", "POST"])
def trashMovie():
    removeImage = url_for('static', filename='/removeMovieImage.jpg')
    width = "500"
    height = "500"
    movieTitle = request.form.get("movieTitle")

    with closing(conn.cursor()) as c:
        query = '''DELETE FROM movies
                        WHERE movieTitle = ?'''
        c.execute(query, (movieTitle,))
        conn.commit()
    return render_template("removeMovie.html", removeImage=removeImage, width=width, height=height)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.values["username"]
        password = request.values["password"]

        with closing(conn.cursor()) as c:
            query = '''Select username, password from users
                        Where username = ? AND password = ?'''
            c.execute(query, (username, password,))
            user = c.fetchone()

        if username == user[0] and password == user[1]:
            return redirect(url_for("collection"))
        else:
            return redirect(url_for("errorPage"))
    return render_template("login.html", boolean=True)


@app.route("/createAccount", methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        username = request.values["username"]
        password1 = request.values["password1"]
        password2 = request.values["password2"]

        with closing(conn.cursor()) as c:
            query = '''Select username, password from users
                        Where username = ?'''
            c.execute(query, (username,))
            user = c.fetchone()

        if username == "":
            flash("Field cannot be blank!", "Error 336")
            return redirect(url_for("errorPage"))
        elif len(username) <= 4:
            flash("Username must be more than 4 characters!", "Error 628")
            return redirect(url_for("errorPage"))
        elif password2 != password1:
            flash("Passwords must match!", "Error 166")
            return redirect(url_for("errorPage"))
        elif username == user:
            flash("That username is already taken!", "Error 007")
            return redirect(url_for("errorPage"))
        elif password1 == "":
            flash("Field cannot be blank!", "Error 336")
            return redirect(url_for("errorPage"))
        elif password2 == "":
            flash("Field cannot be blank!", "Error 336")
            return redirect(url_for("errorPage"))
        else:
            with closing(conn.cursor()) as c:
                sql = '''Insert into users (username, password)
                         values (?, ?)'''
                c.execute(sql, (username, password1,))
                conn.commit()
                return redirect(url_for("login"))
    return render_template("createAccount.html")

@app.route("/logout")
def logout():
    return redirect(url_for("login", boolean=False))

@app.route("/error")
def errorPage():
    loginFailedImage = url_for('static', filename='/LoginFailed.jpg')
    width = "560"
    height = "315"
    return render_template("errorPage.html", loginFailedImage=loginFailedImage, width=width, height=height)