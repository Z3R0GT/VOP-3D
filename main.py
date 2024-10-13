from core.models import *
from core.game import *

#DEBUG_MODE[0] = False

player = User("uwu", "X", 4, 3)
player.setup_configs(["i", "t"], [inventory, config])

house = Structure("stu", chr="&", x=1, y=4, sz_x=10, sz_y=10)
house.generate_lines("-Y", Y_CORD=[2, 5], X_CORD=[1, 6])
house.del_geometry(ID=[1])

door = Door("uwu", x=2, y=0, chr="M", multi=4)
house.add_child(door)
door = Door("mom", 9, 2, "M", pos=False, multi=4)
house.add_child(door)

scene = Mapa("ma", "#", x=30, y=15)

sword_1 = Sword("Legendary Mile Sword", 16, 3)
sword_2 = sword_1.copy("Epic Mile Sword", 1, 3)

scene.add_child(sword_1)
scene.add_child(sword_2)

cam = Camera("main", zone=scene, look=player, static=False)

scene.add_child(node=house)
scene.add_child(node=player)

start_game_2d()