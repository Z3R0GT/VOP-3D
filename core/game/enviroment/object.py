from ...models.data.d2.ObjectModel import ObjectModel

__ALL_CHR__ = \
{
    "sword":"%",
    "shield":"N",
    "pistol":"-",
    "scroll":"M"
}

#caracteres por defecto, version base del motor 
#TODO: posiblemente en futuras versiones, se requiere cambiar para soportar multiples cosas
REQ_SWORD = "None"
EFF_SWORD = {"DMG":1} 
CHR_SWORD = __ALL_CHR__["sword"]

class Sword(ObjectModel):
    def __init__(self, name: str, x: int, y: int, *, 
                 comment: str | None = None, ) -> None:
        super().__init__(name, CHR_SWORD, x, y, 
                         comment=comment, 
                         re=REQ_SWORD, eff=EFF_SWORD)
        
REQ_SHIELD = "None"
EFF_SHIELD = {"DEF":10}
CHR_SHIELD = __ALL_CHR__["shield"]
        
class Shield(ObjectModel):
    def __init__(self, name: str, x: int, y: int, *, 
                 comment: str | None = None) -> None:
        super().__init__(name, CHR_SHIELD, x, y, 
                         comment=comment,
                         re=REQ_SHIELD , eff=EFF_SHIELD)
        
def _apply_effect(what, eff):
    return what-eff
    
REQ_PISTOL = "None"
EFF_PISTOL = {"LIFE":1}
CHR_PISTOL = __ALL_CHR__["pistol"]
        
class Pistol(ObjectModel):
    def __init__(self, name: str, x: int, y: int, *, 
                 comment: str | None = None) -> None:
        super().__init__(name, CHR_PISTOL, x, y,
                         method=_apply_effect, 
                         comment=comment,
                         re=REQ_PISTOL, eff=EFF_PISTOL)
        
def _print_scroll_():
    #insert action here
    ...
        
class Scroll(ObjectModel):
    def __init__(self, name: str, chr: str, x: int, y: int, *,
                 method=...,
                 comment: str | None = None, re: dict = ..., eff: dict = ...) -> None:
        super().__init__(name, chr, x, y, 
                         method=method, comment=comment, re="None", eff=eff)