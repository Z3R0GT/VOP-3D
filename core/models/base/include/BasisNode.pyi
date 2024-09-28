"""
Nodo base para cualquier objeto

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
    Literal: 4.12.2
        Decorador opcional
    sleep:    3.12
        Función del modulo time desde sleep
    overload: 3.12
        Función del modulo typing desde overload
"""
from ...util import *
from ..tools.logic import *

class BasisNode:
    """Clase por defecto de cualquier objeto visto o no en pantalla
    """  
    def __init__(self, name:str, id:int, abs:str, comment:str|None=None ) -> None:
        self.name   :str
        
        self.id     :int
        self.abs    :str        
        self.comment:str
    
        self.meta   :dict
    
    def set_meta(self, nme:str, kwr:str|int|list|tuple|dict) -> None:
        """Crea una llave dado un valor para el objeto

        Args:
            nme (str): llave
            kwr (str | int | list | tuple | dict): valor
        """
    
    @deprecated("Se requiere pensar como simplificarlo usando herramientas actuales", stacklevel=3)
    def edit_meta(self, nme:str, kwr:str|int|list|tuple|dict, pos:str|int=...) -> None:
        """Edita el valor de un objeto

        Args:
            nme (str): llave
            kwr (str | int | list | tuple | dict): valor
            pos (str | int, optional): en caso que el valor sea lista, dar la posición. Defaults to ....
        """

    def get_meta(self, isPrint:bool=True) -> dict:
        """Imprime la información de meta (y la retorna)

        Args:
            isPrint (bool, optional): ¿se puede imprimir?. Defaults to True.

        Returns:
            dict: representación de la actual meta
        """
        
    def del_meta(self, nme):
        """Borra una valor (es permanente)

        Args:
            nme (_type_): llave
        """