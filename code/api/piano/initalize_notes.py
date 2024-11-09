from flask import jsonify, abort, session
import random

def initalize_notes():
    match session["mode"]:
        case "survival":
            session["previous_note"] = random.randint(53, 67)
            return jsonify({"nextNote": session["previous_note"]})
        case "play_music":
            # TODO init songs
            return jsonify({})
        case _:
            abort(400, description="Wrong mode for initilization")
            return jsonify({"error": "Wrong mode"})