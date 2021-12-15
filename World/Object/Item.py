from .__init__helper import *

from .Player import *

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

    def __repr__(self) -> str:
        return f'{self.type}'

    def get_picked_up(self,by):
        picker=byasdasd
        picker.inventories.append(self)
        self.holder=picker
    @property
    def pos(self):
        if isinstance(self.holder,Player):
            self.taken_positions[0]=self.holder.pos.copy()
        return self.taken_positions[0]