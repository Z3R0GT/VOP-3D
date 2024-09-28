from types import EllipsisType

from core.models.base.tools.maths import insert
from core.models.data.d2.env import PAUSING, PLAYING

from ....base.constant.BasisMover import *

#NOTE: esta clase tiene por objetivo actuar como intermediario para aquellos nodos
# que se muevan por el mapa/escenario actual, puedes considerarlo como la parte "backend"
# de todo, ya que solo recibe datos y envia datos 

#TODO: _num_in_rng y _inter necesitan ser simplificados
def _num_in_rng(vector:list[int, int], rgns:list[range], inver:bool)->bool:
    if inver:
        return vector[0] in rgns[0] or vector[1] in rgns[1]
    else:
        return vector[0] in rgns[0] and vector[1] in rgns[1]

def _inter(focus:list[int, int], scene, components:list[str], inver:bool=False)->list[bool, Vector|EllipsisType]:
    for node in scene.chunks:
        node:str
        re = _num_in_rng(focus, 
                         scene.chunks[node], 
                         inver)
        if re:
            n = node.split("_")
            if n[1] in components:
                i = int(n[2])
                return [re, scene.child_lst[i]]
    return [re, ...]

class Skeleton(BasisMover):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, 
                 id: int, abs: str, *,
                 components: list[str] = ..., 
                 comment: str | None = None) -> None:
        super().__init__(name, chr, x, y, id, abs, components, comment)
        super().__coords__()
        super().__caster__()
        self.exept:str = ""
        self.bef = ["", ""]
        self.input = (self.in_x, self.in_y)
    
    #NOTE: estas funciones puede ser sobre escrita... no hace falta documentar
    def mover(self, key:str):
        key = key.lower()
        self.__caster__()
        w, s, a, d = self.controll
        
        match key:
            case n if n == w:
                self.in_y = -1
            case n if n == s:
                self.in_y = 1
            case n if n == a:
                self.in_x = -1
            case n if n == d:
                self.in_x = 1
        
        #TODO: requiere de hacer un caso donde se presionen dos botones al mismo tiempo
        # (y solo dos)
        self.input = (self.in_x, self.in_y)
        #TODO: aqui se tienen que agregar las condiciones necesarias para el movimiento
        self.move_to()
        
    def adder(node):...
        
    def move_to(self):
        mapper:Vector| BasisTreeNode = self.father[0]
        
        tmp_x = self.global_x+self.input[0]
        tmp_y = self.global_y+self.input[1]
        glob = [self.global_x, self.global_y]
        
        try:
            checker(line=[tmp_x, tmp_y], limit=mapper.vec, vector=2)
        except (CoordNotFound, CoordExced):
            return
        chr_nxt:str = mapper.square[tmp_y][tmp_x]
        
        #solo evalua en caso este cerca a algo
        if 0 in mapper.next_to(self):
            #evalua el componente
            node = _inter([tmp_x, tmp_y], mapper, ["stu", "obj"])
            if node[0]:
                
                #TODO: requiere se extrapolar a una función para mayor 
                # comodidad al operar (el retorno tiene que un BasisNode/Node)
                match node[1].abs:
                    case "stu":
                        self.exept = node[1].character
                        if chr_nxt == self.exept:
                            return
                        
                        #en caso el objeto stu tenga también un obj
                        dor = _inter(glob, node[1], ["dor", "obj"], True)
                        #¿X?
                        if not dor[0] and chr_nxt == self.bef[1]:
                            tmp_x+=self.input[0]
                            tmp_y+=self.input[1]
                            chr_nxt = " "
                        #¿Y?
                        elif dor[0] and chr_nxt == dor[1].character:
                            self.bef[0] = dor[1].name
                            self.bef[1] = dor[1].character
                            tmp_x+=self.input[0]
                            tmp_y+=self.input[1]
                            chr_nxt = " "
                        #magia :D
                        elif dor[0] and dor[1].name != self.bef[0]:
                            self.bef[0] = dor[1].name
                            self.bef[1] = dor[1].character
                            
                    case "obj":
                        #digamos que puede tomarlo
                        if self.adder(node[1]):
                            chr_nxt = mapper.square[tmp_y+self.input[1]][tmp_x+self.input[0]]
                            mapper.del_child(node[1], kind="dinamic")
                        #no pudo tomarlo
                        else:
                            return
                        
        #actualiza el anterior caracter
        mapper.square[self.global_y] = insert(mapper.square[self.global_y],
                                              chr_nxt,
                                              self.global_x,
                                              self.global_x+1)
        
        self.global_x = tmp_x
        self.global_y = tmp_y
        
        #inserta a la posición actual
        mapper.square[self.global_y] = insert(mapper.square[self.global_y],
                                              self.character,
                                              self.global_x,
                                              self.global_x+1)
        
        #actualiza el mapa
        mapper.set_pre_view()
        