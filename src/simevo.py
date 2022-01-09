import pygame, random as rand, os, math

# Pygame setup
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SimEvo')

# Base genetics
bases = ['A', 'T', 'C', 'G']
gene_length = 20

# Color of individuals in Pygame display
ind_color = (150, 150, 150)
food_color = (25, 198, 43)

# Population metrics 
pop_size_init = 100
population = []
mutation_rate = 0.05
individual_max_age = 50

for i in range(pop_size_init):
    x = rand.randrange(0, width)
    y = rand.randrange(0, height)
    age = 0

    gene = "".join(rand.choices(bases, k = gene_length))

    population.append([x, y, gene, age])

# Simulation metrics
time_elapsed = 0

# Represents ratio of food presents and population size
environmental_difficulty = 0.5
num_food = math.ceil(environmental_difficulty * pop_size_init) 
food = []

# Individual moveset
moveset = [
 [0,1],
 [1,0],
 [1,1],
 [0,-1],
 [-1,-1],
 [-1,0],
 [1,-1],
 [-1,1]
]

def move(individual, movekey):
    x = individual[0]
    y = individual[1]
    movement = moveset[movekey]

    newx = x + movement[0]
    newy = y + movement[1]

    individual[0] = newx
    individual[1] = newy

def eat(individual, food):
    # ...
    print('yo')

if __name__  == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        screen.fill((0,0,0))

        # Draw population to screen
        for i in range(len(population)):
            pygame.draw.rect(screen, ind_color, (population[i][0], population[i][1], 1, 1))
            move(population[i], rand.randrange(0,7)) # Issues move order to population

        for i in range(num_food):
            x = rand.randrange(width)
            y = rand.randrange(height)

            pygame.draw.rect(screen, food_color, (x, y, 1, 1))
            food.append([x,y])
            

        pygame.display.update()

        # Caveman solution to print data to console, remove later
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Time: {time}'.format(time = time_elapsed))

        time_elapsed += 1

    pygame.quit()
