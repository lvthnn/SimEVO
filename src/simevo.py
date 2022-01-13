#!/usr/bin/env python3
import pygame, random as rand, os, math, time, numpy as np
from colorhash import ColorHash

# Pygame setup
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SimEvo')

# Base genetics
bases = ['A', 'T', 'C', 'G']
gene_length = 4790

# Food color in Pygame
food_color = (255, 255, 255)

# Population metrics 
pop_size_init = 100
population = []
mutation_rate = 0.05

individual_max_age = 10000
individual_energy = 100

for i in range(pop_size_init):
    x = rand.randrange(0, width)
    y = rand.randrange(0, height)
    age = 0

    gene = "".join(rand.choices(bases, k = gene_length))

    population.append([x, y, gene, age, individual_energy])

# Simulation metrics
time_elapsed = 0
generation_count = 1
simulation_time = []

# Represents ratio of food presents and population size
environmental_difficulty = 0.5
num_food = math.ceil(environmental_difficulty * pop_size_init) 
food = []

for i in range(num_food):
    x = rand.randrange(width)
    y = rand.randrange(height)
    food.append([x,y])

# Individual moveset
moveset = [
 [0,1],
 [1,0],
 [1,1],
 [0,-1],
 [-1,0],
 [-1,-1],
 [1,-1],
 [-1,1]
]

# 3x3 ellipse used for scanning surroundings
scanset = [
 [0,1],
 [0,2],
 [0,3],
 [0,-1],
 [0,-2],
 [0,-3],
 [1,0],
 [2,0],
 [3,0],
 [-1,0],
 [-2,0],
 [-3,0],
 [1,1],
 [2,2],
 [-1,-1],
 [-2,-2],
 [2,1],
 [3,1],
 [1,2],
 [1,3],
 [-2,1],
 [-3,1],
 [-1,2],
 [-1,3],
 [-2,-1],
 [-3,-1],
 [-1,-2],
 [-1,-3],
 [2,-1],
 [3,-1],
 [1,-2],
 [1,-3]
]

# Individual operations
def move(individual, movekey):
    x = individual[0]
    y = individual[1]
    movement = moveset[movekey]

    newx = x + movement[0]
    newy = y + movement[1]

    individual[0] = newx
    individual[1] = newy

def eat(individual, food):
    # TODO: Individual needs to have same (x,y) coordinate as food
    # in order to eat food
    print('yo')

def scan_surroundings(ind):
    x = ind[0]
    y = ind[1]

    # Scan results are either 1 (individual) or 2 (food)
    # with relative positions
    scan_result = []

    for scan in scanset:
        scanx = x + scan[0]
        scany = y + scan[1]
       
        for i in range(len(population)):
            if population[i][0] == scanx and population[i][1] == scany:
                scan_result.append([population[i], 1])

        for i in range(len(food)):
            if food[i][0] == scanx and food[i][1] == scany:
                scan_result.append([food[i], 2])

    return scan_result

def reproduce(ind):
    # TODO: Implement asexual reproduction
    # One individual becomes two, with a slight
    # chance of mutation as indicated by the
    # variable mutation_rate
    print('Yo')
        

if __name__  == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        # Get time at the start of simulation iteration
        startTime = time.time()

        screen.fill((0,0,0))

        for i in range(len(population)):
            ind_color = ColorHash(population[i][2])
            pygame.draw.rect(screen, ind_color.rgb, (population[i][0], population[i][1], 1, 1))
            
            # Random movement, requires implementation
            move(population[i], rand.randrange(0,7))
            
            population[i][3] += 1
            population[i][4] -= 1

            # if population[i][4] == 0 or population[i][3] >= individual_max_age:
                # population.remove(population[i])

        for i in range(len(food)):
            pygame.draw.rect(screen, food_color, (food[i][0], food[i][1], 1, 1))


        pygame.display.update()

        # Append total time to array
        simulation_time.append(time.time() - startTime)
        meanTime = np.mean(simulation_time)

        # Caveman solution to print data to console, remove later
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Time: {time}\nGeneration: {generation}\nAverage iteration time: {avgtime}'.format(time = time_elapsed, generation = generation_count, avgtime = meanTime))

        time_elapsed += 1

