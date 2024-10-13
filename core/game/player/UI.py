from ...models.data.ui import *
from ...models.data.d2.env import *

def _cont_(*args):
    PLAYING[0] = True

def inventory(**kwargs):
    
    print(kwargs)
    input()
    info = ["uwu", "asd"] # reemplazar esto con lo necesario en nombre objeto
    men = Menu("menu_inventory", "#", 50, 13)
    men.add_child(Label("uwu", "Menu de inventario", 1, 1))
    
    pnl = PanelList("pnl", "#", 
                    24, 1, 
                    23, 10, 
                    info, 2, 2)

    re  = Buttons("resume", "Reanudar", 1, 5, default="CONTINUE", action=_cont_)
    nxt = Buttons("nxt", "Siguiente", 36, 11)
    bfr = Buttons("bfr", "Anterior", 23, 11)
    exi = Buttons("exit", "Salir del juego", 1, 11, default="EXIT")

    men.add_child(re)
    men.add_child(exi)
    men.add_child(nxt)
    men.add_child(bfr)

    pnl.setup_btns_in(bfr, nxt)
    men.add_child(pnl)
    pnl.refresh()

    men.start()
    
def config(**kwargs):
    men = Menu("config", "#", 40, 12)
    men.add_child(Label("generic", "Menu de configuración", 1, 1))

    re  = Buttons("resume", "Reanudar", 3, 3)
    vol = Buttons("volumen", "Dar volumen", 3, 5)
    mn  = Buttons("return", "Volver al menu", 3, 7, default="MAIN")

    men.add_child(re)
    men.add_child(vol)
    men.add_child(mn)
    
    men.start()