"""
Conjunto de excepciones generales que puede o no lanzarse de vez
en cuanto obtengas alguno de estos muy probablemente no quieras
volver a usar esto

Contribuidores
-------------
    Z3R0_GT: 0.0.0.1 \n
        contac.es.z3r0.gt@gmail.com

Registro
--------
    Coordenadas: 0.0.0.1
        * se agregaron excepciones para las coordenadas 

Modulos incluidos
-----------------
    typing_extensions: 3.12
        * usado para decoración

"""
from typing_extensions import *

#######################
#######################
#     Coordenadas     #
#######################
#######################
class CoordNotFound(ValueError):
    """Lanzado cuando las coordenadas no son suficientes"""
    def __init__(self, coord:list[int], *args: object) -> None:
        self.message = f"Se necesitan una o más coordenadas ({coord}, {len(coord)})"
        self.foo     = coord
        super().__init__(self.message, *args)

class CoordInConflict(ValueError):
    """Lanzado cuando la coordenada esta en conflicto a otra"""
    def __init__(self, node_f, node_t, *args: object) -> None:
        self.message = f"El nodo {node_f.name} esta en conflicto con {node_t.name}\n\
            Coordenada desde: {node_f.vec}\n\
            Coordenada hasta: {node_t.vec}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)

class CoordExced(ValueError):
    """Lanzado cuando alguna coordenada esta fuera del limite"""
    def __init__(self, limit_f:list[int, int]|int, limit_t:list[int, int]|int, *args: object) -> None:
        self.message = f"Una o más coordenadas estan fuera de los limites\n\
            Coordenada ingresada: {limit_f}\n\
            Coordenada limite:    {limit_t}"
        self.foo = (limit_f, limit_t)
        super().__init__(self.message, *args)


#######################
#######################
#     Incorrectos     #
#######################
#######################
class IncorrectVector(TypeError):
    """Lanzado cuando el vector no es una lista"""
    def __init__(self, node_f, node_t:str, *args: object) -> None:
        self.message = f"Se esperada un {node_t} no {type(node_f)}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)

class IncorrectTypeNode(TypeError):
    """Lanzado cuando un nodo es incorrecto"""
    def __init__(self, node_f, node_t:list, *args: object) -> None:
        self.message = f"EL nodo dado no es compatible con el actual\n\
            Dado:     {node_f.abs}/{type(node_f)} \n\
            Esperado: {node_t}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)


#######################
#######################
#     Arbol nodos     #
#######################
#######################
class IsNotAChild(BaseException):
    """Lanzado cuando un nodo no es un hijo"""
    def __init__(self, node_f, node_t, *args: object) -> None:
        self.message = f"El nodo no puede ser hijo\n\
            Dado:  {node_f.name}/{type(node_f)}\n\
            Padre: {node_t.name}/{type(node_t)}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)

class IsNotAFather(BaseException):
    def __init__(self, node_f, node_t, *args: object) -> None:
        self.message = f"El nodo no puede ser padre\n\
            Dado:  {node_f.name}/{type(node_f)}\n\
            hijo: {node_t.name}/{type(node_t)}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)

class NotChildsIn(BaseException):
    """Lanzado cuando se referencia a un hijo que no existe"""
    def __init__(self, node_f, node_t, *args: object) -> None:
        self.message = f"El nodo actual no tiene hijo\n\
            Referenciado: {node_f.name}/{type(node_f)}\n\
            Nodo:         {node_t.name}/{type(node_t)}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)
        
class NotFathersIn(BaseException):
    """Lanzado cuando se referencia a un padre que no existe"""
    def __init__(self, node_f, node_t, *args: object) -> None:
        self.message = f"El nodo actual no tiene por padre o no tiene padres\n\
            Referenciado: {node_f.name}/{type(node_f)}\n\
            Nodo:         {node_t.name}/{type(node_f)}"
        self.foo = (node_f, node_t)
        super().__init__(self.message, *args)
        
class NodeDuplicade(BaseException):
    """Lanzado cuando un nodo ya existe"""
    def __init__(self, node_f, node_p, node_t, *args: object) -> None:
        self.message = f"El nodo ya existe dentro del padre\n\
            Referenciado:  {node_f.name}/{type(node_f)}\n\
            ID de creación:{node_p}\n\
            Nodo:          {node_t.name}/{type(node_t)}"
        self.foo = (node_f, node_t, node_p)
        super().__init__(self.message, *args)


