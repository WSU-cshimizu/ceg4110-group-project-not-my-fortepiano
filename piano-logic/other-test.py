import mido

# Open the MIDI file
mid = mido.MidiFile('Mary-Had-a-Little-Lamb.mid')

# Iterate over tracks
for i, track in enumerate(mid.tracks):
    # print(f'Track {i}: {track.name}')

    # Iterate over messages in the track
    for msg in track:
        print(msg)
        
