from .general_complex import *



cur_dir=dirname(__file__)
class World:
    def __init__(world,empty_map,objects,move_limit):
        world.objects=[]
        empty_map=empty_map.split()
        #add_edge first
        empty_map=['W'+xs+'W' for xs in empty_map]
        w=len(empty_map[0])
        empty_map=['W'*w]+empty_map+['W'*w]
       

        #add the plain map object
        for y,xs in enumerate(empty_map):
            for x,o in enumerate(xs):
                #o=o.upper()
                data={'pos':[x,y],'world':world}
                if o=='W':
                    world.objects.append(Wall(data))
                if o=='E':
                    world.objects.append(Exit(data))
                if o=='T':
                    world.objects.append(Trap(data))
                if o=='P':
                    world.objects.append(Player(data))
                if o=='o':#only 1x1 obstacle
                    data['shape']=[1,1]
                    world.objects.append(Obstacle(data))
                if o=='m':#only 1x1 monster
                    data['shape']=[1,1]
                    world.objects.append(Monster(data))
        #add the objects
        for data in objects:
            name=data['name'].lower()
            name=name[0].upper()+name[1:]
            data['world']=world
            if name in all_objects_type():
                world.objects.append(eval(f'{name}')(data))
        world.player.move_limit=move_limit
        

    @staticmethod
    def load_level(lvl,strict=True):
        data=yaml.safe_load(open(cur_dir+f"/worlds/room_{lvl}.yaml"))
        if not strict:
            data['least_moves_count']=99999
        return World(
            data['empty_map'],
            data['objects'],
            data['least_moves_count']
        )
    
    def object_at(world,x,y):
        pos=[x,y]
        world.objects.sort(key=lambda x:[x.is_player()],reverse=True)
        for o in world.objects:
            for taken_pos in o.taken_positions:
                if np.all(taken_pos==pos):
                    return o
        return None
    def objects_at(world,x,y):
        r=[]
        pos=[x,y]
        for o in world.objects:
            for taken_pos in o.taken_positions:
                if np.all(taken_pos==pos):
                    r.append(o)
        return r
    @property
    def shape(world):
        min_x,min_y,max_x,max_y=world.min_max_xy()
        return max_y-min_y+1,max_x-min_x+1
    def min_max_xy(world):
        min_x,min_y,max_x,max_y=999,999,0,0
        for x,y in world.all_taken_positions():
            min_x=min(min_x,x)
            min_y=min(min_y,y)
            max_x=max(max_x,x)
            max_y=max(max_y,y)
        return min_x,min_y,max_x,max_y
    def all_taken_positions(world):
        for o in world.objects:
            for taken_pos in o.taken_positions:
                yield taken_pos.copy()


    def all_gettable_pos(world):
        min_x,min_y,max_x,max_y=world.min_max_xy()
        r=[]
        for y in range(min_y,max_y+1):
            for x in range(min_x,max_x+1):
                yield [x,y]
    def preview(world):
        p=[]
        #min_x,min_y,max_x,max_y=world.min_max_xy()
        h,w=world.shape
        for y in range(h):
            for x in range(w):
                o=world.object_at(x,y)
                if o is None:
                    print('.',end='')
                else:
                    print(o.display_prefix,end='')
            print()
    @property
    def player(self):
        for o in self.objects:
            if isinstance(o,Player):
                return o
    @property
    def monsters_left(self):
        r=[]
        for o in self.objects:
            if isinstance(o,Monster):
                r.append(o)
        return o