from World import *
world=World.load_level(5,strict=True)

player=world.player
world.preview()
print(player.is_dead())