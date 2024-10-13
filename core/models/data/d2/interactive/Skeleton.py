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

def _inside_case_(node, global_pos, chr_nxt:str, chr_bef:list[str], self=...) -> list[Literal["is_inside","can_walk", "can_jump", "no_pass"]| EllipsisType|BasisMover]:
    #NOTE: en caso en el futuro existan más "interiores", es correcto 
    # agregarlos aqui de ser necesario
    match node.abs:
        case "stu":
            dor = _inter(global_pos, node, ["dor", "obj"], True)
            #NOTE: cuando encuentra el nodo o esta dentro del mismo
            if dor[0]:
                match dor[1].abs:
                    case "obj":
                        #TODO: en caso volver a escribir la parte de movimiento, resolver bug que no se puede evaluar el stu correctamente por alguna razon
                        ...
                    case "dor":
                        #X
                        if chr_nxt == chr_bef[1]:
                            return ["can_walk", ...]
                        #Y
                        elif chr_nxt == dor[1].character:
                            return ["can_jump", dor[1]]
                        #Actualizar el caracter
                        else:
                            return ["is_inside", dor[1]]
            #NOTE: esta fuera del nodo o no lo encontro
            else:
                return ["can_walk", ...]
        
def _object_case(self, main:BasisTreeNode, node) -> list[Literal["no_pass", "can_walk"], EllipsisType]:
    if self.adder(node):
        main.del_child(node, kind="dinamic")
        return ["can_walk", ...]
    else:
        return ["no_pass", ...]
class Skeleton(BasisMover):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, 
                 id: int, abs: str, *,
                 components: list[str] = ..., 
                 comment: str | None = None) -> None:
        super().__init__(name, chr, x, y, id, abs, components, comment)
        super().__coords__()
        super().__caster__()
        self.bef = [" ", " "]
        self.input = (self.in_x, self.in_y)
    
    #NOTE: estas funciones puede ser sobre escrita... no hace falta documentar
    def mover(self, key:str):
        self.__caster__()
        w, s, a, d = [self.controll[i] for i in range (4)] 
        
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
        #return significa que no se movera el personaje 
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
                    #NOTE: solo evalua el "cuadrado" interno, nada más (hacer el TODO de arriba, puto)
                    case choice if choice in ["stu"]:
                        
                        if chr_nxt == node[1].character:
                            return
                        
                        re = _inside_case_(node[1], glob, chr_nxt, self.bef, self)
                        match re[0]:
                            case "can_jump":
                                self.bef[0] = re[1].name
                                self.bef[1] = re[1].character
                                tmp_x+=self.input[0]
                                tmp_y+=self.input[1]
                                chr_nxt=" "
                            case "can_walk":
                                tmp_x+=self.input[0]
                                tmp_y+=self.input[1]
                                chr_nxt=" "
                            #solo ejecutado cuando el objeto esta dentro del nodo
                            case "is_inside":
                                self.bef[0] = re[1].name
                                self.bef[1] = re[1].character      
                            case "no_pass":
                                return                      
                    case choice if choice == "obj":
                        re = _object_case(self, mapper, node[1])
                        match re[0]:
                            case "can_walk":
                                chr_nxt = mapper.square[tmp_y+self.input[1]][tmp_x+self.input[0]]
                            case "no_pass":
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
        