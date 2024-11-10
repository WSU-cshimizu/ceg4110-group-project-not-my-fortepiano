from flask import jsonify, abort, session

def select_song(data):
    # TODO add song init here (will display song name)

    print(data['song'])

    return jsonify({})