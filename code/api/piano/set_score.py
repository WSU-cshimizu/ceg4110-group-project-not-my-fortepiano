from flask import jsonify, abort, session
from io import StringIO
import random
import sys
import DBcontrol


def set_score(data):
    # TODO set score data.name contains name to assign score to
    # print(session["score"])
    sys.stdin = StringIO(data["name"])
    DBcontrol.loadSurvScore(session["score"])
    return jsonify({})
