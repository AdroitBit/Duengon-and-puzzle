from .__init__helper import *

class Chair(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)

        data.setdefault('pos',[None,None])
        

        self.taken_positions=[data['pos']]
        self.pushable=True
        self.steppable=True
        
        self.keeper=data['world']
    @property
    def display_prefix(self):
        return 'c'