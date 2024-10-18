from flask import jsonify, abort
import fluidsynth
import json


def key_press(data):
    match data["mode"]:
        case "play_music":
            velocity = 127  # 127 is max for Nice-Steinway-Lite-v3.0.sf2
            fs = fluidsynth.Synth()
            fs.start()
            sfid = fs.sfload(
                "assets/instruments/Nice-Steinway-Lite-v3.0.sf2"
            )  # from https://sites.google.com/site/soundfonts4u/
            fs.program_select(0, sfid, 0, 0)
            fs.noteon(0, data["key"], velocity)
        case "survival":
            pass
        case "song":
            pass
        case _:
            abort(400, description="Missing 'mode' field")

    # # # Verify mode is play music or survival
    # # if data['mode'] == "play_music" or data['mode'] == "survival":
    # #     # TODO: Create logic for next note

    # #     # Return information to user
    # #     # TODO: Fill in values
    #     return jsonify({'correctNote': True, 'nextNote': '12'})
    # else:
    #     abort(400, description="Missing 'mode' field")
