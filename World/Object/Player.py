from .__init__helper import *
#clear warning from pylance
from .Exit import *
from .Trap import *
from .Chair import *
from .Monster import *

class Player(CommonObject):
    def __init__(self,data,move_limit=999):
        CommonObject.__init__(self)
        
        data.setdefault('pos',[None,None])
        self.taken_positions=np.array([data['pos']])
        self.move_count=0
        self.move_limit=data['least_moves_count']
        self.dead=False
        self.world=data['world']
        self.inventories=[]
    @property
    def pos(self):
        return self.taken_positions[0]
    @pos.setter
    def pos(self,p):
        self.taken_positions[0]=p
    def is_dead(self):
        c1=self.dead
        c2=self.move_count>self.move_limit
        c3=self.move_count==self.move_limit and not isinstance(self.stepping_on(),Exit)
        c4=isinstance(self.stepping_on(),Trap)
        self.dead=c1 or c2 or c3 or c4
        return self.dead
    @property
    def display_prefix(self):
        return 'P'
    def perform(self,t,d):#type,direction
        if self.is_dead():
            return

        if t==MovementType.sword:
            self.walk(d)
        if t==MovementType.bow:
            self.shoot(d)
        if t==MovementType.glove:
            self.drag(d)
        if t==MovementType.shield:
            self.push(d)
    def object_at(self,d):
        p=self.pos.copy()
        p=p+direction_2_vector(d)
        return self.world.object_at(*p)
    def stepping_on(self):
        o=self.world.objects_at(*self.pos).copy()
        o.remove(self)
        if len(o)==0:
            return None
        else:
            return o
    def pick(self,o):
        world=o.holder
        o.get_picked_up(by=self)
        o.holder=self
        self.inventories.append(o)
        world.objects.remove(o)
    def pick_at(self,x,y):
        world=self.world
        objects=world.objects_at(x,y)
        objects.remove(self)#exclude player
        for o in objects:
            o.get_picked_up(by=self)#already apply to inventory and stuff
    def walk(self,d):
        if self.is_dead():
            return
        p0=self.pos.copy()
        world=self.world

        while True:
            o=self.object_at(d)
            if o is not None and o.is_not_steppable():
                break
            elif o is not None and o.is_steppable():
                self.pos=self.pos+direction_2_vector(d)
                if isinstance(o,Trap):
                    self.dead=True
                elif o.is_pickable():#damn we have to be able to pick multiple item there.
                    self.pick_at(*o.pos)
                elif isinstance(o,Chair):
                    break
                break
            else:
                self.pos=self.pos+direction_2_vector(d)
                
        if np.any(self.pos!=p0):
            self.move_count+=1
    def use_sword(self,d):
        p=self.pos+direction_2_vector(d)
        world=self.world
        
        o=self.object_at(d)
        if o is not None and isinstance(o,Monster):
            world.objects.remove(o)
            o.keeper=None
        else:
            raise SystemError(f"Nothing in the {d} direction")

        self.move_count+=1
    def have_bow(self):
        for item in self.inventories:
            if item.type=='bow':
                return True
        return False
    def have_arrow(self):
        for item in self.inventories:
            if item.type=='arrow':
                return True
        return False
    def use_bow(self,d):
        if not self.have_bow():
            raise SystemError("Player doesn't have bow")
        if not self.have_arrow():
            raise SystemError("Player doesn't have arrow")
        

    def __repr__(self):
        return 'player'