"""
Nodo base para todo objeto que tiene pantalla

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
    BasisNode: 0.0.0.1
        Nodo base generico
"""
from .BasisNode import *

VIEWPORT_LIMIT:int
"""Limite dentro de la coordenada"""

def checker_coord(line:list[int, int, int]|list[int, int],
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
    
class BasisViewPort(BasisNode):
    """Nodo base para todo objeto que requiera coordenadas y otros"""
    
    def __viewport__(self) -> None:
        """Agrega las propiedad 'square' y 'pre_view'
        """
        self.square:list[str]
        self.pre_view:str
        
        
    def __set_pre_view__(self) -> None:
        """Crea un frame de como se ve actualmente
        """
        
    def __del_pre_view__(self) -> None:
        """Purga la variable 'pre_view'
        """
        
    def get_pre_view(self, isPrint:bool=True) -> str:
        """Imprime la variable 'pre_view' y la retorna

        Args:
            isPrint (bool, optional): ¿puede imprimir la variable?. Defaults to True.

        Returns:
            str: 'pre_view' en estado puro
        """
        
    def __del_square__(self) -> None:
        """Purga la variable 'square'
        """
        
    def get_square(self) -> list:
        """retorno el actual 'square'

        Returns:
            list: 'square' en estado puro
        """
        
        
        
        
        
        
        
        
        