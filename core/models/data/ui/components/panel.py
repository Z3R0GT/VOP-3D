#BASIS
from ....base.include.BasisUI import *
from ....base.include.BasisTreeNode import *

#COMPONENTS
from ..buttons import Buttons

#REFERENCES
from ...references import PANEL_OBJ

COMPONENTS_PANEL_FA:list[str] = ["men"]
COMPONENTS_PANEL_CH:list[str] = ["btn"]

class Panel(BasisUI, BasisTreeNode):
    def __init__(self, name: str, 
                 x: int, y: int, 
                 chr:str,
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, len(PANEL_OBJ), "pnl", chr, x, y, comment)
        super().__tranform_2d__(sz_x, sz_y)
        super().__father_node__()
        super().__child_node__()

        self._set_frame_square_2d_(self.transform)
        if DEBUG_MODE[0]:
            self._set_frame_num_square_2d_(self.transform[0])
        PANEL_OBJ.append(self)

    def set_interactive(self,
                        items_to_ren:int,
                        items_to_ren_rgn:list[int, int],
                        msg_to_show:list,
                        btn_in:list[Buttons],
                        btn_ou:list[Buttons]|Buttons,
                        *args,
                        is_new:bool=False):
        
        #Verifica que el nodo dado si pueda ser un hijo
        for i in btn_in:
            self.can_be_child(i, components=COMPONENTS_PANEL_CH, throw=True)
        
        if hasattr(btn_in, "in_id"):
            self.can_be_child(btn_in, components=COMPONENTS_PANEL_CH, throw=True)
        else:
            for i in btn_ou:
                self.can_be_child(i, components=COMPONENTS_PANEL_CH, throw=True)


        LIMIT_ITEM_X:int = self.transform[0]
        LIMIT_ITEM_Y:int = items_to_ren
        LIMIT_POS   :int = 1

        #Borra los anteriores textos
        for in_ in range(LIMIT_ITEM_Y):
            self.create_text(" "*(LIMIT_ITEM_X-2), 
                             "CUSTOM", 
                             (self.vec[0]+LIMIT_POS, (in_%LIMIT_ITEM_Y)+self.vec[1]+LIMIT_POS))

            
        c = -1
        for in_ in range(items_to_ren_rgn[0], items_to_ren_rgn[1]):
            if in_ >= len(msg_to_show):
                ch = True
                break

            c+=1
            self.create_text(f"{c%LIMIT_ITEM_X}) {msg_to_show[in_][:LIMIT_ITEM_X-6]}",
                             "CUSTOM",
                             (self.vec[0]+LIMIT_POS, (in_%LIMIT_ITEM_Y)+self.vec[1]+LIMIT_POS))
            ch = False
        if is_new:
            return
        
        BUTTON_FOW:Buttons = btn_in[0]
        BUTTON_BAC:Buttons = btn_in[1]

        #UPDATE THE CURRENT INFO
        if hasattr(btn_in, "in_id"): #IS A BUTTON
            btn_ou.var = [self, items_to_ren_rgn[0], msg_to_show, args]
            self.add_child(btn_ou, False)
        else:                         
            for BUTTON_INP in btn_ou:
                BUTTON_INP.var = [self, items_to_ren_rgn[0], msg_to_show, args]
                self.add_child(BUTTON_INP, False)

        if ch:                                   #MAX CASE
            self.del_child(BUTTON_FOW, False)
            self.add_child(BUTTON_BAC, False)
        elif items_to_ren_rgn[1] == LIMIT_ITEM_Y:#MIN CASE
            self.del_child(BUTTON_BAC, False)
            self.add_child(BUTTON_FOW, False)
        else:
            BUTTON_BAC.var = [self, items_to_ren, 
                              [BUTTON_FOW.var[5][0]-LIMIT_ITEM_Y, BUTTON_FOW.var[5][1]-LIMIT_ITEM_Y], 
                              msg_to_show, btn_in, btn_ou, args, False]
            BUTTON_FOW.var = [self, items_to_ren,
                              [items_to_ren_rgn[0]+items_to_ren, items_to_ren_rgn[1]+LIMIT_ITEM_Y],
                              msg_to_show, btn_in, btn_ou, args, False]
            
            self.add_child(BUTTON_FOW, False)
            self.add_child(BUTTON_BAC, False)


    def adder(self, node:BasisNode|BasisTreeNode|BasisSquare):
            
        match node.abs:
            case "btn":
                print_debug(f"MODO EXPERIMENTAL: {EXPER_MODE[0]} PUEDE QUE EL OBJETO NO FUNCIONE")
                if not EXPER_MODE[0]:
                    return
                self.create_text(f"{node.in_id+1}) "+node.character, "CUSTOM", node.vec)
                

    def deleter(self, node:BasisNode|BasisTreeNode|BasisSquare):
        
        match node.abs:
            case "btn":
                self.create_text(" "*(node.in_id+len(node.character)+2), "CUSTOM", node.vec)
        ...