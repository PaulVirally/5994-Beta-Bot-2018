from math import exp

def sigmoid(x):
    return 1/(1 + exp(-x))

def remap(x, min_x, max_x, min_y, max_y):
    '''Maps x, which ranges from `min_x` to `max_x`,
    to a new number which can range from `min_y` to 
    `max_y`.
    '''
    return min_y + (max_y - min_y) * ((x - min_x) / (max_x - min_x))