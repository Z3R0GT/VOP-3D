from ...base.include.layout.BasisUI import *
from ...base.include.BasisTreeNode import *
from ...base.tools.maths import insert
from .components.panel import Panel
from .buttons import Buttons

from ..references import MENU_OBJ

COMPONENTS_MN_CH = ["btn", "pnl", "lbl"]

class PanelList(Panel):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, 
                 sz_x: int, sz_y: int,
                 list:list[str],
                 render:int,
                 increment:int,
                 as_num:bool=False) -> None:
        super().__init__(name, chr, x, y, sz_x, sz_y, "clase predefinida")
        self.list = list

        self.render = render
        self.increment = increment
        self.as_num = as_num
        
        self.current = [0, render]
        
    def _next_up(self, *args):
        self.current[0] += self.increment
        self.current[1] += self.increment
        
        self.update_lst()
        print(args)
        
    def _next_back(self, *args):
        self.current[0] -= self.increment
        self.current[1] -= self.increment
        
        self.update_lst()
        print(args)

    def _input(self, *args):
        print(args, self.current)


    def setup_btns_in(self, back:Buttons, next:Buttons, input:Buttons):
        self.back = back
        self.next = next
        self.inp = input
        
        self.next.action = self._next_up
        self.back.action = self._next_back
        self.inp.action  = self._input

    def setup_btns_ou(self, ou:list[Buttons]):
        self.ou = ou
        
    def update_lst(self):
        #borra las lineas de texto
        [self.create_text(" "*(self.transform[0]-2), "CUSTOM", [self.vec[0]+1, self.vec[1]+i+1]) for i in range(1, self.render-2)]

        c = -1
        for line in range(self.current[0], self.current[1]):
            #cuando llega al limite
            if line >= len(self.list):
                self.deleter(self.next)
                self.adder(self.back)
                return 
            
            #actualiza el texto a mostrar (Posiblemente tenga bugs)
            if self.as_num:
                self.create_text(f"{int(c%self.render)}) {self.list[line][:self.transform[0]-6]}",
                                 "CUSTOM",
                                 [self.vec[0]+1, int(line%self.render)+self.vec[0]+1])
            else:
                self.create_text(self.list[line][:self.transform[0]-6],
                                 "CUSTOM",
                                 [self.vec[0]+1, int(line%self.render)+self.vec[0]+1])
        
        #minimo
        if self.current[1] == self.render:
            self.adder(self.next)
            self.deleter(self.back)
            return
        
        #intermediario
        self.adder(self.next)
        self.adder(self.back)

class Menu(BasisUI, BasisTreeNode):
    def __init__(self, name: str, 
                 chr: str, 
                 x: int, 
                 y: int, comment: str | None = None) -> None:
        super().__init__(name, len(MENU_OBJ), "men", chr, x, y, comment)
        super().__father_node__(COMPONENTS_MN_CH)
        
        self.btns: list[Buttons]  =[]
        self.panel:list[Panel] =[]
        
        self.child_lst:list[Buttons|Panel]
        
        self.set_frame_square()
        if DEBUG_MODE[0]:
            self.set_frame_num_square()
        MENU_OBJ.append(self)
        
    def adder(self, node:Buttons|Panel):
        
        match node.abs:
            case "btn":
                text = f"{len(self.btns)+1}) {node.character}"
                #if len(text)-node.vec[0] >= self.vec[0]:
                #    raise CoordExced(text, self.vec[0])
                
                self.btns.append(node)
                self.create_text(text, "CUSTOM", node.vec)
            case "lbl":
                self.create_text(node.character, "CUSTOM", node.vec)
            case "pnl":
                checker(line=node.transform, limit=self.vec, vector=2)
                for nodes in self.child_lst:
                    if nodes.name == node.name:
                        continue
                    checker(line=node.kind_vector()[0], limit=self.vec, vector=2)
                    checker(line=node.vec, limit=self.vec, vector=2)
                
                for y in range(node.vec[1], node.transform[1]+node.vec[1]):
                    self.square[y] = insert(self.square[y],
                                            node.square[y-node.vec[1]],
                                            node.vec[0],
                                            node.transform[0]+node.vec[0])
                self.set_pre_view()
                self.panel.append(node)
                
    def deleter(self, node:Buttons|Panel):
        
        match node.abs:
            case "btn":
                text = (len(str(node.in_id)))+2+len(node.character)
                self.create_text(" "*text, "CUSTOM", node.vec)
            case "lbl":
                self.create_text(" "*len(node.character), "CUSTOM", node.vec)

    def execute(self, btn:Buttons|int, **kwargs):
        if not hasattr(btn, "in_id"):
            btn = self.child_lst[btn.in_id]
        
        inf = {"name":btn.name,
               "id": btn.id}
        
        self.find_child(inf)[0].input()
        
    def start(self, auto_size:bool=False):
        if not DEBUG_MODE[0] or auto_size:
            size_screen(self.vec[0], self.vec[1])
        else:
            erase_screen()
        
        self.get_pre_view()
        
        if True:
        #try:
            _in = int(input(f"Ingresa el numero del boton{MARK_SCAPE}"))-1
            if _in+1 == 2004:
                exit(1)
            elif _in+1 == 3013:
                from time import sleep
                print_debug("'An human kissing a dragon, beware that's still kind of close to the zoophilia factor'.- ArchangelCGA")
                print_debug("EASTEREGG Finded")
                sleep(10)
                return 
            
            self.btns[_in].input()
        #except (ValueError, IndexError) as e:
        #    print(e)

    ...
