#esta clase hereda de "interactive.object" y son todo los objetos que puedes
# conseguir dentro del juego (entre esos monedas) 
from .base.inventory import *
from .interactive.object import *

class ObjectModel(Inventory, Object):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, 
                 *, can_move: bool = False,
                 method=..., 
                 components: list[str] = ..., 
                 comment: str | None = None,
                 re:dict=..., eff:dict=...) -> None:
        super().__init__(name, chr, x, y, 
                         can_move=can_move, 
                         method=method, 
                         components=components, 
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
                           components=self.comp_fa,
                           comment="Esto es una copia",
                           re=self.req,
                           eff=self.eff)
    
    
__ALL_CHR__ = \
{
    "sword":"%",
    "shield":"N",
    "pistol":"-",
}

#caracteres por defecto, version base del motor 
#TODO: posiblemente en futuras versiones, se requiere cambiar para soportar multiples cosas
REQ_SWORD = "None"
EFF_SWORD = {"DMG":1} 
CHR_SWORD = __ALL_CHR__["sword"]

class Sword(ObjectModel):
    def __init__(self, name: str, x: int, y: int, *, 
                 can_move: bool = False, 
                 comment: str | None = None, ) -> None:
        super().__init__(name, CHR_SWORD, x, y, 
                         can_move=can_move, 
                         comment=comment, 
                         re=REQ_SWORD, eff=EFF_SWORD)
        
REQ_SHIELD = "None"
EFF_SHIELD = {"DEF":10}
CHR_SHIELD = __ALL_CHR__["shield"]
        
class Shield(Inventory, Object):
    def __init__(self, name: str, x: int, y: int, *, 
                 can_move: bool = False, 
                 comment: str | None = None) -> None:
        super().__init__(name, CHR_SHIELD, x, y, 
                         can_move=can_move,
                         comment=comment)
        super().__meta__(REQ_SHIELD, EFF_SHIELD)
        
def _apply_effect(what, eff):
    return what-eff
    
REQ_PISTOL = "None"
EFF_PISTOL = {"LIFE":1}
CHR_PISTOL = __ALL_CHR__["pistol"]
        
class Pistol(Inventory, Object):
    def __init__(self, name: str, chr: str, x: int, y: int, *, 
                 can_move: bool = False, 
                 comment: str | None = None) -> None:
        super().__init__(name, CHR_PISTOL, x, y,
                         can_move=can_move, 
                         method=_apply_effect, 
                         comment=comment)
        super().__meta__(REQ_PISTOL, EFF_PISTOL)