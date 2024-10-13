#esta clase hereda de "interactive.object" y son todo los objetos que puedes
# conseguir dentro del juego (entre esos monedas) 
from .base.inventory import *
from .interactive.object import *

class ObjectModel(Inventory, Object):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, 
                 *, can_move: bool = False,
                 method=..., 
                 comment: str | None = None,
                 re:dict=..., eff:dict=...) -> None:
        super().__init__(name, chr, x, y, 
                         can_move=can_move, 
                         method=method, 
                         comment=comment)
        super().__meta__(re, eff)
        
    @override
    def copy(self, name:str="", x:int=-1, y:int=-1):
        """Retona una copia no perzonalizable del objeto (no da padres)"""
        if name == "":
            name = self.name
        if x == -1:
            x = self.vec[0]
        if y == -1:
            y = self.vec[1]
        
        
        
        return ObjectModel(name, self.character,
                           x, y,
                           can_move=self.can_move,
                           method=self.action,
                           comment="Esto es una copia",
                           re=self.req,
                           eff=self.eff)
  