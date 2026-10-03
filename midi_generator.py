from music21 import (
    stream,
    note,
    tempo,
    meter
)

def create_midi(individual, filename):
    score = stream.Score()
    melody = stream.Part()
    melody.append(tempo.MetronomeMark(number=100))
    melody.append(meter.TimeSignature("4/4"))

    for midi_note in individual:

        music_note = note.Note(midi_note)
        music_note.quarterLength = 1
        melody.append(music_note)

    score.append(melody)
    score.write("midi",fp=filename)