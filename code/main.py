from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, send_file
from api.piano.key_press import key_press
from api.piano.initalize_notes import initalize_notes
import os

app = Flask(__name__)
app.secret_key = 'KtCAH&EFwPP)wsq4'

@app.route('/')
def render_homepage():
    return(render_template('home.html'))

@app.route('/api/piano/keypress', methods=['POST'])
def handle_key_press():
    data = request.json
    return key_press(data)

@app.route('/api/piano/initialize', methods=['POST'])
def handle_initialize():
    return initalize_notes()

@app.route('/freeplay')
def render_freeplay():
    session['mode'] = "freeplay"
    session['previous_note'] = 60 #default start note is middle c
    session['score'] = 0
    return(render_template('freeplay.html', mode='freeplay'))

@app.route('/play-music')
def render_play_music():
    # Initalize session variables
    session['mode'] = "play_music"
    session['score'] = 0
    session['notes'] = {} #notes should be initialized here based on song selected which might need another page
    session['index'] = 0

    return(render_template('play_music.html', mode='play_music'))

@app.route('/survival')
def render_survival():
    # Initalize session variables
    session['mode'] = "survival"
    session['score'] = -1
    session['previous'] = -1

    return(render_template('survival.html', mode='survival'))

if __name__ == '__main__':
    app.run(debug=True)