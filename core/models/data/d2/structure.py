from multiprocessing import Value
from .base.object2d import *
from ...base.include.BasisTreeNode import *
from ..references import STU_OBJ, DOO_OBJ

COMPONENTS_STU_FA = ["map"]
COMPONENTS_STU_CH = ["dor", "pla", "obj"]

COMPONENTS_DOO_FA = ["stu"]

COMPONENTS_EXE:list[str] = ["pla"]
@final
class Door(Vector, BasisTreeNode):
    def __init__(self, name: str, 
                 x:int, y:int,
                 chr:str,*,
                 pos:bool=True, #<- le indica si es X o Y
                 multi:int = 1,
                 comment: str | None = None) -> None:
        super().__init__(name, len(DOO_OBJ), "dor", comment)
        super().__vector__(chr=chr, x=x, y=y)
        if pos:
            super().__transform__(size_x=multi, size_y=0)
        else:
            super().__transform__(size_x=0, size_y=multi)
        super().__child_node__(COMPONENTS_DOO_FA)
        
        self.info:list[bool, int] = [pos, multi]
        self.set_meta("info", self.info)
        DOO_OBJ.append(self)


@final
class Structure(Object2D, BasisTreeNode):
    def __init__(self, name: str, 
                 chr, x, y, 
                 sz_x:int, sz_y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, len(STU_OBJ), "stu", chr, x, y, comment)
        super().__mem_chunks__(COMPONENTS_EXE)
        super().__square__()
        super().__transform__(size_x=sz_x, size_y=sz_y)
        
        super().__father_node__(COMPONENTS_STU_CH)
        super().__child_node__(COMPONENTS_STU_FA)
        
        self.geometry:list[int, int, int] = []
        self.set_meta("geometry", self.geometry)
        self.set_frame_square()
        if DEBUG_MODE[0]:
            self.set_frame_num_square()
            
        STU_OBJ.append(self)
        
    def adder(self, node:Door):
        match node.abs:
            case "dor":
                checker(line=node.vec, limit=self.transform, vector=2)
                #caso de X
                if node.info[0]:
                    txt = node.character*node.info[1]
                    self.edit_line_square(coords=node.vec, chr=txt)
                else:
                    #BUG: es posible que este iterador no funciona
                    [self.edit_line_square(coords=[node.vec[0], node.vec[1]+y], chr=node.character) for y in range(node.info[1])]
                self.set_pre_view()
            case "stu":
                self.insert_square(node)
            case "obj":
                self.square[node.vec[1]] = insert(self.square[node.vec[1]], 
                                                  node.character, 
                                                  node.vec[0], node.vec[0]+1)
                self.set_pre_view()
        self.generate_chunks()
        
    #NOTE: recordar que el resultado  de caracter a mostrar siempre sera 
    # igual a la diferencia entre las posiciones 1-0 de Y/X respectivamente
    def generate_lines(self, kind:Literal["X", "Y", "-Y"],
                       Y_CORD:list[int, int],
                       X_CORD:list[int, int],
                       formated:bool=True) -> list[list[int, int, int], int]: #<- el ultimo int representa las iteraciones hechas (pa que no uses len() )
        
        checker(line=X_CORD, limit=[self.transform[0], self.transform[0]], vector=2)
        checker(line=Y_CORD, limit=[self.transform[1], self.transform[1]], vector=2)
        
        coord = []
        ite   = 0
        match kind:
            case "X":
                ite+=1
                coord.append([X_CORD[0], X_CORD[1], Y_CORD[0]])
            case "Y":
                for line in range(Y_CORD[0], Y_CORD[1]):
                    ite+=1
                    coord.append([X_CORD[0], X_CORD[1], line])
            case "-Y":
                for line in range(Y_CORD[1], Y_CORD[0], -1):
                    ite+=1    
                    coord.append([X_CORD[0], X_CORD[1], line])
        if formated:
            self.edit_geometry(coord)    
        return coord, ite
    
    def edit_geometry(self, coord:list[list[int, int, int]], add:bool=True) -> None:
        secure_type_one(value=coord, kind=[])
        for cord in coord:
            secure_type_one(value=cord, kind=[])
            if len(cord) != 3:
                raise CoordNotFound(cord)    
            if cord in self.geometry and add:
                #TODO: mejorar mensaje
                print("Coordenada ya existente:", cord)
                continue
            
            x_init, x_end, y = (
                                secure_type_one(value=cord[0], kind=1), 
                                secure_type_one(value=cord[1], kind=1), 
                                secure_type_one(value=cord[2], kind=1) 
                                )
            checker(line=[x_init, x_end], 
                    limit=[self.transform[0], self.transform[0]], vector=2)
            checker(num_from=y, num_to=self.transform[1], great=False)
            if add:
                self.geometry.append(cord)
                
            self.square[y] = insert(self.square[y], 
                                          f"{self.character}"*(x_end-x_init),
                                          x_init,
                                          x_end)
            
        self.set_meta("geometry", self.geometry)
        self.set_pre_view()
        
    def del_geometry(self, ID:list[int]|int):
        secute_type_multi(value=ID, kinds=[[], 1])
        try:
            list(ID)
        except TypeError:
            ID = [ID]
        ID.sort()
        
        c = True
        for i in ID:
            if not c:
                del self.geometry[i-1]
            else:
                del self.geometry[i]
                c=False
            self.del_square()
            self.set_frame_square()
            self.edit_geometry(self.geometry, False)