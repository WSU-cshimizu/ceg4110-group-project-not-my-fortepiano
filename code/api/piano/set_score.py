from flask import jsonify, abort, session
from io import StringIO
import random
import sys
import DBcontrol


def set_score(data):
    # TODO set score data.name contains name to assign score to
    # print(session["score"])
    match session["mode"]:
        case "survival":            
            # sys.stdin = StringIO(data["name"])
            DBcontrol.loadSurvScore(session["score"],data["name"])
            return jsonify({})
        case "play_music":
            # sys.stdin = StringIO(data["name"])
            DBcontrol.loadSongScore(session["song"],session["score"],data["name"])
            # DBcontrol.loadSongScore(session["song"],session["score"])
            return jsonify({})
        case _:
            abort(400, description="Missing 'mode' field")
