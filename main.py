from core import *

DEBUG_MODE[0] = False

a = Menu("uwu", 10, 12, "$","uwu")
btn = Buttons("7w7", 1, 1, "UwU", "hehe", default="BACK")
a.add_child(btn)

p = Panel("owo", 0, 2, "#" , 10, 10)
p.get_meta()