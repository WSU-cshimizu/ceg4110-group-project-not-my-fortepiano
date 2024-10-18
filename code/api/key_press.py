from flask import jsonify, abort
import json

def key_press(data):
    # Verify mode is play music or survival
    if data['mode'] == "play_music" or data['mode'] == "survival":
        # TODO: Create logic for next note

        # Return information to user
        # TODO: Fill in values
        return jsonify({'correctNote': True, 'nextNote': '12'})
    else:
        abort(400, description="Missing 'mode' field")