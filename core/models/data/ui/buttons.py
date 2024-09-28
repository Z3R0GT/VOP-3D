from ...base.include.layout.BasisUI import MARK_SCAPE
from ...base.constant.function import *
from ...base.include.BasisTreeNode import *

from ..references import MENU_OBJ, BUTTONS_OBJ

def __queque__(*args, **kwargs):
    exit()
    
def __continue__(*args, **kwargs):
    return

def __link__(*args, **kwargs):
    from webbrowser import open
    contains(kwargs, ["value"], throw=True)
    open(secure_type_one(value=kwargs["value"], kind=True))
    
def __main_menu__(*args, **kwargs):
    #TODO: requiere un reemplanteamiento
    #MENU_OBJ[0]
    print(kwargs)
    ...
    
def __back__(*args, **kwargs):
    #Función empleada para llamar a un menu X y iniciar su cast
    print(kwargs)
    ...
    
COMPONENTS_BTN_FA:list[str] = ["pnl", "men"]
class Buttons(Function, BasisTreeNode):
    def __init__(self, name: str, 
                 text: str,
                 x: int, y: int, 
                 comment: str | None = None,
                 default:Literal["EXIT", 
                                 "LOAD", 
                                 "SAVE", 
                                 "BACK", 
                                 "MAIN",
                                 "LINK", 
                                 "LIST",
                                 "OUTP",
                                 "CONTINUE", 
                                 "CUSTOM"]="CUSTOM",
                action=...) -> None:
        super().__init__(name, text, 
                         len(BUTTONS_OBJ), "btn", 
                         x, y, 
                         comment)
        super().__child_node__(COMPONENTS_BTN_FA)
        super().__func__(action)
        
        self.cast      = ("")
        
        match default:
            case "EXIT":
                if text== "":
                    self.character ="Salir"
                self.action = __queque__
            case "MAIN":
                if text == "":
                    self.character = "Menu"
                self.action = __main_menu__
            case "BACK":
                if text == "":
                    self.character = "Regresar"
                self.action = __back__
            case "LINK":
                if text == "":
                    self.character = "Abrir URL"
                self.action = __link__
                self.var = action
            case "CONTINUE":
                if text == "":
                    self.character = text
                self.action = __continue__
            case "CUSTOM":
                self.action = action
            case _:
                self.action = action
        
        BUTTONS_OBJ.append(self)
        
    def caster(self, msg:tuple[str]=(""), **kwargs):
        self.cast = msg
        self.var = kwargs
                
    def input(self):
        _in_ = []
        
        for msg in list(self.cast):
            _in_.append(input(f"{msg}{MARK_SCAPE}"))
        self.action(*_in_, **self.var)