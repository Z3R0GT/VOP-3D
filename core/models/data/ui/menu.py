#BASIS
from ...base.include.BasisUI import *
from ...base.include.BasisTreeNode import *

#COMPONENTS
from .buttons import Buttons, MARK_SCAPE
from .components.panel import Panel

#REFERENCES
from ..references import MENU_OBJ

COMPONENTS_MENU_CH = ["btn", "pnl"]

class Menu(BasisUI, BasisTreeNode):
    def __init__(self, 
                 name: str, 
                 x: int, 
                 y: int, 
                 chr:str,
                 comment: str | None = None) -> None:
        
        super().__init__(name, len(MENU_OBJ), "men", chr, x, y, comment)
        super().__father_node__()

        self.btns:list[Buttons]=[]
        self.panel:list[Panel] =[]

        self.child_lst:list[Buttons| Panel]
        
        self._set_frame_square_2d_(self.vec)

        if DEBUG_MODE[0]:
            self._set_frame_num_square_2d_(self.vec[0])
        MENU_OBJ.append(self)

    def adder(self, node:Buttons|Panel):
        """Agrega un nodo de manera literal (no se incluye en la meta final)

        Args:
            node (BasisNode | BasisTreeNode | BasisSquare): nodo desde

        Raises:
            IncorrectTypeNode: Lanzado cuando el nodo es compatible para el tipo de objeto
        """
        if not node.abs in COMPONENTS_MENU_CH:
            raise IncorrectTypeNode(node)

        match node.abs:
            case "btn":
                text = len(f"{len(self.btns)}) "+node.character)
                if text-node.vec[0] >= self.vec[0]: 
                    raise CoordExced(text, self.vec[0]) 
                   
                self.btns.append(node)
                self.create_text(f"{len(self.btns)}) "+node.character, "CUSTOM", node.vec)
            case "pnl":
                checker_coord(node.transform, self.vec)
                for nodes in self.child_lst:
                    if nodes.name == node.name:
                        continue

                    if nodes.vec[1] == node.vec[1] and nodes.vec[0] == node.vec[0]:
                        raise CoordInConflic(nodes, node) 
                
                for y in range(node.vec[1], node.transform[1]+node.vec[1]):
                    self.square[y] =insert(self.square[y], 
                                           node.square[y-node.vec[1]],
                                           node.vec[0],
                                           node.transform[0]+node.vec[0])
                self.__set_pre_view__()
                self.panel.append(node)

    def deleter(self, node:Buttons|Panel):
        """borra un nodo de manera literal (no se incluye en la meta final)

        Args:
            node (BasisNode | BasisTreeNode | BasisSquare): nodo desde

        Raises:
            IncorrectTypeNode: Lanzado cuando el nodo es compatible para el tipo de objeto
        """
        if not node.abs in COMPONENTS_MENU_CH:
            raise IncorrectTypeNode(node)

        match node.abs:
            case "btn":
                self.create_text(" "*(node.in_id+len(node.character)), "CUSTOM", node.vec)
            case "pnl":
                
                for y in range(node.vec[1], node.transform[1]+node.vec[1]):
                    self.square[y] =insert(self.square[y], 
                                           " "*node.transform[0],
                                           node.vec[0],
                                           node.transform[0]+node.vec[0])
                self.__set_pre_view__()

    def execute(self, btn:Buttons, *args):

        btn.var = args
        self.child_lst[btn.in_id]._input_(self.child_lst[btn.in_id].cast)

    def start_cast(self, auto_resize:bool=False):
        if not DEBUG_MODE[0] or auto_resize == True:
            size_screen(obj=self)
        else:
            erase_screen()

        self.get_pre_view()

        if True:
        #try:
            _in = int(input(f"Ingresa el numero del boton{MARK_SCAPE}"))-1
            #CANCELACIÓN DE OPERACIÓN (acortador)
            if _in+1 == 2004:
                sys.exit(0)
            elif _in+1 == 3013:
                print_debug("'An human kissing a dragon, beware that's still kind of close to the zoophilia factor'.- ArchangelCGA")
                print_debug("EASTEREGG Finded")
                sleep(10)
                return 

            self.btns[_in]._input_(self.btns[_in].cast)

        #except (ValueError, IndexError) as e:
        #    print(e)


