#!/usr/bin/env python3
import Bio.Seq as bio
import pprint, time

import numpy as np, random as rand

# For reproducibility
rand.seed(10)

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
    "V",
    "*"
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
# TODO: Implement fitness calculation from translated AA sequence
# TODO: Implement next move function which calculates the next move
# performed by the individual based on NN output
class BehaviourNet:
    def __init__(self, gene):
        self._gene = bio.Seq(gene)
        self._aa = self._gene.translate()
        self._params = []

    def feedforward(self, input):
        # TODO: Implement feed forward into NN which
        # returns integer from [0, 10] which describes
        # action in next round



    def calculate_model_params(self):
        # TODO: Takes in amino acid sequence from @param self._aa
        # and uses @param dict_aa to transcribe respective amino acids
        # into weights and biasesfor model. This has to be done for every node in the
        # network, a total of 21 times.

        # Nodes in the μ-layer (hidden layer) have the dimensions (146x1)
        # while the o-layer (output layer) has only one node and input dimensions
        # (20x1).

        # Returns a two-item array [P_μ, P_o] with the respective weights and biases 
        # of each layer.

        # P_μ = [w_μ, b_μ] -- Contains weight and bias matrices
        # P_o = [w_o, b_o] -- Contains weight matrices and output bias

        # Weight matrix and biases for hidden layer
        w_mu = []
        b_mu = []

        # Weight matrix and bias for output layer
        w_o = []
        b_o = []

        aa_seq = str(self._aa)
        arr_seq = list(aa_seq) 

        count = 0
        for i in arr_seq:
            param_current = dict_aa[i]
            count += 1

            # If we've yet to fill out weights for
            # hidden layer...
            if count <= 2920:
                w_mu.append(param_current)
            elif count >= 2920 and count <= 2940:
                w_o.append(param_current)
            elif count >= 2940 and count <= 2960:
                b_mu.append(param_current)
            elif count == 2961:
                b_o.append(param_current)

                P_mu = [np.array(w_mu), np.array(b_mu)]
                P_o = [np.array(w_o), np.array(b_o)]

                self._params = [P_mu, P_o]

if __name__ == '__main__':
    initialize()
    bases = ['A', 'C', 'G', 'T']
    gene_length = 8883
    gene = ''.join(rand.choices(bases, k = gene_length))

    behaviour_nsx = BehaviourNet(gene)
    behaviour_nsx.calculate_model_params()

    # Check for correct dimensions
    print(np.shape(behaviour_nsx._params[0][0]))
    print(np.shape(behaviour_nsx._params[0][1]))

    print(np.shape(behaviour_nsx._params[1][0]))
    print(np.shape(behaviour_nsx._params[1][1]))

    time.sleep(1000)

