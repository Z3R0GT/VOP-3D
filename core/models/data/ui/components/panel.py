from ....base.include.BasisUI import *
from ....base.include.BasisTreeNode import *

from ...references import PANEL_OBJ

class Panel(BasisUI, BasisTreeNode):
    def __init__(self, father, in_id:int, name: str, 
                 x: int, y: int, 
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        
        super().__init__(name, len(PANEL_OBJ), "pnl", x, y, comment)
        super().__tranform_2d__(sz_x, sz_y)
        super().__child_node__(father, in_id)


