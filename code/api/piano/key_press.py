from flask import jsonify, abort, session
# import fluidsynth
# import mido
# import json
import random

# Access persistent/'saved' variables in session variable
# All session variables are guaranteed start state. View 'main.py'
def key_press(data):
    match data["mode"]:
        case "survival":
            # # should be initilized when survival mode is selected
            # previousNote = random.randint(53, 67)
            # score = 0
            print(session["score"])
            if session["previous_note"] != data["key"]:
                return jsonify({"correctNote": False, "nextNote": 0})  # exit the mode
            else:
                session["previous_note"] = random.randint(53, 67)
                session["score"] += 1
                return jsonify({"correctNote": True, "nextNote": session["previous_note"]})
            
        case "play_music":
            print("current note is " + session["notes"][session["index"]] )
            if data["key"] == session["notes"][session["index"]]:
                session["index"] += 1
                return jsonify(
                    {"correctNote": True, "nextNote": session["notes"][session["index"]]}
                )
            else:
                return jsonify({"correctNote": False, "nextNote": 0})  # exit the mode

        case _:
            abort(400, description="Missing 'mode' field")