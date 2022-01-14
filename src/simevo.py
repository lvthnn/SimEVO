#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
#
#
#       Kári Hlynsson, 2021-2022.
#       Feel free to use! :)
#       
#       For more info on how this script works and what it aims
#       to demonstrate, checkout the README.md as well as my blog 
#       post!
#
#       https://github.com/lvthnn/SimEVO
#
#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

#!/usr/bin/env python3
import pygame, random as rand, math, time, numpy as np, os

import behaviournet
from behaviournet import BehaviourNet

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
# 
#   globals
#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

# Pygame setup
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Evolutionary simulation')

# Base genetics
bases = ['A', 'T', 'C', 'G']
gene_length = 8763
aa_weights = behaviournet.initialize()

# Food color in Pygame
food_color = (0, 255, 0)
ind_color = (0, 0, 0)

# Stores all entities, allows for faster searches based
# on (x,y) coordinate
entity_field = np.empty(size, dtype = int)

# Population metrics 
pop_size_init = 100
population = []
mutation_rate = 0.05
individual_energy = 400
generation_time = 1200

# Simulation metrics
time_elapsed = 0
generation_count = 1
simulation_time = []
environmental_difficulty = 8
num_food = math.ceil(environmental_difficulty * pop_size_init) 

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
# 
#   operation sets 
#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

# 3x3 square for movement 
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

# 7x7 square for scanning surroundings 
scanset = [
    # Right
    [1,0],
    [2,0],
    [3,0],
    # Left
    [-1,0],
    [-2,0],
    [-3,0],
    # Up
    [0,1],
    [0,2],
    [0,3],
    # Down
    [0,-1],
    [0,-2],
    [0,-3],
    # RUDiagonal
    [1,1],
    [2,2],
    [3,3],
    #RDDiagonal
    [1,-1],
    [2,-2],
    [3,-3],
    # LDDiagonal
    [-1,-1],
    [-2,-2],
    [-3,-3],
    #LUDiagonal
    [-1,1],
    [-2,2],
    [-3,3],
    # LWing-I
    [1,2],
    [1,3],
    [2,3],
    # RWing-I
    [2,1],
    [3,1],
    [3,2],
    # LWing-II
    [-2,1],
    [-3,1],
    [-3,2],
    # RWing-II
    [-1,2],
    [-1,3],
    [-2,3],
    # LWing-III
    [-2,-1],
    [-3,-1],
    [-3,-2],
    # RWing-III
    [-1,-2],
    [-1,-3],
    [-2,-3],
    # LWing-IV
    [1,-2],
    [1,-3],
    [2,-3],
    # RWing-IV
    [2,-1],
    [3,-1],
    [3,-2]
]

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
# 
#   entity and entity_field setup 
#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

food = []

for i in range(pop_size_init):
    x = rand.randrange(0, width)
    y = rand.randrange(0, height)
    age = 0

    gene = ''.join(rand.choices(bases, k = gene_length))

    nsx = BehaviourNet(gene) # nsx = nervous system
    nsx.calculate_model_params()

    population.append([x, y, gene, age, individual_energy, nsx])
    entity_field[x][y] = 2


for i in range(num_food):
    x = rand.randrange(width)
    y = rand.randrange(height)

    food.append([x,y])
    entity_field[x][y] = 1

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
# 
#   individual methods 
#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

# Individual operations
def move(individual, movekey):
    x = individual[0]
    y = individual[1]
    movement = moveset[movekey]

    newx = x + movement[0]
    newy = y + movement[1]

    individual[0] = newx
    individual[1] = newy

def scan_surroundings(individual):
    x = individual[0]
    y = individual[1]

    scan_result = []


    for scan in scanset:
        scanx = x + scan[0]
        scany = y + scan[1]
        
        if entity_field[scanx - 1][scany - 1] != 0:
            print('Hello')

        # for individual in population:
            # if individual[0] == scanx and individual[1] == scany:
                # replacement = scan_result.index([scan[0], scan[1], 0])
                # scan_result[replacement][2] == 1

        # for f in food:
            # if f[0] == scanx and f[1] == scany:
                # replacement = scan_result.index([scan[0], scan[1], 0])
                # scan_result[replacement][2] == 2

                # if abs(f[0] - x) <= 1 and abs(f[1] - y) <= 1:
                    # ind[4] = individual_energy
                    # food.remove(f)

        return np.array(scan_result, dtype = object).flatten()

def perform_action(ind, actionID):
    # TODO: Abstraction we use to simplify code.
    # Takes in integer input from individual nsx object
    # and performs the appropriate action 

    if actionID <= 7:
        move(ind, actionID)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
# 
#   main loop 
#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

if __name__  == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        # Get time at the start of simulation iteration
        startTime = time.time()
        screen.fill((80, 80, 80))

        for individual in population:
            pygame.draw.rect(screen, ind_color, (individual[0], individual[1], 2, 2))
           
            # TODO: Organism acts based on input from neural network
            # feedback. Formatted as integer ranging from [0,7].
            surroundings = scan_surroundings(individual)
            response = individual[5].feedforward(surroundings)
            
            action = round(7 * response)
            perform_action(individual, action)

            individual[4] -= 1
            if individual[4] == 0:
                population.remove(individual)

        for i in range(len(food)):
            pygame.draw.rect(screen, food_color, (food[i][0], food[i][1], 2, 2))


        pygame.display.update()
        
        # Append total time to array
        simulation_time.append(time.time() - startTime)
        meanTime = np.mean(simulation_time)

        # Caveman solution to print data to console, remove later
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print('Time: {time}\nGeneration: {generation}\nAverage iteration time: {avgtime}'.format(
            # time = time_elapsed, 
            # generation = generation_count, 
            # avgtime = meanTime
        # ))

        time_elapsed += 1
