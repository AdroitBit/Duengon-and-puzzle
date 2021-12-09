#all object will import this might fix some warning and stuff
import numpy as np




class MovementType:
    walk='go'
    sword='sword'
    bow='shoot'
    glove='drag'
    shield='push'
class Direction:
    left='left'
    right='right'
    down='down'
    up='up'
def direction_2_vector(d):
    return {
        Direction.left:[-1,0],
        Direction.right:[1,0],
        Direction.down:[0,1],
        Direction.up:[0,-1]
    }[d]

class CommonObject:
    def __init__(self):
        self.steppable=False
        self.pickable=False
        self.pushable=False

    def is_steppable(self):
        return self.steppable
    def is_not_steppable(self):
        return not self.steppable
    def is_pushable(self):
        return self.pushable
    def is_not_pushable(self):
        return not self.pushable
    def is_pickable(self):
        return self.pickable
    def is_not_pickable(self):
        return not self.pickable

    def is_player(self):
        return self.display_prefix=='P'