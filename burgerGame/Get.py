import numpy as np

class Get:
    def __init__(self,position, command):
        self.speed = 10
        self.position = np.array([position[0]-3, position[1]-3, position[0]+3, position[1]+3])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.state = None
        if command['up_pressed']:
            self.direction['up'] = True
        if command['dowm_pressed']:
            self.direction['down'] = True
        if command['right_pressed']:
            self.direction['right'] = True
        if command['left_pressed']:
            self.direction['left'] = True

    def move(self):
        if self.direction['up']:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        if self.direction['down']:
            self.position[1] += self.speed
            self.position[3] += self.speed

        if self.direction['left']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            
        if self.direction['right']:
            self.position[0] += self.speed
            self.position[2] += self.speed

    def get_check(self, ingredients):
        for 