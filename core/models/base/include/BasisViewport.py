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
if __name__ == "__main__":
    from sys import exit
    exit(1)

from .BasisNode import *

VIEWPORT_LIMIT:int=2

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
    if not hasattr(line, "append"):
        raise IncorrectTypeNode(line)    
    if not len(line) == VIEWPORT_LIMIT:
        raise CoordNotFound(line)
    
    if limit == "ex":
        return
    
    if not hasattr(limit, "append"):
        raise IncorrectTypeNode(limit)
    if not len(limit) == VIEWPORT_LIMIT:
        raise CoordNotFound(limit)
    
    if line[0] > limit[0]:
        raise CoordExced(line[0], limit[0])
    if line[1] > limit[1]:
        raise CoordExced(line[1], limit[1])

class BasisViewPort(BasisNode):
    def __viewport__(self) -> None:
        """Agrega las propiedad 'square' y 'pre_view'
        """
        self.square = []
        self.pre_view = ""

    def __set_pre_view__(self):
        """Crea un frame de como se ve actualmente
        """
        self.__del_pre_view__()
        for line in self.square:
            self.pre_view += f"{line}\n"

    def __del_pre_view__(self):
        """Purga la variable 'pre_view'
        """
        self.pre_view = ""
    
    def get_pre_view(self, isPrint:bool=True) -> str:
        """Imprime la variable 'pre_view' y la retorna

        Args:
            isPrint (bool, optional): ¿puede imprimir la variable?. Defaults to True.

        Returns:
            str: 'pre_view' en estado puro
        """
        if isPrint:
            print(self.pre_view)
        return self.pre_view
    
    
    def __del_square__(self):
        """Purga la variable 'square'
        """
        self.square = []

    def get_square(self) -> list:
        """retorno el actual 'square'

        Returns:
            list: 'square' en estado puro
        """
        return self.square