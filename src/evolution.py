from population import Population


class Evolution:
    def __init__(self, population, difficulty, difficulty_increase, difficulty_increment, check_percent):
        self._population = population
        self._difficulty = difficulty
        self._difficulty_increase = difficulty_increase
        self._difficulty_increment = difficulty_increment
        self._check_percent = check_percent

    def interval_cycle(self):
        population = self._population
        difficulty = self._difficulty
        percent = self._check_percent

        # Expose part of population to EF
        population.cycle(difficulty, percent)

        # Calculate population variables
        size = len(population._members)
        fitness = population.mean_fitness()
        density = []

        # Create dictionary and return to logger / grapher
        for i in population._members:
            density.append(i._fitness)

        results = {'size': size, 'fitness': fitness, 'density': density}

        # If increase_difficulty == True: increase difficulty.
        if self._difficulty_increase:
            self._difficulty += self._difficulty_increment

        return results
