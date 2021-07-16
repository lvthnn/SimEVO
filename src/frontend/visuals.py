import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as animation

import seaborn as sns
import pandas as pd
import numpy as np

from scipy.stats import kde

# global
fig = plt.figure(1)
gridspec = gs.GridSpec(nrows=2, ncols=2)

# animate function


def animate(i):

    # read in csv output files of backend
    # ...................................

    # read in population size over time elapsed
    with open('../csv/population_data.csv') as input:
        df_size = pd.read_csv(input, sep=',', encoding='utf-8', header=1)

    input.close()

    time_elapsed = df_size['time_elapsed']
    population_size = df_size['population_size']
    average_pop_fitness = df_size['population_fitness']

    # read in population fitness distribution
    with open('../csv/fitness_distribution.csv') as input:
        df_distribution = pd.read_csv(
            input, sep=',', names=(['fitness']), encoding='utf-8')

    input.close()

    population_fitness = df_distribution['fitness']

    # population size
    ax1 = plt.subplot(gridspec[0, 0:2])
    ax1.plot(time_elapsed, population_size, color="#6889ed")
    ax1.set_xlabel('Time elapsed')
    ax1.set_ylabel('Population size')

    # fitness distribution
    ax2 = plt.subplot(gridspec[1, 0])
    print(population_fitness)
    sns.kdeplot(population_fitness)
    ax2.set_xlabel('Fitness value')
    ax2.set_ylabel('Density estimate')

    # avg fitness as function of time elapsed
    ax3 = plt.subplot(gridspec[1, 1])
    ax3.plot(time_elapsed, average_pop_fitness)
    ax3.set_xlabel('Time elapsed')
    ax3.set_ylabel('Average fitness')

    plt.suptitle('Evolutionary Algorithm')
    plt.pause(10)

    ax1.cla()
    ax2.cla()
    ax3.cla()


anim = animation.FuncAnimation(fig, animate, interval=250)

plt.tight_layout()
plt.show()
