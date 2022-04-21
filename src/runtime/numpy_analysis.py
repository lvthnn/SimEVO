import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('data.csv', index_col = False)
    print(data)

    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')

    ax.plot_trisurf(data["n"], data["C"], data["max_load"])
    ax.set_xlabel('Population Size')
    ax.set_ylabel('Number of Chunks')
    ax.set_zlabel('Maximum Chunk Load')
    plt.show()

    plt.savefig('mcl_simulation.png', bbox_inches ='tight')



