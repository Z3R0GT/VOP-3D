from .config.constant import MAPA_OBJ

from ...base.constant.BasisRoot import *

COMPONENTS_MAPA_CH:list[str]=["obj", "stu"]

class Mapa(BasisRoot):
    def __init__(self, 
                 name: str, 
                 x:int,
                 y:int,
                 chr:str,
                 comment: str | None = None) -> None:
        super().__init__(name, len(MAPA_OBJ), "map", comment)
        super().__viewport__()
        super().__vector__(chr, x, y)
        super().__father_node__(COMPONENTS_MAPA_CH)
        
        self._set_frame_square_()
        if DEBUG_MODE[0]:
            self._set_frame_num_square_()
        
        MAPA_OBJ.append(self)
        
    def adder(self, node:BasisNode):
        checker_coord(node.vec, self.vec)
        
        match node.abs:
            case "stu":
                self._insert_square(node)

    def deleter(self, node:BasisNode):
        match node.abs:
            case choice if choice in ["stu", "obj"]:
                pass
        
        self.__update_children__(False)