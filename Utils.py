from math import exp

def sigmoid(x, a=1):
    return 1/(1 + exp(-a*x))

def remap(x, min_x, max_x, min_y, max_y):
    '''Maps x, which ranges from `min_x` to `max_x`,
    to a new number which can range from `min_y` to 
    `max_y`.
    '''
    min_x = (min_x if min_x <= max_x else max_x)
    max_x = (max_x if max_x >= min_x else min_x)

    min_y = (min_y if min_y <= max_y else max_y)
    max_y = (max_y if max_y >= min_y else min_y)

    return min_y + (max_y - min_y) * ((x - min_x) / (max_x - min_x))