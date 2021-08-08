from evolution import Evolution
from population import Population

import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as animation

import seaborn as sns
import pandas as pd
import numpy as np
import math


def main():
    print('| EVOLUTION ALGORITHM |--------------------------------')
    DIFFICULTY = float(input('[1/4] (DBL) Enter difficulty : '))
    print('')

    DIFFICULTY_INCREASE = input('[2/4] (Y/N) Increase difficulty? : ')
    DIFFICULTY_INCREMENT = None
    print('')

    if DIFFICULTY_INCREASE.upper() == 'Y':
        DIFFICULTY_INCREMENT = float(input(
            '            Difficulty increment (DBL) : '))
        print('')

    POPULATION_SIZE_INIT = int(input(
        '[3/4] (INT) Enter initial population size : '))
    print('')

    MUTATION_RATIO = float(input('[4/4] Enter mutation ratio : '))

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
        ax1.tick_params(top=False, right=False)
        ax1.grid()

        ax2.plot(t_axis, fitness)
        ax2.set_xlabel('Time elapsed')
        ax2.set_ylabel('Fitness value')
        ax2.tick_params(top=False, right=False)
        ax2.grid()

        if t == 0:
            sns.kdeplot(density, ax=ax3, label='current')
        else:
            sns.kdeplot(density, ax=ax3, label='current')
            sns.kdeplot(density_initial, ax=ax3,
                        color='orange', label='initial')
        ax3.set_xlabel('Fitness value')
        ax3.set_ylabel('Density')
        ax3.set(yticklabels=[])
        ax3.tick_params(left=False, top=False, right=False)
        ax3.legend(loc='upper right')

    # global
    fig = plt.figure(1)
    gridspec = gs.GridSpec(nrows=2, ncols=2)
    # plt.style.use('seaborn-dark')

    t = 0
    t_axis = []
    size = []
    fitness = []
    density = []
    density_initial = []

    population = Population(
        [], MUTATION_RATIO, DIFFICULTY, POPULATION_SIZE_INIT)
    algorithm = Evolution(
        population, DIFFICULTY, DIFFICULTY_INCREASE, DIFFICULTY_INCREMENT, 0.5)

    # set up plots
    ax1 = plt.subplot(gridspec[0, 0:2])
    ax1.set_xlabel('Time elapsed')
    ax1.set_ylabel('Population size')

    ax2 = plt.subplot(gridspec[1, 0])
    ax2.set_xlabel('Time elapsed')
    ax2.set_ylabel('Fitness value')

    ax3 = plt.subplot(gridspec[1, 1])
    ax3.set_xlabel('Fitness value')
    ax3.set_ylabel(None)
    ax3.set(yticklabels=[])

    anim = animation.FuncAnimation(fig, animate, interval=250)
    plt.tight_layout()
    plt.show()
    print('Exited graphing...')


main()
