if __name__ == "__main__":
    from sys import exit
    exit(1)
from time import *

from ...util import *

def _set_name_(nme:str, nme_dtf:Literal["DEFAULT + NRO"]|list|tuple) -> str:
    if nme != "":
        return nme
    else: 
        return f"{nme_dtf[0]}_{nme_dtf[1]}"
    
class BasisNode:
    def __init__(self, name:str, id:int, abs:str, comment:str|None=None ) -> None:
        self.name = _set_name_(name, (abs, id))

        self.id   = id
        self.abs  = abs
        self.comment= comment
    
        self.meta = {"name":self.name, 
                     "id":self.id,
                     "abs":self.abs,
                     "comment":self.comment 
                     }

    def __set_meta__(self, nme:str, kwr:str|int|list|tuple|dict):
        self.meta[nme] = kwr

    def _edit_meta_(self, nme:str, kwr:str|int|list|tuple|dict, pos:str|int=...):
        if type(pos) != type(...):
            if type(kwr) == type([]) or type(kwr) == type({}): 
                self.meta[nme][pos].append(kwr)
            else:
                self.meta[nme].append(kwr) 
        else:
            self.__set_meta__(nme, kwr)

    def get_meta(self, isPrint:bool=True) -> dict:
        if isPrint:
            print(self.meta)
        return self.meta

    def del_meta(self, nme):
        try:
            del self.meta[nme]
        except KeyError:
            return