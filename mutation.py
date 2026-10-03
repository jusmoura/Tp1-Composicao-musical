import random

from config import (
    MUTATION_RATE,
    LOW_NOTE,
    HIGH_NOTE
)

def mutate(individual):
    child = individual.copy()
    for i in range(len(child)):
        if random.random() < MUTATION_RATE:
            child[i] = random.randint(LOW_NOTE, HIGH_NOTE)
    return child