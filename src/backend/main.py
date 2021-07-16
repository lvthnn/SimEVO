import pandas as pd
import time
import csv

from organism import Organism
from population import Population


def main(init_genotype_distribution=0.2, difficulty=1.2, n=100, percent=0.2, difficulty_increases=False, difficulty_increase=0.05):
    population = Population([], init_genotype_distribution, difficulty, n)

    # count time elapsed
    count = 0

    # csv data structure and initialization
    # while refining the algorithm, we will use termplotlib
    # to facilitate visualization of data and stop outputting
    # to csv

    data = {"time_elapsed": [], "population_size": [], "population_fitness": []}
    df = pd.DataFrame(data)

    while True:
        # cycle the population
        population.cycle(difficulty, percent)

        # calculate various population parameters
        population_size = len(population._members)
        population_fitness = population.mean_fitness()

        next_row = {"time_elapsed": count, "population_size": population_size,
                    "population_fitness": population_fitness}

        # write out calculated values to csv and
        # increment time counter
        df = df.append(next_row, ignore_index=True)
        df.to_csv('csv/data_plot.csv', index=False)
        count += 1


main()
