from ...base.constant.Text import *
from ...base.include.BasisTreeNode import *

COMPONENTS_LB_FA = ["btn", "pnl", "men", "map", "stu"]

class Label(text, BasisTreeNode):
    def __init__(self, 
                 name: str, 
                 text: str, 
                 x: int, 
                 y: int, 
                 comment: str | None = None) -> None:
        super().__init__(name, text, "0", "lbl",x, y, comment)
        super().__child_node__(COMPONENTS_LB_FA)