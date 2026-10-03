from config import (
    BLUES_SCALE,
    CHORDS,
    NOTES_PER_BAR
)

def is_in_blues_scale(midi_note):
    pitch_class = midi_note % 12
    blues_pitch_classes = [
        (60 + interval) % 12
        for interval in BLUES_SCALE
    ]

    return pitch_class in blues_pitch_classes

def scale_fitness(individual):
    score = 0
    for midi_note in individual:
        if is_in_blues_scale(midi_note):
            score += 2
        else:
            score -= 1

    return score

def chord_fitness(individual):
    score = 0

    for i, midi_note in enumerate(individual):

        bar = i // NOTES_PER_BAR

        chord_notes = CHORDS[bar]

        chord_pitch_classes = [
            note % 12
            for note in chord_notes
        ]

        if midi_note % 12 in chord_pitch_classes:
            score += 3
        else:
            score -= 1

    return score

def interval_fitness(individual):
    score = 0

    for i in range(1, len(individual)):

        interval = abs(
            individual[i] - individual[i - 1]
        )

        if interval <= 5:
            score += 2

        elif interval <= 9:
            score += 1

        else:
            score -= 2

    return score

def repetition_fitness(individual):
    score = 0

    for i in range(len(individual) - 4):

        if individual[i] == individual[i + 4]:
            score += 1

    return score

def diversity_fitness(individual):
    unique_notes = len(set(individual))

    if unique_notes < 4:
        return -10

    if unique_notes > 15:
        return 5

    return 3

def fitness(individual):
    return (
        scale_fitness(individual)
        + chord_fitness(individual)
        + interval_fitness(individual)
        + repetition_fitness(individual)
        + diversity_fitness(individual)
    )