import pynput as pn

from ..references import PLA_OBJ, MENU_OBJ, find_node
from .interactive.Skeleton import *
from .interactive.stats import *

from ..ui.menu import *
from ..ui.buttons import *


@final
class Player(Skeleton, Stats):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, *,
                 components: list[str] = ..., 
                 comment: str | None = None) -> None:
        super().__init__(name, chr, x, y, 
                         len(PLA_OBJ), "pla",
                         components=components, 
                         comment=comment)
        super().__stats__()
        #TODO: transferir a su propio objeto        
        PLA_OBJ.append(self)
        
    def __key_normal(self, key):
        try:
            inp = key.char
            
            match inp:
                case "i":
                    #mata los procesos
                    self.move("stop")
                    PLAYING[0] = False
                    #nombre reservado (menu_pause)
                    ...
                    #crea los menu :v
                    
                case _:
                    self.mover(inp)
        except AttributeError:
            pass
        
    def __key_special(self, key):
        if key == pn.keyboard.Key.esc:
            PLAYING[0] = False
            self.key.stop()
            self.special.stop()
        if key == pn.keyboard.Key.space:
            PAUSING[0] = not PAUSING[0]
            self.move("stop")
            if not PAUSING[0]:
                self.setup_move("key")
                self.key.start()

    #NOTE: ESTO SOLO PUEDE SER LLAMADO UNA VEZ!
    def setup_move(self, kind:Literal["key", "special", "all"]="all"):
        if kind == "all":
            self.key = pn.keyboard.Listener(
                                on_press=self.__key_normal, 
                                )
            self.special = pn.keyboard.Listener(
                                on_press=self.__key_special
                                )
        elif kind == "key":
            self.key = pn.keyboard.Listener(
                                on_press=self.__key_normal, 
                                )
        elif kind == "special":
            self.special = pn.keyboard.Listener(
                                on_press=self.__key_special
                                )
            
    def move(self, kind:Literal["start", "stop", "debug"]):
        if kind == "start":
            self.key.start()
            self.special.start()
        elif kind == "stop":
            self.key.stop()
        elif kind == "debug":
            self.mover(input("dirección:\n>..."))
       
    @override     
    def adder(self, node):
        node = secure_type_one(node=node, abs="obj")
        re = node.canEffect(self.stats)
        
        if re:
            self.apply_effects(re)
            return True
        else:
            return re
