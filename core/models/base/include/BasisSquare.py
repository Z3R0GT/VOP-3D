from ..tools.maths import insert
from ..tools.logic import checker

from ..constant.Vector import *

__get_pre_view_att__ = ["isPrint"]

__set_frame_att__ = ["chr", "line"]
__edit_line_att__ = ["chr", "coords"]

class BasisSquare(Vector):
    def __square__(self)->None:
        self.square:list[list[str]] = []
        self.tmp_square = []
        self.pre_view = ""
        
    def set_pre_view(self):
        self.del_pre_view()
        for line in self.square:
            self.pre_view += f"{line}\n"
        for line in self.tmp_square:
            self.pre_view += f"{line}\n"
            
    def del_pre_view(self):
        self.pre_view = ""
        
    def get_pre_view(self, isPrint:bool=True):
        if isPrint:
            print(self.pre_view)
        return self.pre_view
    
    def del_square(self):
        self.square:list[list[str]] = []
        
    def get_square(self) -> list[str]:
        return self.square
    
    #forma basica de un cuadrado/rectangulo
    def set_frame_square(self, **kwargs:dict):
        coords = self.kind_vector()[0]
        char = self.character
        #en caso solo necesite modificar el caracter
        if contains(kwargs, __set_frame_att__[0]):
            tmp = secure_type_one(value=kwargs["chr"],kind="a")
            if tmp != "default":
                char = tmp
            del tmp
            
        #en caso necesite una linea en concreto
        if contains(kwargs, __set_frame_att__):
            tmp:Literal["last", "start"] = secure_type_one(value=kwargs["line"], kind="a")
            if tmp == "start":
                return f"{char}" + " "*(coords[0]-2)+ f"{char}"
            elif tmp == "last":
                return f"{char}"*coords[0]
            del tmp
        
        #conducción normal
        for y in range(coords[1]): 
            if y == 0 or y== (coords[1]-1):
                tmp = f"{char}"*coords[0]
            else:
                tmp =  f"{char}" + " "*(coords[0]-2)+ f"{char}"
        
            if DEBUG_MODE[0]:
                self.square.append(tmp+ f"\t\tline {self.abs}: {y}")
            else:
                self.square.append(tmp)

        self.set_pre_view()
        
    def set_frame_num_square(self):
        self.del_pre_view()
        line_all = ""
        line_num = ""
        nro      = 0
        
        for num in range(self.kind_vector()[0][0]):
            re = num%10
            line_all+= str(re)
            if re == 0:
                line_num += str(nro)
                nro += 1
            else:
                line_num+=" "
                
        self.tmp_square.append(line_all)
        self.tmp_square.append(line_num)
        self.set_pre_view()
        
        
    def edit_line_square(self, **kwargs:dict):
        vec = self.kind_vector()[0]
        
        contains(kwargs, __edit_line_att__, throw=True)
        coords = secure_type_one(value=kwargs["coords"], kind=[])
        char   = secure_type_one(value=kwargs["chr"], kind="")
        
        checker(line=coords, limit=vec, vector=2)
        self.del_pre_view()
        
        len_chr = len(char)
        #cuando la linea supera el vec X actual
        if len_chr >= vec[0]:
                
            #agrega la linea nueva
            self.square[coords[1]] = insert(self.square[coords[1]], str(char), coords[0], vec[0]-1)
            #reemplaza caracter del cuadrado por el actual
            self.square[coords[1]] = insert(self.square[coords[1]], self.character, vec[0], vec[0]-1)
                
            #el booleano representa un "entro en el limite"
            return True, int(len_chr-vec[0])-1
        else:
            self.square[coords[1]] = insert(self.square[coords[1]], str(char), coords[0], coords[0]+len_chr)
            return False, 0
        
    def edit_multi_line_square(self, **kwargs:dict):
        contains(kwargs,__edit_line_att__, throw=True)
        coords = secure_type_one(value=kwargs["coords"], kind=[])
        char   = secure_type_one(value=kwargs["chr"], kind="")
        
        while True:
            result = self.edit_line_square(chr=char, coords=coords)
            self.set_pre_view()
            if not result[0]:
                return
            if not secure_type_one(value=kwargs["auto"], kind=False):
                return result
            #NOTE: dejo esta nota, es posible que no sirve, ya que en "teoria" 
            # deberia crear una nueva linea en caso se pase de la linea dada
            char = char[len(char)-result[1]-3:]
            
            try:
                checker(line=[1 ,coords[1]+1], limit=self.kind_vector()[0],vector=2)
            except CoordExced:
                #en caso ya este en el limite
                if self.kind_vector()[1] == "vec":
                    self.vec[1]+=1
                    self.set_meta("vec", self.vec)
                elif self.kind_vector()[1] == "trans":
                    self.transform[1]+=1
                    self.set_meta("transform", self.transform)
                
                self.square[-1] = self.set_frame_square(chr=self.character, line="start")
                self.square.append(self.set_frame_square(chr=self.character, line="last"))

            coords = [1, coords[1]+1]