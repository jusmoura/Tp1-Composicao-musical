import random

from fitness import fitness


def tournament_selection(population):
    tournament = random.sample(
        population,
        3
    )

    return max(
        tournament,
        key=fitness
    )