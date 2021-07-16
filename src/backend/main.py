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
    population_data = {"time_elapsed": [],
                       "population_size": [], "population_fitness": []}
    df_population = pd.DataFrame(population_data)

    while True:
        # cycle the population
        population.cycle(difficulty, percent)

        # calculate various population parameters
        population_size = len(population._members)
        population_avg_fitness = population.mean_fitness()

        population_data_next = {"time_elapsed": count, "population_size": population_size,
                                "population_avg_fitness": population_avg_fitness}

        population_fitness = []
        for i in population._members:
            population_fitness.append(i._fitness)

        df_fitness = pd.DataFrame(population_fitness, columns=['fitness'])

        # write out population size for line plot
        with open('../csv/population_data.csv', 'w') as output1:
            df_population = df_population.append(
                population_data_next, ignore_index=True)
            df_population.to_csv(output1, index=False, sep=',')
        output1.close()

        # write out fitness distribution for kde plot
        with open('../csv/fitness_distribution.csv', 'w') as output2:
            df_fitness.to_csv(output2, index=False, sep=',')
        output2.close()

        count += 1


main()
