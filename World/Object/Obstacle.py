from .__init__helper import *

class Obstacle(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)

        data.setdefault('shape',[0,0])
        data.setdefault('pos',[None,None])
        
        self.taken_positions=[]
        x,y=data['pos']
        self.shape=data['shape']
        w,h=self.shape
        for ay in range(h):
            for ax in range(w):
                self.taken_positions.append([x+ax,y+ay])
    @property
    def display_prefix(self):
        return 'o'