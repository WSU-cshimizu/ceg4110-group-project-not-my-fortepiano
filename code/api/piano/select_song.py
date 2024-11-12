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
                notes.append(instruction[24:26])
                # notes.append(str(int(instruction[24:26])+12))
    avg = 0
    shift = 0
    print(1)
    for note in notes:
        avg += int(note)
    avg = avg / len(notes)
    print(2)
    print(avg)
    while avg < 53 or avg > 67:
        if avg < 53:
            shift += 1
            avg = float(avg) + 12
        else:
            shift -= 1
            avg = float(avg) - 12
    print(3)
    for i, note in enumerate(notes):
        print(i)
        notes[i] = int(note) + shift * 12
    session["notes"] = notes
    # print(session["notes"])
    # print(data['song'])

    print(session["notes"])

    return jsonify(
        {"correctNote": True, "nextNote": session["notes"][session["index"]]}
    )
