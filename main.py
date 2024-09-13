from core import *

def uwu(ins, var):
    print(ins, var)

#a = Menu("uwu", 10, 20, "#")
#n = Buttons("owo", 1, 1, "hola", action=uwu)
#a.add_child(n)

my_map = Mapa("UWU", 100, 20, "#")
stu_1 = Structure("uwu", 1, 1, 20, 10, "#")
stu_2 = Structure("owo", 32, 1, 20, 10, "#")

stu_1_1 = Structure("asd", 1, 2, 4, 4, "#")

d = Door("uw", 1, 1, "D", multi=4)
v = Door("uw", 1, 1, "D", multi=4)

stu_1.add_child(d)
stu_1.add_child(stu_1_1)


#stu_1.get_pre_view()
#stu_2.add_child(v)

my_map.add_child(stu_1)
#my_map.add_child(stu_2)


#my_map.get_meta()
my_map.get_pre_view()
#input()
#my_map.del_child(stu_1)
#my_map.get_meta()
#my_map.get_pre_view()