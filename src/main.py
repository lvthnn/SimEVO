import matplotlib.pyplot as plt
import time

from organism import Organism
from population import Population


def main(n=1000, difficulty=0.5, init_genotype_distribution=0.2, difficulty_increases=False, difficulty_increase=0.05):
    # Declare initial variables:
    population = Population([], init_genotype_distribution,
                            difficulty, n)

    count = 0
    t_elapsed = []

    while True:
        population.tick()
        population.check_population(difficulty, 1.0)
        population.population_reproduction()

        population_n = len(population._members)
        plt.plot(count, population_n)
        plt.show()

        t_elapsed.append(count)
        count += 1

        time.sleep(0.1)


main()
