from ....base.include.layout.BasisUI import *
from ....base.include.BasisTreeNode import *

from ...references import PANEL_OBJ

COMPONENTS_PNL_FA:list[str] = ["men"]
COMPONENTS_PNL_CH:list[str] = ["lbl"]

class Panel(BasisUI, BasisTreeNode):
    def __init__(self, name: str, 
                 chr: str, x: int, y: int, 
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, len(PANEL_OBJ), "pnl", chr, x, y, comment)
        super().__transform__(size_x=sz_x, size_y=sz_y)
        
        super().__father_node__(COMPONENTS_PNL_CH)
        super().__child_node__ (COMPONENTS_PNL_FA)
        
        self.set_frame_square()
        if DEBUG_MODE[0]:
            self.set_frame_num_square()
        PANEL_OBJ.append(self)
        
    def adder(self, node):
        match node.abs:
            case "lbl":
                self.create_text(node.character, "CUSTOM", node.vec)
            case "btn":
                ID = self.find_child(node)
                btn = self.child_lst[ID]
                print(btn, ID)  
                self.create_text(f"{ID+1}) {btn.character[:self.transform[0]-5]}",
                                 "CUSTOM",
                                 btn.vec)
                
    def deleter(self, node:BasisSquare):
        match node.abs:
            case "lbl":
                self.create_text(" "*len(node.character), "CUSTOM", node.vec)
        