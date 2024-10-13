import pynput as pn

from ..references import PLA_OBJ, MENU_OBJ, find_node
from .interactive.Skeleton import *
from .interactive.stats import *

from ..ui.menu import *
from ..ui.buttons import *

class Player(Skeleton, Stats):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, *,
                 comment: str | None = None) -> None:
        super().__init__(name, chr, x, y, 
                         len(PLA_OBJ), "pla",
                         comment=comment)
        super().__stats__()
        #TODO: transferir a su propio objeto        
        PLA_OBJ.append(self)
        
    def __key_normal(self, key):
        try:
            inp = key.char
            self.key_input(inp)
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
                
    def key_input(self, key):...
    
    
    def setup_configs(self, lst_key:list[str], lst_func:list):
        self.controll+=[i.lower() for i in lst_key]
        self.config = lst_func
        
    
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
            self.key_input(input("dirección:\n>..."))
    
