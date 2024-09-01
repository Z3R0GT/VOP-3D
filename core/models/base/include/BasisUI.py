"""
Nodo base para cualquier objeto que tenga interfaz

Contribuidores
-------------
    Z3R0_GT: 0.0.0.1 \n
        contac.es.z3r0.gt@gmail.com

Registro
--------
    Importaciones relativas: 0.0.0.1
        * imports
    
Modulos incluidos
-----------------
    BasisViewpot: 0.0.0.1
        Nodo base para todo objeto que tiene pantalla
    BasisSquare:  0.0.0.1
        Nodo base para todo objeto que tiene tamaño de pantalla
    ScreenTools:  0.0.0.1
        Nodo de utilidad para la pantalla
"""
from           .BasisViewport import *
from ..constant.BasisSquare   import *

from ..tools.   ScreenTools import *

class BasisUI(BasisSquare, BasisViewPort):
    def __init__(self, name: str, id: int, abs: str, chr:str, x:int, y:int, comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__viewport__()
        super().__vector__(chr, x, y)
        
    def create_text(self,
                    text:str,
                    sector:Literal["CENTER", "UPPER", "LOWER", "CUSTOM"],
                    line:list[int, int]=...,
                    chk=True):
        
        if self.abs in COMPONENTS_UI_VE:
            vec = self.vec
        elif self.abs in COMPONENTS_UI_TF:
            vec = self.transform
            
        checker_coord(line, vec)
        
        def __recursive__(ver:list[bool, int]):
            temp = []
            new  = ""
            checker_coord(ver, vec)
            
            for chr_per in range(len(text)-ver[1]-2, len(text)):
                temp.append(text[chr_per])
            
            for chr_all in range(len(temp)):
                new += temp[chr_all]
                
            self.create_text(new, [line[0], line[1]+1], sector, False)
            del new, temp, chr_per, chr_all
        
        self.__del_pre_view__()
        
        if sector == "CUSTOM":
            ver = self._edit_line_square_([(line)], text)  
            if ver[0]:
                __recursive__(ver)
        elif sector == "UPPER":
            if chk:
                line=(1,1)
            ver = self._edit_line_square_([(line)], text)
        elif sector == "CENTER":
            if chk:
                line = (int(vec[0]/2)-5, int(vec[1]/2))
            ver = self._edit_line_square_([(line)], text)
            if ver[0]:
                __recursive__(ver)
        elif sector == "LOWER":
            if chk:
                line = (1, vec[1]-2)
            ver = self._edit_line_square_([(line)], text)            
            if ver[0]:
                self.square[-2] = self._set_frame_square_(vec, "last")
                __recursive__(ver)
                
        self.__set_pre_view__()