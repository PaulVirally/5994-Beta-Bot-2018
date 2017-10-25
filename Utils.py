from math import exp
import numpy as np
import pickle

def sigmoid(x, a=1):
    return 1/(1 + exp(-a*x))

def remap(x, min_x, max_x, min_y, max_y):
    '''Maps x, which ranges from `min_x` to `max_x`,
    to a new number which can range from `min_y` to 
    `max_y`.
    '''
    return min_y + (max_y - min_y) * ((x - min_x) / (max_x - min_x))

class Net:
    def __init__(self, topology, alpha=1):

        self.topology = topology
        self.num_synapses = len(self.topology)-1
        self.num_layers = self.num_synapses + 1
        self.alpha = alpha

        self.synapses = []
        for i in range(self.num_synapses):
            self.synapses.append((2*np.random.rand(topology[i], topology[i+1]))-1)

        self.layers = []
        self.layer_errors = []
        self.layer_deltas = []

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoid_prime(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def feedforward(self, inpt):

        # Reset
        self.layers = []

        # Fill in data
        self.layers.append(inpt)
        for i in range(self.num_layers-1): # -1 because we already did the first layer
            self.layers.append(self.sigmoid(np.dot(self.layers[i], self.synapses[i])))

        return self.layers[-1]

    def train(self, inpt, outpt, print_error=False):

        # Feed forward
        self.feedforward(inpt)

        # Reset
        self.layer_errors = []
        self.layer_deltas = []

        self.layer_errors.append(self.layers[-1] - outpt)
        self.layer_deltas.append(self.layer_errors[-1] * self.sigmoid_prime(self.layers[-1]))

        if print_error:
            print("Error: {0}".format(str(np.mean(np.abs(self.layer_errors[-1])))))

        for i in range(self.num_layers - 1): # -1 because we already did the first layer
            self.layer_errors.append(self.layer_deltas[-1].dot(self.synapses[(-1*i)-1].T))
            self.layer_deltas.append(self.layer_errors[-1] * self.sigmoid_prime(self.layers[(-1*i)-2]))

        for i in range(self.num_synapses):
            self.synapses[(-1*i)-1] -= self.alpha * self.layers[(-1*i)-2].T.dot(self.layer_deltas[i])

    def save_state(self, file_path):

        with open(file_path, 'wb') as outfile:
            pickle.dump(self.synapses, outfile)

    def read_state(self, file_path):

        with open(file_path, 'rb') as infile:
            self.synapses = pickle.load(infile)