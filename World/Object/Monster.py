from .__init__helper import *


class Monster(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)

        data.setdefault('shape',[1,1])
        data.setdefault('pos',[None,None])
        self.steppable=False
        self.pushable=True
        self.pickable=False

        self.taken_positions=[]
        x,y=data['pos']
        self.shape=data['shape']
        w,h=self.shape
        for ay in range(h):
            for ax in range(w):
                self.taken_positions.append([x+ax,y+ay])
    @property
    def display_prefix(self):
        w,h=self.shape
        if w==h==1:
            return 'm'
        elif w*h>1:
            return 'M'