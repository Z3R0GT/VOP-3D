# esta clase de objetos aparecen en pantalla, teniendo las siguientes caracteristicas 
# * puede moverse 
# * puede ser "tomado" por otro objeto
# * puede ejcutar algunas funciones (de ser necesario)

from .Skeleton import *
from ...references import OBJ_OBJ

class Object(Skeleton):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, *, 
                 can_move:bool=False,
                 method=...,
                 components: list[str] = ..., 
                 comment: str | None = None) -> None:
        super().__init__(name, chr, x, y, len(OBJ_OBJ), "obj", components=components, comment=comment)
        super().__func__(method)   
            
        self.can_move = can_move
        self.set_meta("can_move", self.can_move)
        
        OBJ_OBJ.append(self)
        
    