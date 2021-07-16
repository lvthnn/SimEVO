import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import seaborn as sns
import pandas as pd
import numpy as np

from scipy.stats import kde


# read in csv output files of backend
# ...................................

# read in population size over time elapsed


df_size = pd.read_csv('../csv/population_data.csv', sep=',')

time_elapsed = df_size['time_elapsed']
population_size = df_size['population_size']
average_pop_fitness = df_size['population_fitness']

# read in population fitness distribution
df_distribution = pd.read_csv(
    '../csv/fitness_distribution.csv', sep=',', names=(['fitness']))

population_fitness = df_distribution['fitness']

average_fitness = np.mean(population_fitness)

# visualization
fig = plt.figure(1)
gs = gs.GridSpec(nrows=2, ncols=2)


# population size
ax1 = plt.subplot(gs[0, 0:2])
ax1.plot(time_elapsed, population_size, color="#6889ed")
ax1.set_xlabel('Time elapsed')
ax1.set_ylabel('Population size')

# fitness distribution
ax2 = plt.subplot(gs[1, 0])
sns.kdeplot(population_fitness)
ax2.set_xlabel('Fitness value')
ax2.set_ylabel('Density estimate')

# avg fitness as function of time elapsed
ax3 = plt.subplot(gs[1, 1])
ax3.plot(time_elapsed, average_pop_fitness)
ax3.set_xlabel('Time elapsed')
ax3.set_ylabel('Average fitness')

plt.suptitle('Evolutionary Algorithm')
plt.tight_layout()
plt.show()
