import pandas as pd
import csv

from organism import Organism
from population import Population


def main(init_genotype_distribution=0.2, difficulty=1.2, n=100, percent=0.2, difficulty_increases=False, difficulty_increase=0.05):
    population = Population([], init_genotype_distribution, difficulty, n)

    # prepare line plot
    popdata = open('../csv/population_data.csv', 'w', newline='')

    fieldnames = ['time_elapsed', 'population_size', 'average_fitness']
    init_writer = csv.DictWriter(popdata, fieldnames=fieldnames)
    init_writer.writeheader()

    popdata.close()

    # count time elapsed
    time = 0

    while True:
        # cycle the population
        population.cycle(difficulty, percent)

        # calculate various population parameters
        population_size = len(population._members)
        average_fitness = population.mean_fitness()

        # dictionary structures for line plot csv
        next_row = {'time_elapsed': time, 'population_size': population_size,
                    'average_fitness': average_fitness}

        with open('../csv/population_data.csv', 'a', newline='') as output:
            writer = csv.DictWriter(
                output, fieldnames=fieldnames, delimiter=',')
            writer.writerow(next_row)
        output.close()

        # write out for fitness kde
        fitness_data = [{'fitness': None}]

        for i in population._members:
            next = {'fitness': i._fitness}
            fitness_data.append(next)

        fitness_dataframe = pd.DataFrame(fitness_data)
        fitness_dataframe = fitness_dataframe.iloc[1:, :]

        with open('../csv/fitness_distribution.csv', 'w', newline='') as output:
            fitness_dataframe.to_csv(
                output, sep=',', index=False, line_terminator='\n', encoding='utf-8', header=False)
        output.close()

        # increment time
        time += 1


main()
