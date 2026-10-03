import random

from genetic_algorithm import run
from midi_generator import create_midi


def main():

    # Música 1
    random.seed(42)

    (best_individual_1, best_history, average_history) = run()

    print("\nBest individual 1:")
    print(best_individual_1)

    create_midi(best_individual_1, "output/music_01.mid")

    # Música 2
    random.seed(100)

    (best_individual_2, _, _) = run()

    print("\nBest individual 2:")
    print(best_individual_2)

    create_midi(best_individual_2, "output/music_02/music_02.mid")

    # Música 3
    random.seed(200)

    (best_individual_3, _, _) = run()

    print("\nBest individual 3:")
    print(best_individual_3)

    create_midi( best_individual_3,"output/music_03/music_03.mid")

if __name__ == "__main__":
    main()