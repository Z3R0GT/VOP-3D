from ..       .util      import *
from ..include.BasisNode import *

@deprecated("algún dia sera borrada, no usarla muy amenudo (función 'insert')", stacklevel=1)
def insert(old:str, new:str, 
           form:int, to:int=...) -> str:
    old = list(old)
    
    if to == ...:
        to = len(new) + form
    
    c=0
    for ch in range(len(old)):
        if ch in range(form, to):
            old[ch] = new[c] 
            c+=1
    mew = ""
    for i in old:
        mew+=i
        
    return mew

VIEWPORT_LIMIT:int = 2

def checker(*args) -> None:
    if hasattr(args[0], "append"):
        line :list[int, int, int]|list[int, int]
        limit:list[int, int, int]|list[int, int]|Literal["ex"]

        if not hasattr(line, "append"):
            raise TypeError(f"Se esperaba una lista, no {line}/{type(line)}")
        if not len(line) == VIEWPORT_LIMIT:
            raise CoordNotFound(line)
        
        if limit == "ex":
            return
        
        if not hasattr(limit, "append"):
            raise TypeError(f"Se esperaba una lista, no {line}/{type(line)}")
        if not len(limit) == VIEWPORT_LIMIT:
            raise CoordNotFound(limit)
        
        if line[0] > limit[0] or line[0] < 0:
            raise CoordExced(line, limit)
        if line[1] > limit[1] or line[1] < 0:
            raise CoordExced(line, limit)
    elif hasattr(args[0], "comp_ch"):
        node_base  = args[0]
        node_to    = args[1]
        
        if node_to == "ex":
            return
        for nodes in node_base.child_lst:
            if hasattr(nodes, "real") or nodes.name == node_to.name:
                continue
            
            if nodes.vec == node_to.vec:
                raise CoordInConflict(nodes, node_to)
    