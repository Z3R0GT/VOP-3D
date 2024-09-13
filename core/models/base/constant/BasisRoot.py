from .BasisSquare import *
from ..include.BasisTreeNode import *

class BasisRoot(BasisSquare, BasisTreeNode):
    def _base(self):
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
            
            
    def _insert_square(self, node):
        if node.in_id != Ellipsis:
            checker_coord([node.vec[0]+node.transform[0], node.vec[1]+node.transform[1]], self.__kind_vector__())
            checker_coord(self, node)

        c=0
        for y in range(node.vec[1], node.transform[1]+2):
            self.square[y] = insert(self.square[y], node.square[c], node.vec[0], node.vec[0]+node.transform[0])
            c+=1
    
        self.__set_pre_view__()