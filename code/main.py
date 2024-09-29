from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os

app = Flask(__name__)

@app.route('/')
def render_homepage():
    return(render_template('base.html'))

@app.route('/freeplay')
def render_freeplay():
    return(render_template('freeplay.html'))

@app.route('/play-music')
def render_play_music():
    return(render_template('play_music.html'))

@app.route('/survival')
def render_survival():
    return(render_template('survival.html'))

if __name__ == '__main__':
    app.run(debug=True)