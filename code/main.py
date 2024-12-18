import os
from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    send_file,
    jsonify,
)
from api.piano.select_song import select_song
from api.piano.initalize_notes import initalize_notes
from api.piano.key_press import key_press
from api.piano.set_score import set_score
from DBcontrol import showAllSongs, findTitlefromDB
from csvToHTML import toHTML

app = Flask(__name__)
app.secret_key = "KtCAH&EFwPP)wsq4"


@app.route("/")
def render_homepage():
    return render_template("home.html")


@app.route("/api/piano/initialize", methods=["POST"])
def handle_initialize():
    return initalize_notes()


@app.route("/api/piano/selectsong", methods=["POST"])
def handle_song_select():
    data = request.json
    return select_song(data)


@app.route("/api/piano/keypress", methods=["POST"])
def handle_key_press():
    data = request.json
    return key_press(data)


@app.route("/api/piano/setscore", methods=["POST"])
def handle_set_score():
    data = request.json
    return set_score(data)


@app.route("/freeplay")
def render_freeplay():
    session["mode"] = "freeplay"
    session["previous_note"] = 60  # default start note is middle c
    session["score"] = 0
    return render_template("freeplay.html", mode="freeplay")


@app.route("/play-music")
def render_play_music():
    # Initalize session variables
    session["mode"] = "play_music"
    session["score"] = 0
    # session["notes"] = {}
    session["index"] = 0
    songs = []

    # Generate list of available songs
    for _, row in showAllSongs().iterrows():
        songs.append(row["songTitle"])
    return render_template("play_music.html", mode="play_music", songs=songs)


@app.route("/survival")
def render_survival():
    # Initalize session variables
    session["mode"] = "survival"
    session["score"] = 0
    session["previous"] = -1

    return render_template("survival.html", mode="survival")


@app.route("/scoreboard")
def render_scoreboard():
    tables = ""
    tables += "<h3>Survival Highscores</h3>\n"
    tables += toHTML("code/assets/databases/survscore.csv")
    for _, row in showAllSongs().iterrows():
        tables+= "<h3>" + row["songTitle"] + "</h3>\n"
        tables += toHTML("code/assets/databases/" + row["scoreFile"])
    return render_template("scoreboard.html", mode="scoreboard", html=tables)


if __name__ == "__main__":
    app.run(debug=True)
