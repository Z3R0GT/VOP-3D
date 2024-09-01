from ....base.include.BasisUI import *
from ....base.include.BasisTreeNode import *

from ...references import PANEL_OBJ

COMPONENTS_PANEL_FA:list[str] = ["men"]
COMPONENTS_PANEL_CH:list[str] = ["btn"]

class Panel(BasisUI, BasisTreeNode):
    def __init__(self, name: str, 
                 x: int, y: int, 
                 chr:str,
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, len(PANEL_OBJ), "pnl", chr, x, y, comment)
        super().__transform__(sz_x, sz_y)
        
        super().__father_node__(COMPONENTS_PANEL_FA)
        super().__child_node__ (COMPONENTS_PANEL_CH)
        
        self._set_frame_square_(self.transform)
        if DEBUG_MODE[0]:
            self._set_frame_num_square_(self.transform[0])
        PANEL_OBJ.append(self)
        