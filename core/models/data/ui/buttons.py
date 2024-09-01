from ...base.include.BasisButtons import *
from ...base.include.BasisTreeNode import *
from ..references import *


def __link__(*nm):
    from webbrowser import open
    open(nm[1])

def __continue__(*nm):
    return

def __queque__(*nm):
    sys.exit()

def __save__():

    print("SAVE WIP")

def __load__():

    print("LOAD WIP")
    

def __main_menu__(*nm):
    MENU_OBJ[0].start_cast()

def __back__(*nm):
    inp = nm[0]
    var = nm[1]
    try:
        MENU_OBJ[var].start_cast()
    except IndexError:
        print_debug("MENU NO ENCONTRADO")
        
COMPONENTS_BTN_FA:list[str]= ["pnl", "men"]
class Buttons(BasisButtons, BasisTreeNode):
    def __init__(self, 
                 name: str, 
                 x: int, 
                 y: int, 
                 text:str="",
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
        
        super().__init__(name, len(BUTTONS_OBJ), "btn", text, x, y, comment)
        super().__child_node__(COMPONENTS_BTN_FA)

        self.in_id:int = 0

        self.cast= ("")
        self.var = []

        match default:
            case "SAVE":
                if text == "":
                    self.character = "Guardar"
                self.action = __save__
            case "LOAD":
                if text == "":
                    self.character = "Cargar"
                self.action = __load__
            case "EXIT":
                if text == "":
                    self.character = "Salir"
                self.action = __queque__
            case "MAIN":
                if text == "":
                    self.character = "Regresar"
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
                    self.character = "Continuar"
                self.action = __continue__
            case "CUSTOM":
                self.action = action
            case _:
                self.action = action

        BUTTONS_OBJ.append(self)
        
    def caster(self, msg:tuple[str]=(""), *var):
        """Setea las variable 'cast' y 'var' para su uso posterior (no retreactivo)

        Args:
            msg (tuple[str], optional): conjunto de mensaje a mostrar en pantalla. Defaults to ("").
        """
        self.cast = msg
        self.var = list(var)