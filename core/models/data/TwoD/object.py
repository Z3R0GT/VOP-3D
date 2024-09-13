from .config.constant import OBJI_OBJ

from ...base.include.BasisTreeNode import *
from ...base.constant.BasisSquare import *

COMPONENTS_OBJI_FA:list[str]=["map", "stu"]

class Object(BasisSquare, BasisTreeNode):
    def __init__(self, 
                 name: str, 
                 x:int,
                 y:int,
                 chr:str,
                 comment: str | None = None) -> None:
        super().__init__(name, 
                         len(OBJI_OBJ), 
                         "obj", 
                         comment)
        super().__vector__(chr, x, y)
        super().__child_node__(COMPONENTS_OBJI_FA)
        
        OBJI_OBJ.append(self)