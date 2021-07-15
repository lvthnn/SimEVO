import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import time
import csv

from organism import Organism
from population import Population


def main(init_genotype_distribution=0.2, difficulty=0.5, n=100, difficulty_increases=False, difficulty_increase=0.05):
    population = Population([], init_genotype_distribution, difficulty, n)

    # time indexing count
    count = 0

    # csv data
    data = {"time_elapsed": [], "population_size": [], "population_fitness": []}
    df = pd.DataFrame(data)

    # csv paths
    path_plot = "csv/data_plot.csv"

    while True:
        # cycle the population
        population.cycle(difficulty)

        # calculate various population parameters
        population_size = len(population._members)
        population_fitness = population.calc_mean_fitness()

        next_row = {"time_elapsed": count, "population_size": population_size,
                    "population_fitness": population_fitness}

        print(df)
        df = df.append(next_row, ignore_index=True)
        count += 1

        df.to_csv('csv/data_plot.csv', index=False)

        time.sleep(0.2)


main()
