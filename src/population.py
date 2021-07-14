from organism import Organism

import random
import math


class Population:

    def __init__(self, members, init_genotype_distribution, difficulty, n):
        self._members = members
        self._init_genotype_distribution = init_genotype_distribution
        self._difficulty = difficulty
        self._n = n

        for i in range(n):
            i = Organism()
            i.determine_genotype(self._init_genotype_distribution)
            i.calc_fitness()
            i._age = random.randint(0, i.MAX_AGE / 2)

            print("O [GT] %s [PT] %s | Fitness: %.2f" % (
                i._genotype, i._phenotype, i._fitness))

    def __str__(self):
        result_str = ""
        for i in self._members:
            result_str += "O [GT] %s [PT] %s | Fitness: %.2f | Age: %s \n" % (
                i._genotype, i._phenotype, i._fitness, i._age)
        return result_str

    def check_population(self, difficulty, percent):
        """ Expose a population to an environmental factor. Difficulty is an integer ranging from 0 and up
        so that if an individual's fitness is lower than the difficulty, the individual dies and is removed 
        from the population. Percent specifies what percentage of the population is exposed to the environmental
        factor."""

        # This variable isn't currently needed: n_selected = math.ceil(len(self._members) * percent)
        # Neither is this one: count = 0

        if percent == 1.0:
            for i in self._members:
                if not i.survives_check(difficulty):
                    self._members.remove(i)

    def population_reproduction(self):
        """ All individuals whose reproduction cooldown has expired reproduce. """

        offspring_produced = []
        for i in self._members:
            offspring = i.reproduce()

            if not offspring:
                break

            offspring_produced.append(offspring)
        for thing in offspring_produced:
            self._members.append(thing)

    def tick(self):
        """ Increase age of all organisms and decrease their reproduction cooldown. """

        for i in self._members:
            i._age += 1
            i._reproduction_timer += 1

            if i._age >= Organism.MAX_AGE:
                self._members.remove(i)

    def calc_mean_fitness(self):
        """ Returns mean fitness of the population. """

        n = 0.0

        for i in self._members:
            n += i._fitness

        mean_fitness = n / len(self._members)
        return mean_fitness
