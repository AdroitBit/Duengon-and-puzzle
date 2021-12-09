from .__init__helper import *


class Trap(CommonObject):
    def __init__(self,data):
        CommonObject.__init__(self)

        data.setdefault('pos',[None,None])
        self.taken_positions=[data['pos']]

        self.steppable=True
    @property
    def display_prefix(self):
        return 'T'