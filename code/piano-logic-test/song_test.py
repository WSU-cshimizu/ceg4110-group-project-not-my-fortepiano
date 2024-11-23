import mido

currentNote = 0

# Open the MIDI file
mid = mido.MidiFile("code/assets/songs/Mary Had a Little Lamb.mid")
notes = []

# Iterate over tracks
for i, track in enumerate(mid.tracks):
    # print(f'Track {i}: {track.name}')

    # Iterate over messages in the track
    for msg in track:
        instruction = str(msg)
        if instruction.__contains__("note_off"):
            notes.append(instruction[24:26])
            print(instruction[24:26])

while True:
    print("current note is " + notes[currentNote])
    if(input() == notes[currentNote]):
        currentNote += 1
    else:
        break