import matplotlib.pyplot as plt
import time

from organism import Organism
from population import Population


def main(init_genotype_distribution=0.2, difficulty=0.5, n=100, difficulty_increases=False, difficulty_increase=0.05):
    # Declare initial variables:
    population = Population([], init_genotype_distribution,
                            difficulty, n)

    count = 0
    t_elapsed = []
    t_population_size = []

    while True:
        population.tick()
        population.check_population(difficulty, 1.0)
        population.population_reproduction()

        population_size = len(population._members)
        t_population_size.append(population_size)

        population_fitness = population.calc_mean_fitness()

        t_elapsed.append(count)
        count += 1

        print("time {time}: population size:  {pop_size}     average fitness:  {avg}    difficulty: {diff}".format(
            time=count, pop_size=population_size, avg=population_fitness, diff=difficulty))

        time.sleep(0.5)


main()
