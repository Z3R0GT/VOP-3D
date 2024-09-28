from ...include.BasisSquare import *
from ...tools.tools import *

MARK_SCAPE ="\n>  "
class BasisUI(BasisSquare):
    def __init__(self, name: str, 
                 id: int, 
                 abs: str, 
                 chr:str,
                 x:int,
                 y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__square__()
        super().__vector__(chr=chr, x=x, y=y)
        
    def create_text(self, 
                    text:str, 
                    sector:Literal["CENTER", "UPPER", "LOWER", "CUSTOM"],
                    line:list[int, int]=...,
                    auto:bool=True):
        
        vec = self.kind_vector()[0]
        checker(line=line, limit=vec, vector=2)
        
        #def __recursive__(ver:list)
        
        self.del_pre_view()
        match sector:
            case "CUSTOM":
                a = self.edit_multi_line_square(coords=line, chr=text, auto=auto)
            case "UPPER":
                line = [1,1]
                a = self.edit_multi_line_square(coords=line, chr=text)
            case "CENTER":
                line = [int(vec[0]/2)-5, int(vec[1]/2)]
                a = self.edit_multi_line_square(coords=line, chr=text)
            case "LOWER":
                line = [1, vec[1]-2]
                a = self.edit_multi_line_square(coords=line, chr=text)
        
        self.set_pre_view()