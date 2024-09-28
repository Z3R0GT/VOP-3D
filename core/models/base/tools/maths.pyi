from ..       .util      import *
from ..include.BasisNode import *

VIEWPORT_LIMIT:int
"""Limite dentro de la coordenada"""

@deprecated("algún dia sera borrada, no usarla muy amenudo", stacklevel=3)
def insert(old:str, new:str, 
           form:int=..., to:int=...) -> str:
    """Viejo función pensada para insertar una cadena
    de texto pero manteniendo el tamaño de la cadena 
    original 
    
    Args:
        old (str): original
        new (str): insertar
        form (int, optional): coordenada de inicio. Defaults to ....
        to (int, optional): coordenada limite. Defaults to ....

    Returns:
        str: nueva cadenas de texto
    """

@overload
def checker(line:list[int, int, int]|list[int, int],
            limit:list[int, int, int]|list[int, int]|Literal["ex"]
            ):
    """Verifica la integridad de las coordenadas

    Args:
        line (list[int, int, int] | list[int, int]): linea dada
        limit (list[int, int, int] | list[int, int] | Literal[&quot;ex&quot;]): linea limite

    Raises:
        IncorrectTypeNode: nodo incorrecto
        CoordNotFound: coordenadas no encontrada
        CoordExced: coordenada excedida
    """
@overload
def checker(node:BasisNode):
    """Verifica que las coordenadas de un nodo no este en conflicto

    Args:
        node (BasisNode): Nodo dado
        
    Raises:
        CoordInConflict: coordenada en conflicto
    """