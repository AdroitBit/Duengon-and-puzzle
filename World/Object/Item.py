from .__init__helper import *

class Item(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)
        
        data.setdefault('type','')
        data.setdefault('pos',[None,None])
        self.pickable=True
        self.pushable=True
        self.steppable=True

        
        self.type=data['type']
        self.taken_positions=[data['pos']]
        self.holder=data['world']

    @property
    def display_prefix(self):
        return self.type[0].upper()