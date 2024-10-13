from ...base.include.layout.BasisUI import *
from ...base.include.BasisTreeNode import *
from ...base.tools.maths import insert
from .components.panel import Panel
from ..custom.Label import *
from .buttons import Buttons

from ..references import MENU_OBJ

COMPONENTS_MN_CH = ["btn", "pnl", "lbl"]

class PanelList(Panel):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, 
                 sz_x: int, sz_y: int,
                 lst:list[str],
                 render:int,
                 increment:int,
                 as_num:bool=False) -> None:
        super().__init__(name, chr, x, y, sz_x, sz_y, "pre_def_name")
        
        self.list:list[Label] = []
        for i in range(len(lst)):
            self.list.append(Label("n", lst[i], 1, i+1))
        
        self.render = render
        self.increment = increment
        self.as_num = as_num
        
        self.current = [0, render]
        
        
    def _next_up(self, *args):
        if self.current[1] < len(self.list):
            self.current[0] += self.increment
            self.current[1] += self.increment
        
        self.refresh(True)
        
    def _next_back(self, *args):
        if self.current[1] >= 0:
            self.current[0] -= self.increment
            self.current[1] -= self.increment

        self.refresh(True)

    def _input(self, *args):
        num = int(input(f"Ingrese ID de la opción{MARK_SCAPE}"))+self.current[0]
        if not num in range(self.current[0], self.current[1]):
            from random import randint
            num = randint(self.current[0], self.current[1])
        for btn in self.ou:
            btn.var["input"] = self.list[num].character
        self.refresh(True)
        
    def setup_btns_in(self, back:Buttons, next:Buttons, input:Buttons=...):
        self.back = back
        self.next = next
        if not input == ...:
            self.inp = input
            self.inp.action  = self._input
        
        self.next.action = self._next_up
        self.back.action = self._next_back

    def setup_btns_ou(self, ou:list[Buttons]):
        self.ou = list(ou)
       
    def refresh(self, start:bool=False):
        self.update_list()
        self.father[0].adder(self)
        if start:
            self.father[0].start()
        
    def update_list(self):
        if self.current[1] > len(self.list):
            return
            
        #borra las lineas de texto
        [self.create_text(" "*(self.transform[0]-2), "CUSTOM", [1, i]) for i in range(1, self.render+1)]
        
        c = 1
        for line in range(self.current[0], self.current[1]):
            if line >= len(self.list):
                break
            
            #actualiza el texto a mostrar (Posiblemente tenga bugs)
            if self.as_num:
                self.create_text(
                    f"{c}) {self.list[line].character[:self.transform[0]-6]}",
                    "CUSTOM",
                    [1, c]
                )
            else:
                self.create_text(
                    self.list[line].character[:self.transform[0]-6],
                    "CUSTOM",
                    [1, c]
                )
            c+=1
            
        if line >= self.current[1]:
            self.father[0].deleter(self.next)
            self.father[0].adder(self.back)
        #minimo
        elif self.current[1] == self.render:
            self.father[0].adder(self.next)
            self.father[0].deleter(self.back)
            return
        else:
            #intermediario
            self.father[0].adder(self.next)
            self.father[0].adder(self.back)
        
        
        

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
                if not node.id in [i.id for i in self.btns]:
                    self.btns.append(node)
                    num = node.in_id[node.father.index(self)]
                else:
                    num =self.btns[self.btns.index(node)].in_id[node.father.index(self)]
                    
                text = f"{num}) {node.character}"
                
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
                if not node.id in [i.id for i in self.panel]:
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
            #erase_screen()
            ...
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

