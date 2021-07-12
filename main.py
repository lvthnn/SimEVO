import matplotlib.pyplot as plt

from organism import Organism
from population import Population
    
def main(n = 1000, difficulty = 0.9, mutation_chance = 0.2, checks_per_turn = 2, difficulty_increases = False, difficulty_increase = 0.05):
    # Declare initial variables:
    population = Population([], mutation_chance, difficulty, checks_per_turn, n)
    t = 100

    # Erase everything from database files distribution_before.txt and distribution_after.txt:
    erase = open("charts/distribution_before.txt", "w")
    erase.truncate(0)
    erase.close

    erase = open("charts/distribution_after.txt", "w")
    erase.truncate(0)
    erase.close()


    for individual in population._members:
        f = open("charts/distribution_before.txt", "a")
        f.write("%.4f\n" % individual._fitness)
        f.close()

    t_elapsed = []
    mean_fitness_t = []
    n_population_t = []
    difficulty_t = []

    for i in range(t):
        population.tick()
        population.check_population(difficulty, 1.0)
        print(len(population._members))
        population.population_reproduction()
        print(len(population._members))

        n_population = len(population._members)
        n_population_t.append(n_population)

        mean_fitness = population.calc_mean_fitness()
        mean_fitness_t.append(mean_fitness)

        t_elapsed.append(i)

        # If difficulty_increases and difficulty <= 2.0:
        difficulty_t.append(difficulty)
        if(difficulty_increases):
            difficulty += difficulty_increase



    for individual in population._members:
        f = open("charts/distribution_after.txt", "a+")
        f.write("%.4f\n" % individual._fitness)
        f.close()


    plt.plot(t_elapsed, n_population_t, label = "fjöldi i ∈ P")
    plt.title("Fjöldi")
    plt.ylabel("nₚ")
    plt.xlabel("Δt")
    plt.show()

    plt.plot(t_elapsed, mean_fitness_t, label = "ω avg.")
    plt.plot(t_elapsed, difficulty_t, label = "φ")
    plt.title("Meðalhæfni")
    plt.ylabel("ω")
    plt.xlabel("Δt")
    plt.legend()
    plt.show()

main()
