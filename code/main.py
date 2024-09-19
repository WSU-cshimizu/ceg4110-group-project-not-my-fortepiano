from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os

app = Flask(__name__)

@app.route('/')
def render_homepage():
    return(render_template('home.html'))

if __name__ == '__main__':
    app.run(debug=True)