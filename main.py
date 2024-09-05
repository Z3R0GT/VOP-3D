from core import *

def uwu(ins, var):
    print(ins, var)

#a = Menu("uwu", 10, 20, "#")
#n = Buttons("owo", 1, 1, "hola", action=uwu)
#a.add_child(n)

m = Mapa("UWU", 100, 20, "#")
#m.get_pre_view()
#m.get_meta()
c = Structure("uwu", 1, 1, 20, 10, "#")

k = Structure("owo", c.vec[0]+c.transform[0]+2, 1, 20, 10, "#")


d = Door("uw", 1, 1, "D", multi=4)
v = Door("uw", 1, 1, "D", multi=4)

c.add_child(d)

k.add_child(v)

m.add_child(c)
m.add_child(k)

m.get_pre_view()