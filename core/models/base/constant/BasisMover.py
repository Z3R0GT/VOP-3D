from .Vector import *
from ..include.BasisTreeNode import *
from .function import *

COMPONENTS_GENERIC_MOV_FA:list[str] = ["map", "stu"]
COMPONENTS_GENERIC_MOV_CH:list[str] = ["obj"]
DEFAULT_CONTROLLS:list[str]=['w', 's', 'a', 'd']

class BasisMover(Vector, BasisTreeNode, Function):
    def __init__(self, name: str, 
                 chr:str, 
                 x:int, y:int,
                 id: int, abs: str, 
                 controll:list[str]=...,
                 components:list[str]=...,
                 comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__vector__(chr=chr, x=x, y=y)
        super().__father_node__(COMPONENTS_GENERIC_MOV_CH)
        
        if components != ... and components == COMPONENTS_GENERIC_MOV_FA:
            super().__child_node__(components)
        else:
            super().__child_node__(COMPONENTS_GENERIC_MOV_FA)

        if controll != ... and controll == DEFAULT_CONTROLLS:
            self.controll = controll
        else:
            self.controll = DEFAULT_CONTROLLS
        
    def __coords__(self) -> None:
        if len(self.kind_vector()[0]) == 2:
            self.global_x = self.vec[0]
            self.global_y = self.vec[1]
            self.kind = 2 # TODO: simplificar a un vector y convertir a función (similar a .kind_vector )
        elif len(self.kind_vector()[0]) == 3:
            self.global_x = self.vec[0]
            self.global_y = self.vec[1]
            self.global_z = self.vec[2]
            self.kind = 3
    
    #da variables necesarias para ser controlados por
    #teclado/programables 
    def __caster__(self) -> None:
        if len(self.kind_vector()[0]) == 2:
            self.in_x = 0
            self.in_y = 0
        elif len(self.kind_vector()[0]) == 3:
            self.in_x = 0
            self.in_y = 0
            self.in_x = 0
        
        