"""
Da coordenadas y transformados al nodo

Contribuidores
-------------
    Z3R0_GT: 0.0.0.1 \n
        contac.es.z3r0.gt@gmail.com

Registro
--------
    Importaciones relativas : 0.0.0.1
        * agregados importaciones

Modulos incluidos
-----------------
    BasisNode : 0.0.0.1
        Nodo base para todo objeto
"""
from ..include.BasisNode import *

COMPONENTS_UI_VE:list[str]
"""Componentes que usan vec"""
COMPONENTS_UI_TF:list[str]
"""Componentes que usan transformador"""

class Vector(BasisNode):
    """
    Conjunto de funciones y variables orientadas a objetos
    que tienen un lugar dentro del espacio
    """
    @overload
    def __vector__(self, *,chr:str, x:int, y:int) -> None:
        """Vector en 2D

        Args:
            chr (str): Caracter inicial
            x (int): posicion X
            y (int): posicion Y
        """
        self.character:str
        
        self.vec      :list[int, int]
        self._tmp_vec_:list[int, int]
    @overload
    def __vector__(self, *,chr:str, x:int, y:int, z:int) -> None:
        """Vector en 3D

        Args:
            chr (str): Caracter inicial
            x (int): posicion X
            y (int): posicion Y
            z (int): posicion Z
        """
        self.character:str
        
        self.vec      :list[int, int, int]
        self._tmp_vec_:list[int, int, int]
    @overload
    def __transform__(self, *,size_x:int, size_y:int) -> None:
        """Transformador en 2D

        Args:
            size_x (int): tamaño X
            size_y (int): tamaño Y
        """
        self.transform:list[int, int]
    @overload
    def __transform__(self, *,size_x:int, size_y:int, size_z:int) -> None:
        """Transformador en 3D

        Args:
            size_x (int): tamaño X
            size_y (int): tamaño Y
            size_z (int): tamaño Z
        """
        self.transform:list[int, int, int]

    def kind_vector(self) -> tuple[list[int, int], Literal["vec", "trans"]]:
        """Consulta y returna si el tipo de nodo 
        es vector o transformador

        Returns:
            Vector (tuple[list[int, int], str]): VEC/TRANS y abreviatura
        """














