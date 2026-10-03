POPULATION_SIZE = 100
GENERATIONS = 200

MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.8

NUM_BARS = 12
NOTES_PER_BAR = 4
GENOME_SIZE = NUM_BARS * NOTES_PER_BAR

LOW_NOTE = 60
HIGH_NOTE = 84

BLUES_SCALE = [0, 3, 5, 6, 7, 10]

CHORDS = [
    [60, 64, 67, 70],  # C7
    [60, 64, 67, 70],  # C7
    [60, 64, 67, 70],  # C7
    [60, 64, 67, 70],  # C7

    [65, 69, 72, 75],  # F7
    [65, 69, 72, 75],  # F7

    [60, 64, 67, 70],  # C7
    [60, 64, 67, 70],  # C7

    [67, 71, 74, 77],  # G7
    [65, 69, 72, 75],  # F7

    [60, 64, 67, 70],  # C7
    [67, 71, 74, 77]   # G7
]