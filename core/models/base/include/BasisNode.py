from ...util import *
from ..tools.logic import *

def set_name(nme:str, nme_dtf:Literal["DEFAULT + NRO"]|list) -> str:
    if nme != "":
        return nme
    else:
        return f"{nme_dtf[0]}-{nme_dtf[1]}"

__get_meta_att__ = ["isPrint"]

class BasisNode:
    def __init__(self, name:str, id:int, abs:str, comment:str|None=None ) -> None:
        self.name   :str = set_name(name, (abs, id))
        
        self.id     :int = id
        self.abs    :str = abs   
        self.comment:str = comment
    
        self.meta   :dict= {
            "name":self.name,
            "id":self.id,
            "abs":self.abs,
            "comment":self.comment
        }
        
    def set_meta(self, nme, kwr:str|int|list|tuple|dict) -> None:
        self.meta[nme] = kwr
    
    def edit_meta(self, nme:str, kwr:str|int|list|tuple|dict, pos:str|int=...):
        if type(pos) != type(...):
            if type(kwr) == type([]) or type(kwr) == type({}): 
                self.meta[nme][pos].append(kwr)
            else:
                self.meta[nme].append(kwr) 
        else:
            self.set_meta(nme, kwr)
            
    def get_meta(self, isPrint:bool=True) -> dict:
        if isPrint:
            print(self.meta)
        return self.meta
            
    def del_meta(self, nme):
        try:
            del self.meta[nme]
        except KeyError:
            return