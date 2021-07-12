from organism import Organism
import random
import math

class Population:

    def __init__(self, members, mutation_chance, difficulty, c_per_t, n):
        self._members = members
        self._mutation_chance = mutation_chance
        self._difficulty = difficulty
        self._c_per_t = c_per_t # checks per unit of time, t
        self._n = n

        for i in range(n):
            new_organism = Organism()
            new_organism.determine_mutation(self._mutation_chance)
            new_organism.calc_fitness()
            new_organism._age = random.randint(0, new_organism.MAX_AGE / 2)

            print("O [GT] %s [PT] %s | Fitness: %.2f" % (new_organism._genotype, new_organism._phenotype, new_organism._fitness))
            self._members.append(new_organism)
            
    def __str__(self):
        result_str = ""
        for organism in self._members:
            result_str += "O [GT] %s [PT] %s | Fitness: %.2f | Age: %s \n" % (organism._genotype, organism._phenotype, organism._fitness, organism._age)
        return result_str
    
    def check_population(self, difficulty, percent):
        n_selected = math.ceil(len(self._members) * percent)
        count = 0

        if percent == 1.0:
            for organism in self._members:
                if not organism.survives_check(difficulty):
                    self._members.remove(organism)

    def population_reproduction(self):
        offspring_produced = []
        for organism in self._members:
            offspring = organism.reproduce()

            if not offspring:
                break

            offspring_produced.append(offspring)
        for thing in offspring_produced:
            self._members.append(thing)


    def tick(self):
        for organism in self._members:
            organism._age += 1
            organism._reproduction_timer += 1
            if organism._age >= organism.MAX_AGE:
                self._members.remove(organism)


    def calc_mean_fitness(self):
        total_fitness = 0.0
       
        for organism in self._members:
            total_fitness += organism._fitness
       
        mean_fitness = total_fitness / len(self._members)
        return mean_fitness