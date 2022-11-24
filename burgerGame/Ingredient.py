import numpy as np

class Ingredient:
    def __init__(self, spawn_position):
        self.state = 'alive'
        self.position = np.array()
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])