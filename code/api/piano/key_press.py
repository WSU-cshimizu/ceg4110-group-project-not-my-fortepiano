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
                return jsonify({"status": 0, "score": session['score'], "correctNote": False, "nextNote": 0})  # exit the mode
            else:
                session["previous_note"] = random.randint(53, 67)
                session["score"] += 1
                return jsonify(
                    {"correctNote": True, "nextNote": session["previous_note"]}
                )

        case "play_music":  # TODO exit on wrong and on song finish
            # print(
            #     "Current index: ",
            #     str(session["index"]),
            #     "\nCurrent note: ",
            #     session["notes"][session["index"]],
            #     "\nPressed key: ",
            #     data["key"],
            #     "\n",
            # )

            # check if the correct key was pressed
            if data["key"] != int(session["notes"][session["index"]]):
                print("final score: ", session["score"])
                return jsonify({"status": 0, "score": session['score'], "correctNote": False, "nextNote": 0})
            session["index"] += 1
            session["score"] += 1
            print("Score: ", session["score"])

            # check if the next note is out of bounds
            if session["index"] >= len(session["notes"]):
                print("final score: ", session["score"])
                return jsonify({"status": 1, "score": session['score'], "correctNote": True, "nextNote": 0})
            return jsonify(
                {
                    "correctNote": True,
                    "nextNote": session["notes"][session["index"]],
                }
            )

        case _:
            abort(400, description="Missing 'mode' field")
