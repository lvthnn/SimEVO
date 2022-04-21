#!/usr/bin/env python3

# FIXME: Remove BioPython integration
# FIXME: Introduce other representation of genetic language 
import Bio.Seq as bio
import numpy as np, random as rand

import time

# For reproducibility
# rand.seed(18192)

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
        dict_aa[aa] = rand.uniform(-1, 1) 
    return str(dict_aa)

# Activation methods for behavioural net
def sigmoid(x):
    return 1 / (1 + np.exp(-1*x.astype(float)))

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
        layer_mu = []
        weights_output = self._params[2]
        biases_output = self._params[3]

        # Calculations for mu-layer
        for weightset in self._params[0]:
            m = np.dot(weightset, input)
            layer_mu.append(m)

        layer_mu = sigmoid(np.add(layer_mu, self._params[1]))

        # Calculations for output layer
        output = sigmoid(np.add(
            np.dot(layer_mu, weights_output),
            biases_output
        ))

        return output
 
    def calculate_model_params(self):
        # TODO: Takes in amino acid sequence from @param self._aa
        # and uses @param dict_aa to transcribe respective amino acids
        # into weights and biases for model. This has to be done for every 
        # node in the network, a total of 21 times.

        # Nodes in the μ-layer (hidden layer) have the dimensions (146x1)
        # while the o-layer (output layer) has only one node and input dimensions
        # (20x1).

        # Returns a two-item array [P_μ, P_o] with the respective weights and biases 
        # of each layer.

        # P_μ = [w_μ, b_μ] -- Contains weight and bias matrices
        # P_o = [w_o, b_o] -- Contains weight matrices and output bias

        # FIXME: Needs revision and optimisation

        aa_seq = str(self._aa)
        arr_seq = list(aa_seq) 

        translate = []

        for e in arr_seq:
            translate.append(dict_aa[e])


        w_mu = np.array_split(translate[:2880], 20)
        b_mu = translate[2880:2900]
        w_o = translate[2900:2920]
        b_o = translate[2920]

        self._params = [
            np.array(w_mu),
            np.array(b_mu),
            np.array(w_o),
            np.array(b_o)
        ]

if __name__ == '__main__':
    print('Initializing test run...')
    initialize()
    bases = ['A', 'C', 'G', 'T']
    gene_length = 8883
    gene = ''.join(rand.choices(bases, k = gene_length))

    print(dict_aa)

    behaviour_nsx = BehaviourNet(gene)
    behaviour_nsx.calculate_model_params()

    sample_input = np.random.rand(144,)
    behaviour_nsx.feedforward(sample_input)

    # Check for correct dimensions
    print(behaviour_nsx._params[0][0])
    print(np.shape(behaviour_nsx._params[0][1]))

    print(np.shape(behaviour_nsx._params[1][0]))
    print(np.shape(behaviour_nsx._params[1][1]))

    time.sleep(1000)

