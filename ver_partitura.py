from music21 import converter

score = converter.parse("output/music_03/music_03.mid")

score.write(
    "musicxml",
    fp="output/music_03/music_03.musicxml"
)

print("Partitura criada!")