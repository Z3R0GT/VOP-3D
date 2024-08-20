from ...base.include.BasisButtons  import *
from ...base.include.BasisTreeNode import *
from ..references import BUTTONS_OBJ

def __link__(*nm):
    from webbrowser import open
    open(nm[1])

def __continue__(*nm):
    return

def __queque__(*nm):
    sys.exit()

def __save__():
    ...

def __load__():
    ...

def __main_menu__():
    ...


class Buttons(BasisButtons, BasisTreeNode):
    def __init__(self, 
                 father,
                 id:int,
                 name: str, 
                 x: int, 
                 y: int, 
                 text:str,
                 action=...,
                 comment: str | None = None,
                 default:Literal["EXIT", 
                                 "LOAD", 
                                 "SAVE", 
                                 "BACK", 
                                 "LINK", 
                                 "CONTINUE", 
                                 "CUSTOM"]="CUSTOM") -> None:
        
        super().__init__(name, len(BUTTONS_OBJ), "btn", x, y, comment)
        super().__child_node__(father, id)

        self.in_id:int = 0

        self.cast= ("")
        self.var = 0

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
            case "BACK":
                if text == "":
                    self.character = "Regresar"
                self.action = __main_menu__
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

    def caster(self, msg:tuple[str]=(""), *var):
        """Setea las variable 'cast' y 'var' para su uso posterior (no retreactivo)

        Args:
            msg (tuple[str], optional): conjunto de mensaje a mostrar en pantalla. Defaults to ("").
        """
        self.cast = msg
        self.var = list(var)
