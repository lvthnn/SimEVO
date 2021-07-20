from evolution import Evolution
from population import Population

import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as animation

import seaborn as sns
import pandas as pd
import numpy as np


def main():
    GLOBAL_DIFFICULTY_PARAM = 0.55

    def animate(i):
        results = algorithm.interval_cycle()
        nonlocal t, t_axis, size, fitness, density, density_initial

        if t == 0:
            density_initial = results['density']

        fitness.append(results['fitness'])
        size.append(results['size'])
        density = results['density']
        t_axis.append(t)
        t += 1

        ax1.cla()
        ax2.cla()
        ax3.cla()

        ax1.plot(t_axis, size)
        ax1.set_xlabel('Time elapsed')
        ax1.set_ylabel('Population size')

        ax2.plot(t_axis, fitness)
        ax2.set_xlabel('Time elapsed')
        ax2.set_ylabel('Fitness value')

        if t == 0:
            sns.kdeplot(density, ax=ax3)
        else:
            sns.kdeplot(density, ax=ax3)
            sns.kdeplot(density_initial, ax=ax3, color='orange')
        ax3.set_xlabel('Fitness value')
        ax3.set_ylabel('Density estimate')

        plt.suptitle('Evolutionary Algorithm')

    # global
    fig = plt.figure(1)
    gridspec = gs.GridSpec(nrows=2, ncols=2)
    plt.style.use('seaborn-dark')

    t = 0
    t_axis = []
    size = []
    fitness = []
    density = []
    density_initial = []

    population = Population([], 0.1, GLOBAL_DIFFICULTY_PARAM, 1000)
    algorithm = Evolution(
        population, GLOBAL_DIFFICULTY_PARAM, False, None, 0.2)

    # set up plots
    ax1 = plt.subplot(gridspec[0, 0:2])
    ax1.set_xlabel('Time elapsed')
    ax1.set_ylabel('Population size')

    ax2 = plt.subplot(gridspec[1, 0])
    ax2.set_xlabel('Time elapsed')
    ax2.set_ylabel('Fitness value')

    ax3 = plt.subplot(gridspec[1, 1])
    ax3.set_xlabel('Fitness value')
    ax3.set_ylabel('Density estimate')

    anim = animation.FuncAnimation(fig, animate, interval=250)
    plt.show()


main()
