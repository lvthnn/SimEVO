import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as animation

import seaborn as sns
import pandas as pd
import numpy as np


def animate(i):
    with open('../csv/population_data.csv', 'r', newline='') as input:
        population_data = pd.read_csv(
            input, sep=',', encoding='utf-8', names=['time_elapsed', 'population_size', 'average_fitness'])

        time_elapsed = population_data['time_elapsed']
        population_size = population_data['population_size']
        average_fitness = population_data['average_fitness']
    input.close()

    with open('../csv/fitness_distribution.csv', 'r', newline='') as input:
        fitness_data = pd.read_csv(
            input, sep=',', encoding='utf-8', names=['fitness'], dtype={'fitness': np.float16})
    input.close()

    ax1.plot(time_elapsed, population_size, color='#6889ed')
    sns.kdeplot(fitness_data['fitness'])
    ax3.plot(time_elapsed, average_fitness)
    plt.suptitle('Evolutionary Algorithm')


# global
fig = plt.figure(1)
gridspec = gs.GridSpec(nrows=2, ncols=2)


ax1 = plt.subplot(gridspec[0, 0:2])
ax1.set_xlabel('Time elapsed')
ax1.set_ylabel('Population size')


ax2 = plt.subplot(gridspec[1, 0])
ax2.set_xlabel('Fitness value')
ax2.set_ylabel('Density estimate')

ax3 = plt.subplot(gridspec[1, 1])
ax3.set_xlabel('Time elapsed')
ax3.set_ylabel('Average fitness')

anim = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
