from flask import jsonify, abort, session
import mido


def select_song(data):
    # TODO add song init here (will display song name)
    # should be initilized when a specific song is selected
    # Open the MIDI file
    mid = mido.MidiFile("code/assets/songs/" + data["song"] + ".mid")
    print("code/assets/songs/" + data["song"] + ".mid")
    notes = []
    # Iterate over tracks
    for track in mid.tracks:
        for msg in track:
            instruction = str(msg)
            if instruction.__contains__("note_off"):
                notes.append(str(int(instruction[24:26])+12))
    session["notes"] = notes
    # print(session["notes"])
    # print(data['song'])

    print(session['notes'])

    return jsonify(
        {"correctNote": True, "nextNote": session["notes"][session["index"]]}
    )
