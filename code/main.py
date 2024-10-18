from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, send_file
from api.key_press import key_press
import os

app = Flask(__name__)

@app.route('/')
def render_homepage():
    return(render_template('base.html'))

@app.route('/api/keypress', methods=['POST'])
def handle_key_press():
    data = request.json
    return key_press(data)

@app.route('/freeplay')
def render_freeplay():
    return(render_template('freeplay.html', mode='freeplay'))

@app.route('/play-music')
def render_play_music():
    return(render_template('play_music.html', mode='play_music'))

@app.route('/survival')
def render_survival():
    return(render_template('survival.html', mode='survival'))

if __name__ == '__main__':
    app.run(debug=True)