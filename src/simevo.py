import pygame, random as rand, os

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SimEvo')

# Denotes dimensions of
# surface (X = nx, Y = ny)
nx = 200
ny = 200

# Base genetics
gene_length = 20
gene_base = 20 * 'A'

# Color of individuals in Pygame display
ind_color = (150, 150, 150)
food_color = (25, 198, 43)

# Initial population
pop_size_init = 100
population = []
for i in range(pop_size_init):
    x = rand.randrange(0, width)
    y = rand.randrange(0, height)
    
    population.append([x, y, gene_base])

# Simulation metrics
time_elapsed = 0

# Individual moveset


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # Draw population to screen
    for i in range(len(population)):
        pygame.draw.rect(screen, ind_color, (population[i][0], population[i][1], 1, 1))

    pygame.display.update()

    # Caveman solution to print data to console, remove later
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Time: {time}".format(time = time_elapsed))

    time_elapsed += 1

def move(ind, mv):
    print("Hello world!")

pygame.quit()
