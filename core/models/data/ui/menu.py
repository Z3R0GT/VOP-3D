#BASIS
from ...base.include.BasisUI import *
from ...base.include.BasisTreeNode import *

#COMPONENTS
from .buttons import Buttons
from .components.panel import Panel

#REFERENCES
from ..references import MENU_OBJ

class Menu(BasisUI, BasisTreeNode):
    def __init__(self, 
                 name: str, 
                 x: int, 
                 y: int, 
                 chr:str,
                 comment: str | None = None) -> None:
        
        super().__init__(name, len(MENU_OBJ), "men", chr, x, y, comment)
        super().__father_node__()

        self.btns:list[Buttons]=[]
        self.panel:list[Panel] =[]

        self.__set_meta__("panel", self.panel)

        self._set_frame_square_2d_(self.vec)
        if DEBUG_MODE:
            self._set_frame_num_square_2d_(self.vec[0])
        MENU_OBJ.append(self)

