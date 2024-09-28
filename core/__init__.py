from time import sleep

from .models.data.references import TPF

#Intefaz de usuario
from .models.data.ui.buttons import * 
from .models.data.ui.menu import *
from .models.data.custom.Label import *
from .models.data.ui.components.panel import *

#2D para todos
from .models.data.camera import *
from .models.data.d2.mapa import *
from .models.data.d2.structure import *
from .models.data.d2.player import *
from .models.data.d2.objects import *

#Ambiente 2D
from .models.data.d2.env import *



#Pruebas
comp = ["map"]
class test(BasisSquare, BasisTreeNode):
    def __init__(self, name: str, 
                 id: int, abs: str, 
                 x:int, y:int,
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__vector__(chr="A", x=x, y=y)
        super().__transform__(size_x=sz_x, size_y=sz_y)
        super().__child_node__(comp)
        

        
def start_game_2d():
    pla:Player = PLA_OBJ[0]
    pla.setup_move()
    
    if not DEBUG_MODE[0]:
        pla.move("start")
    
    cam:Camera = CAMER_OBJ[0]
    while PLAYING[0]:
        if PAUSING[0]:
            continue
        
        sleep(TPF)
        
        cam.render_image("experimental")
        if DEBUG_MODE[0]:
            print("\n")
        else:
            erase_screen()
            
        cam.get_pre_view()
        if DEBUG_MODE[0]:
            pla.move("debug")
        