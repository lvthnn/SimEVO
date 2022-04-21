# Estimations of runtime using simulation
# See notes for details and derivation
import csv
import random


def simulate(n, C):
    container = []
    sizes = []
    for i in range(C):
        container.append([])

    for i in range(n):
        temp = random.randint(0, C - 1)
        container[temp].append(i)

    for i in range(C):
        sizes.append(len(container[i]))

    max_load = max(sizes)
    row = [max_load, n, C]

    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def main():
    for n in range(1, 101):
        for C in range(1,101):
            simulate(n,C)

main()
