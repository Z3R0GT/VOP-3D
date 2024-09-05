from .BasisSquare import *
from ..include.BasisTreeNode import *

class BasisRoot(BasisSquare, BasisTreeNode):
    def _base(self):
        self.can_be_father(self, throw=True)
        if self.child_tlt == 0 or len(self.child_lst) == 0:
            raise HasNotChilds(self)
        
        self.__del_pre_view__()
        self.__del_square__()
        
        self._set_frame_square_()
        if DEBUG_MODE[0]:
            self._set_frame_num_square_()
    
    def __update_children__(self, father_update:bool=True):
        self._base()
        for node in self.child_lst:
            if hasattr(node, "name"):
                self.add_child(node, False)

        if father_update:
            if self.can_be_child(self):
                self.fahter.__updater_father__()
                from ..tools.ScreenTools import print_debug
                print_debug("EL PADRE SE HA ACTUALIZADO")
            else:
                from ..tools.ScreenTools import print_debug
                print_debug("EL PADRE NO HA ACTUALIZADO")
        
    def __updater_father__(self):
        self._base()
        for node in self.child_lst:
            node.__update_children__(False)
            self.add_child(node, False)
            
            