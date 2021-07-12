import random

class Organism:
    GT_DOMINANT = "F"
    REPRODUCTION_TIME = 2
    MAX_AGE = 12

    def __init__(self, genotype = "f", phenotype = "", fitness = 0, age = 0, reproduction_timer = 2):
        self._genotype = genotype
        self._phenotype = phenotype
        self._fitness = fitness
        self._age = age
        self._reproduction_timer = reproduction_timer

    def determine_mutation(self, chance):
        if chance >= random.random():
            self._genotype = self.GT_DOMINANT


    def calc_fitness(self):
        if self._genotype == self.GT_DOMINANT:
            self._phenotype = "Dominant"

            if random.random() > 0.05:
                fitness = 1 + random.random()
            else:
                fitness = 1 - random.uniform(0.0, 0.1)
    
        else:
            self._phenotype = "Recessive"

            if random.random() < 0.5: 
                fitness = 0.5 + random.uniform(0.0, 0.3)
            else:
                fitness = 0.5 - random.uniform(0.0, 0.3)

        self._fitness = fitness

    def survives_check(self, difficulty):
        return self._fitness >= difficulty


    def reproduce(self):
        if self._reproduction_timer >= 2:
            self._reproduction_timer = 0

            if random.random() <= 0.001: # beneficial mutation of individual during reproduction
                passed_on_fitness = self._fitness + random.uniform(0, 0.1)
            else:
                passed_on_fitness = self._fitness
            offspring = Organism(self._genotype, self._phenotype, passed_on_fitness, 0, 2)
            return offspring
        return False
