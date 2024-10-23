from flask import jsonify, abort, session
import fluidsynth
import mido
import json
import random

currentNote = 0

# Access persistent/'saved' variables in session variable
# All session variables are guaranteed start state. View 'main.py'
def key_press(data):
    match data["mode"]:
        case "play_music":
            # should be initilized when play_music mode is selected
            velocity = 127  # 127 is max for Nice-Steinway-Lite-v3.0.sf2
            fs = fluidsynth.Synth()
            fs.start()
            sfid = fs.sfload(
                "assets/instruments/Nice-Steinway-Lite-v3.0.sf2"
            )  # from https://sites.google.com/site/soundfonts4u/
            fs.program_select(0, sfid, 0, 0)

            # unclear how this sound is passed to the front
            fs.noteon(0, data["key"], velocity)
        case "survival":
            # should be initilized when survival mode is selected
            previousNote = random.randint(53, 67)
            score = 0

            if previousNote != data["key"]:
                return jsonify({"correctNote": False, "nextNote": 0})  # exit the mode
            else:
                previousNote = random.randint(53, 67)
                score += 1
                return jsonify({"correctNote": True, "nextNote": previousNote})
            
        case "song":
            # should be initilized when a specific song is selected
            # Open the MIDI file
            mid = mido.MidiFile("assets/songs/Mary Had a Little Lamb.mid")
            notes = []
            # Iterate over tracks
            for track in mid.tracks:
                for msg in track:
                    instruction = str(msg)
                    if instruction.__contains__("note_off"):
                        notes.append(instruction[24:26])

            global currentNote
            print("current note is " + instruction[currentNote])
            if data["key"] == instruction[currentNote]:
                currentNote += 1
                return jsonify(
                    {"correctNote": True, "nextNote": instruction[currentNote]}
                )
            else:
                return jsonify({"correctNote": False, "nextNote": 0})  # exit the mode

        case _:
            abort(400, description="Missing 'mode' field")