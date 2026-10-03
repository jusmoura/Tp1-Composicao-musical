import random

from config import CROSSOVER_RATE, GENOME_SIZE

def crossover(parent1, parent2):

    if random.random() > CROSSOVER_RATE:
        return parent1.copy()

    point = random.randint(1, GENOME_SIZE - 1)
    child = (parent1[:point] + parent2[point:])

    return child