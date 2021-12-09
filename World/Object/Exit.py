from posixpath import islink
from .__init__helper import *


class Exit(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)
        self.prefix='E'
        
        data.setdefault('pos',[None,None])
        
        self.taken_positions=[data['pos']]
        self.pushable=False
        self.pickable=False
        self.keeper=data['world']
        


    @property
    def display_prefix(self):
        return 'E'

    def is_steppable(self):
        world=self.keeper
        if len(world.monsters_left)==0:
            return True
        else:
            return False