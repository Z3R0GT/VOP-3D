from typing_extensions import (
    deprecated, 
    overload, 
    Literal, 
    Self)
from ...util.exceptions import (
    CoordInConflict,
    CoordNotFound,
    CoordExced,
    IncorrectTypeNode)

def contains(kwargs:dict, key:list[str]|str, throw:bool=False) -> bool:
    if type(key) == type(""):
        key:list[str] = [key]
    
    for i in key:
        if not kwargs.__contains__(i):
            if throw:
                raise TypeError(f"El objeto requiere el argumento {i} de tipo {type(key)}")
            else:
                return False
    return True

def hasmutlattr(obj:object, name:list[str])->bool:
    for i in name:
        if not hasattr(obj, i):
            return False
    return True

__sto_n_attr__ = ["value", "kind"]
__sto_m_attr__ = ["node", "abs"]


@overload
def secure_type_one(*, value, kind:str) -> str:...
@overload
def secure_type_one(*, value, kind:int) -> int:...
@overload
def secure_type_one(*, value, kind:bool) -> bool:...
@overload
def secure_type_one(*, value, kind:list) -> list:...
@overload
def secure_type_one(*, value, kind:dict) -> dict:...
@overload
def secure_type_one(*, node, abs:str) -> Self:...
def secure_type_one(**kwargs:dict):
    #cuando es propio de python
    if contains(kwargs, __sto_n_attr__):
        value = kwargs["value"]
        kind  = kwargs["kind"]
        if not type(value) == type(kind):
            raise ValueError(f"Se esperaba un {type(kind)} no {type(value)}")
        return value
    #cuando pertenece a BasisNode
    elif contains(kwargs, __sto_m_attr__):
        if not kwargs["node"].abs == kwargs["abs"]:
            raise IncorrectTypeNode(kwargs["node"], f"Tipo abs:{kwargs["abs"]}")
        return kwargs["node"]
    else:
        #TODO: mejorar el mensaje
        #print(kwargs)
        raise TypeError("argumentos mucho o insuficientes")
        ...
    
__stm_m_attr__ = ["value", "kinds"]
#TODO: mejorar este argumento para se más "literal" en lo que pide
__stm_b_attr__ = ["all"]

@overload
def secute_type_multi(*, value, kinds:list) -> None:...
@overload
def secute_type_multi(*, all:list[list[object| list[str]| str]]|list[object| list[str]| str]) -> None:...
def secute_type_multi(**kwargs):
    if contains(kwargs, __stm_m_attr__):
        for i in kwargs["kinds"]:
            try:
                return secure_type_one(value=kwargs["value"], kind=i)
            except ValueError:
                pass
        raise ValueError("El valor no coincide con ningun de los esperados")
    elif contains(kwargs, __stm_b_attr__):
        #en caso use list[list[...]]
        if hasattr(kwargs["all"][0], "append"):
            for info in kwargs["all"]:
                if not hasmutlattr(info[0], info[1]):
                    raise IncorrectTypeNode(info[0], info[2])
        else:
            if not hasmutlattr(kwargs["all"][0], kwargs["all"][1]):
                raise IncorrectTypeNode(kwargs["all"][0], kwargs["all"][2])
    else:
        #TODO: mejorar el mensaje
        #print(kwargs)
        raise TypeError("argumentos mucho o insuficientes")   
            
__check_att_nor__ = ["line", "limit", "vector"]
__check_att_num__ = ["num_from", "num_to", "great"]
__check_att_nod__ = ["node_from", "node_to"]
    

@overload
def checker(*, line:list[int, int],
            limit:list[int, int]|Literal["ex"],
            vector:int=2) -> None:...
@overload
def checker(*, line:list[int, int, int],
            limit:list[int, int, int]|Literal["ex"],
            vector:int=3) -> None:...
@overload
def checker(*, num_from:int, num_to:int, great:bool=True) -> None:...
@overload
def checker(*, node_from, 
            node_to:Literal["ex"]) -> None:...
def checker(**kwargs:dict):
    #NOTE: caso de coordenadas (más común)
    if contains(kwargs, __check_att_nor__):
        line  = secure_type_one(value=kwargs["line"], kind=[])
        limit = secute_type_multi(value=kwargs["limit"], kinds=["", []])
        
        vector = secure_type_one(value=kwargs["vector"], kind=1)
         
        if not len(line) == vector:
            raise CoordNotFound(line)
        if limit == "ex":
            return
        if not len(limit) == vector:
            raise CoordNotFound(limit)
        
        for i in range(kwargs["vector"]):
            if not ( line[i] in range(0, limit[i]) ):
                raise CoordExced(line[i], limit[i])
    #NOTE: caso de nodos
    elif contains(kwargs, __check_att_nod__):
        node_base = kwargs["node_from"]
        node_to   = kwargs["node_to"]
        if node_to == "ex":
            return
        
        er = "Heredado de 'BasisTreeNode'"
        secute_type_multi(all=[[node_base, ["child_lst", "child_tlt"], er], 
                               [node_to  ,  ["vec", "abs"], er]
                               ])
        for nodes in node_base.child_lst:
            if hasattr(nodes, "real") or nodes.name == node_to.name:
                continue
            
            if nodes.vec == node_to.vec:
                raise CoordInConflict(nodes, node_to)
    elif contains(kwargs, __check_att_num__):
        #TODO: simplificar
        if kwargs["great"]:
            if not kwargs["num_from"] > kwargs["num_to"]:
                raise CoordExced(kwargs["num_to"], kwargs["num_from"])
        else:
            if not kwargs["num_from"] < kwargs["num_to"]:
                raise CoordExced(kwargs["num_from"], kwargs["num_to"])
    else:
        #TODO: mejorar el mensaje
        #print(kwargs)
        raise TypeError("argumentos mucho o insuficientes")   