#BASIS
from ....base.include.BasisUI import *
from ....base.include.BasisTreeNode import *

#COMPONENTS
from ..buttons import Buttons

#REFERENCES
from ...references import PANEL_OBJ

class Panel(BasisUI, BasisTreeNode):
    def __init__(self, name: str, 
                 x: int, y: int, 
                 chr:str,
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, len(PANEL_OBJ), "pnl", chr, x, y, comment)
        super().__tranform_2d__(sz_x, sz_y)
        super().__child_node__()

    def set_interactive(self):

        ...


