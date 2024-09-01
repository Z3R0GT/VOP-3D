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
if __name__ == "__main__":
    from sys import exit
    exit(1)

from typing_extensions import Literal
from time import sleep
from typing import overload

from ...util import *

def _set_name_(nme:str, nme_dtf:Literal["DEFAULT + NRO"]|list|tuple) -> str:
    """Crear un nombre por defecto en caso la literal no sea dado

    Args:
        nme (str): nombre literal
        nme_dtf (Literal[&quot;DEFAULT + NRO&quot;]): nombre dado

    Returns:
        str: nombre final
    """
    if nme != "":
        return nme
    else: 
        return f"{nme_dtf[0]}_{nme_dtf[1]}"
    
class BasisNode:
    def __init__(self, name:str, id:int, abs:str, comment:str|None=None ) -> None:
        """Clase por defecto de cualquier objeto visto o no en pantalla
        Args:
            name (str): nombre del nodo
            id (int): Identificador unico
            abs (str): abreviatua del nodo
            comment (str | None, optional): comentario del nodo. Defaults to None.
        """
        self.name = _set_name_(name, (abs, id))

        self.id   = id
        self.abs  = abs
        self.comment= comment
    
        self.meta = {"name":self.name, 
                     "id":self.id,
                     "abs":self.abs,
                     "comment":self.comment 
                     }

    def __set_meta__(self, nme:str, kwr:str|int|list|tuple|dict):
        """Crea una llave dado un valor para el objeto

        Args:
            nme (str): llave
            kwr (str | int | list | tuple | dict): valor
        """
        self.meta[nme] = kwr

    def _edit_meta_(self, nme:str, kwr:str|int|list|tuple|dict, pos:str|int=...):
        """Edita el valor de un objeto

        Args:
            nme (str): llave
            kwr (str | int | list | tuple | dict): valor
            pos (str | int, optional): en caso que el valor sea lista, dar la posición. Defaults to ....
        """
        if type(pos) != type(...):
            if type(kwr) == type([]) or type(kwr) == type({}): 
                self.meta[nme][pos].append(kwr)
            else:
                self.meta[nme].append(kwr) 
        else:
            self.__set_meta__(nme, kwr)

    def get_meta(self, isPrint:bool=True) -> dict:
        """Imprime la información de meta (y la retorna)

        Args:
            isPrint (bool, optional): ¿se puede imprimir?. Defaults to True.

        Returns:
            dict: representación de la actual meta
        """
        if isPrint:
            print(self.meta)
        return self.meta

    def del_meta(self, nme):
        """Borra una valor (es permanente)

        Args:
            nme (_type_): llave
        """
        try:
            del self.meta[nme]
        except KeyError:
            return