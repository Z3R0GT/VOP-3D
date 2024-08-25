from core import *

#DEBUG_MODE[0] = False

a = Menu("uwu", 10, 12, "$","uwu")
p = Panel("owo", 4, 3, "#" , 5, 5)

btn = Buttons("7w7", 1, 1, "UwU", "hehe", default="BACK")
btn.var = 1

a.add_child(p)
a.add_child(btn)


b = Menu("uwu", 10, 12, "$","uwu")
btn = Buttons("7w7", 1, 1, "not", "hehe", default="MAIN")
b.add_child(btn)

a.start_cast()