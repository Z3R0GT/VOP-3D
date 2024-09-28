from core.models.base.tools.maths import insert
from ..references import MAP_OBJ
from ...base.include.BasisTreeNode import *

from .base.object2d import *

COMPONENTS_ME_CH:list[str]=["obj", "stu", "pla", "test"]

COMPONENTS_EXE:list[str]=["pla"]

@final
class Mapa(Object2D, BasisTreeNode):
    def __init__(self, name: str, 
                 chr, x, y, 
                 comment: str | None = None) -> None:
        super().__init__(name, len(MAP_OBJ), "map", chr, x, y, comment)
        super().__mem_chunks__(COMPONENTS_EXE)
        super().__square__()
        super().__father_node__(COMPONENTS_ME_CH)
        
        
        self.set_frame_square()
        if DEBUG_MODE[0]:
            self.set_frame_num_square()
        
        MAP_OBJ.append(self)
        
    def adder(self, node)->None:
        
        match node.abs:
            case "stu":
                self.insert_square(node)
            case "pla":
                self.square[node.vec[1]] = insert(self.square[node.vec[1]], 
                                                  node.character, 
                                                  node.vec[0], node.vec[0]+1)
                self.set_pre_view()
            case "obj":
                self.square[node.vec[1]] = insert(self.square[node.vec[1]], 
                                                  node.character, 
                                                  node.vec[0], node.vec[0]+1)
                self.set_pre_view()
            case _:
                print(f"NODO {node.name}/{node.abs} NO FUE AGREGADO, CONTINUANDO EJECUCIÓN")
        self.generate_chunks()
                
    def deleter(self, node)->None:
        match node.abs:
            
            case "stu":
                
                #insertar codigo de borra aqui
                ...
            case "obj":
                ...        
                
        self.generate_chunks()
