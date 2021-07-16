from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas as pd
import csv


def animate(i):
    df = pd.read_csv('csv/data_plot.csv')
    time_elapsed = df['time_elapsed']
    population_size = df['population_size']

    plt.cla()
    plt.plot(time_elapsed, population_size)


ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
