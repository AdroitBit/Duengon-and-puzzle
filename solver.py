from World import *
world=World.load_level(6,strict=True)

player=world.player
player.walk(Direction.left)
player.walk(Direction.up)
world.preview()


print(player.pos)
for o in player.inventories:
    print(o,o.pos)

#print('steppable exit :',world.exit.is_steppable())
#print(player.inventories)