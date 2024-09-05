"""
Nodo base para todo objeto que tiene tamaño de pantalla

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
    BasisViewPort: 0.0.0.1
        nodo base para la pantalla
"""
COMPONENTS_UI_VE:list[str]
"""Componentes que usan vec"""
COMPONENTS_UI_TF:list[str]
"""Componentes que usan transformador"""

from typing import overload

from ..include.BasisViewport import *

def insert(old_:str|list, new_:str|list, 
             from_:int=..., to_:int=..., 
             specific_:int=...) -> str:
    """Viejo función pensada para insertar una cadena
    de texto pero manteniendo el tamaño de la cadena 
    original 

    Args:
        old_ (str | list): original
        new_ (str | list): a insertar
        from_ (int, optional): coordenada de inicio. Defaults to ....
        to_ (int, optional): coordenada limite. Defaults to ....
        specific_ (int, optional): se dara en un punto en concreto. Defaults to ....

    Returns:
        str: nueva cadenas de texto
    """

class BasisSquare(BasisViewPort):
    """
    Conjunto de funciones horientados a los cuadrados en sus diferentes
    direcciones, tamaños y vectores
    """
    @overload
    def __vector__(self, chr:str, x:int, y:int) -> None:
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
    def __vector__(self, chr:str, x:int, y:int, z:int) -> None:
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
    def __transform__(self, size_x:int, size_y:int) -> None:
        """Transformador en 2D

        Args:
            size_x (int): tamaño X
            size_y (int): tamaño Y
        """
        self.transform:list[int, int]
    @overload
    def __transform__(self, size_x:int, size_y:int, size_z:int) -> None:
        """Transformador en 3D

        Args:
            size_x (int): tamaño X
            size_y (int): tamaño Y
            size_z (int): tamaño Z
        """
        self.transform:list[int, int, int]

    @deprecated("Usado durante las primeras versiones, ahora no muy usado")
    def _set_line_square_(self) -> None:
        """
        Función interna que se encarga una linea base a 
        un caracter
        """
        
    def _set_frame_num_square_(self) -> None:
        """
        Función interna encargada de crear una linea de números de
        referencia para las coordenadas 
        """

    def _edit_line_square_(self, coords:list[tuple[int, int]], 
                           CHR:str="") -> tuple[bool,int]:
        """Edita una linea concreta dentro del square

        Args:
            coords (list[tuple[int, int]]): Coordenadas
            CHR (str, optional): Texto/Character a reemplazar. Defaults to "".

        Returns:
            tuple[bool,int]: Representación de una linea concreta
        """
        
    def _set_frame_square_(self,
                             single:Literal["last", "start", "none"]="none",
                             chr="") -> None | str:
        """Crea el cuadrado necesario para la interfaz con base a una 
        sere de tamaños

        Args:
            single (Literal[&quot;last&quot;, &quot;start&quot;, &quot;none&quot;], optional): "linea literal". Defaults to "none".
            chr (str, optional): _description_. Defaults to "".

        Returns:
            None | str: _description_
        """

    def __kind_vector__(self) -> list[int, int]:
        """Retorna el tipo de vecotr a emplear a base de la clase 
        de componente que sea

        Returns:
            list[int, int]: Representación del tamaño de l objeto
        """
