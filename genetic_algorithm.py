import random

from config import (
    POPULATION_SIZE,
    GENERATIONS
)

from fitness import fitness
from selection import tournament_selection
from crossover import crossover
from mutation import mutate


def create_individual():
    from config import (
        GENOME_SIZE,
        LOW_NOTE,
        HIGH_NOTE
    )

    return [
        random.randint(LOW_NOTE, HIGH_NOTE)
        for _ in range(GENOME_SIZE)
    ]

def create_population():
    return [
        create_individual()
        for _ in range(POPULATION_SIZE)
    ]

def create_next_generation(population):
    new_population = []

    best = max(population, key=fitness)
    new_population.append(best.copy())

    while len(new_population) < POPULATION_SIZE:

        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)

    return new_population

def run():
    population = create_population()

    best_history = []
    average_history = []

    best_individual = None
    best_score = float("-inf")

    for generation in range(GENERATIONS):

        scores = [
            fitness(individual)
            for individual in population
        ]

        current_best_score = max(scores)

        current_best = population[
            scores.index(current_best_score)
        ]

        average_score = sum(scores) / len(scores)

        best_history.append(current_best_score)
        average_history.append(average_score)

        if current_best_score > best_score:
            best_score = current_best_score
            best_individual = current_best.copy()

        print(
            f"Generation {generation + 1}: "
            f"best={current_best_score:.2f}, "
            f"average={average_score:.2f}"
        )

        population = create_next_generation(
            population
        )

    return (
        best_individual,
        best_history,
        average_history
    )