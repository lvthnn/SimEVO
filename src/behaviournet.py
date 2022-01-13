#!/usr/bin/env python3
from Bio.Seq import Seq

import numpy as np, random as rand
# from keras.layers.core import Dense, Activation
# from keras.models import Sequential
# from keras.layers import Layer

# For reproducibility
np.random.seed = 100

# Contains single-letter amino acid abbreviations
amino_acids = [
    "A",
    "R",
    "N",
    "D",
    "B",
    "C",
    "E",
    "Q",
    "Z",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V"
]

# We use this to store the returned weight
# keyed by each amino acid
dict_aa = {}

# Initializes amino acid weight table
def initialize():
    for aa in amino_acids:
        dict_aa[aa] = rand.uniform(-1,1) 
    return str(dict_aa)

# This class stores each individual's "nervous system"
# TODO: Implement fitnes calculation from translated AA sequence
# TODO: Implement next move function which calculates the next move
# performed by the individual based on NN output
class BehaviourNet:
    def __init__(self, gene):
        self._gene = Seq(gene)
        self._aa = self._gene.translate()
