"""
Nodo base para todo objeto que tiene tamaño y posición en pantalla

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
    Vector: 0.0.0.1
        nodo base para las coordenadas
"""
from ..constant.Vector import *


class BasisSquare(Vector):
    """
    Conjunto de funciones horientados a los cuadrados en sus diferentes
    direcciones, tamaños y vectores
    """
    def __square__(self)-> None:
        """Agrega las propiedad 'square' y 'pre_view'
        """
        self.square  :list[str]
        self.pre_view:str

    def set_pre_view(self) -> None:
        """Crea un frame de como se ve actualmente
        """
        
    def del_pre_view(self) -> None:
        """Purga la variable 'pre_view'
        """
        
    def get_pre_view(self, isPrint:bool=True) -> str:
        """Imprime la variable 'pre_view' y la retorna

        Args:
            isPrint (bool, optional): ¿puede imprimir la variable?. Defaults to True.

        Returns:
            str: 'pre_view' en estado puro
        """
        
    def del_square(self) -> None:
        """Purga la variable 'square'
        """
        
    def get_square(self) -> list:
        """retorno el actual 'square'

        Returns:
            list: 'square' en estado puro
        """
    
    @deprecated("Usado durante las primeras versiones, ahora no muy usado")
    def _set_line_square_(self) -> None:
        """
        Función interna que se encarga una linea base a 
        un caracter
        """

    @overload
    def set_frame_square(self) -> None:
        """_summary_
        """
    @overload
    def set_frame_square(self,*, chr:str="default") -> None:
        """
        Args:
            chr (str, optional): _description_. Defaults to "".
        """
    @overload 
    def set_frame_square(self,*, chr:str="default", line:Literal["last", "start"]="start") -> str:
        """_summary_

        Args:
            line (Literal[&quot;last&quot;, &quot;start&quot;]): _description_
            chr (str, optional): _description_. Defaults to "".
        """
        
    def set_frame_num_square(self) -> None:
        """_summary_
        """
        
    def edit_line_square(self,*, coords:list[int, int], chr="") -> tuple[bool, int]:
        """_summary_

        Args:
            coord (list[list[int, int]]): _description_
            chr (str, optional): _description_. Defaults to "default".
        """
        
    def edit_multi_line_square(self,*, coords:list[int, int], chr="", auto:bool=True)->None|tuple[bool, int]:
        """agrega multiples lineas
        en caso no quiera que se agreguen lineas no planeadas, solo desactive con 'auto'

        Args:
            coords (list[int, int]): _description_
            chr (str, optional): _description_. Defaults to "".
            auto (bool, optional): _description_. Defaults to True.
        """