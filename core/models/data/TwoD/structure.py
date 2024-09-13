from .config.constant import PANE_OBJ, DOOR_OBJ

from ...base.constant.BasisRoot import *

COMPONENTS_STU_CH:list[str] = ["dor", "obj", "stu"]
COMPONENTS_STU_FA:list[str] = ["map", "stu"]

COMPONENTS_DOR_FA:list[str] = ["stu"]

class Door(BasisRoot):
    def __init__(self, 
                 name: str, 
                 x:int,
                 y:int,
                 chr:str,*,
                 pos:bool=True,
                 multi:int=1,
                 comment: str | None = None) -> None:
        
        super().__init__(name, len(DOOR_OBJ), "dor", comment)
        super().__vector__(chr, x, y)
        super().__child_node__(COMPONENTS_DOR_FA)
    
        self.list = [pos, multi]
        DOOR_OBJ.append(self)

    
class Structure(BasisRoot):
    def __init__(self, 
                 name: str, 
                 x:int,
                 y:int,
                 sz_x:int,
                 sz_y:int,
                 chr:str,
                 comment: str | None = None) -> None:
        super().__init__(name, len(PANE_OBJ), "stu", comment)
        super().__viewport__()
        super().__vector__(chr, x, y)
        super().__transform__(sz_x, sz_y)
        
        super().__father_node__(COMPONENTS_STU_CH)
        super().__child_node__ (COMPONENTS_STU_FA)
        
        self._set_frame_square_()
        if DEBUG_MODE[0]:
            self._set_frame_num_square_()
        PANE_OBJ.append(self)
    

    def adder(self, node: Door):
        checker_coord(node.vec, self.transform)
        match node.abs:
            case "dor":
                if node.list[0]:
                    txt = node.character*node.list[1]
                    self._edit_line_square_([node.vec], txt)
                else:
                    for y in range(node.list[1]):
                        self._edit_line_square_([[node.vec[0], node.vec[1]+y]], node.character)
                
                self.__del_pre_view__()
                self.__set_pre_view__()
            case "stu":
                self._insert_square(node)
        
    def deleter(self, node:Door):
        match node.abs:
            case choice if choice in ["stu", "obj"]:
                ...
            case "dor":
                if node.list[0]:
                    txt = " "*(len(node.character)+node.list[1])
                    self._edit_line_square_([node.vec], txt)
                else:
                    for y in range(node.list[1]):
                        self._edit_line_square_([[node.vec[0], node.vec[1]+y]], " "*len(node.character))
                
                self.__del_pre_view__()
                self.__set_pre_view__()

        self.__update_children__(False)
           
    def create_square(self, kind:Literal["X", "Y", "-Y"],
                      y_init:int,
                      y_end:int,
                      x_init:int,
                      x_end:int,
                      formated:bool=True) -> list[int, int, int]:
        coord = []
        checker_coord([x_init, x_end], [self.transform[0], self.transform[1]])
        checker_coord([y_init, y_end], [self.transform[1], self.transform[1]])
    
        match kind:
            case "X":
                coord.append((x_init, x_end, y_init))
            case "Y":
                for line in range(y_init, y_end):
                    coord.append((x_init, x_end, line))
            case "-Y":
                for line in range(y_init, y_end, -1):
                    coord.append((x_init, x_end, line))
        
        if formated:
            self.edit_geometry(coord)
            return coord
        else:
            return coord
                    
                    