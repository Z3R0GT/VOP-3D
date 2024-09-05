"""
Nodo base para cualquier objeto que tenga interfaz

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
    BasisViewpot: 0.0.0.1
        Nodo base para todo objeto que tiene pantalla
    BasisSquare:  0.0.0.1
        Nodo base para todo objeto que tiene tamaño de pantalla
    ScreenTools:  0.0.0.1
        Nodo de utilidad para la pantalla
"""
from           .BasisViewport import *
from ..constant.BasisSquare   import *

from ..tools.   ScreenTools import *
from sys import exit

class BasisUI(BasisSquare):
    """Nodo base para ñas interfazes graficas"""
    def create_text(self,
                    text:str,
                    sector:Literal["CENTER", "UPPER", "LOWER", "CUSTOM"],
                    line:list[int, int]=...,
                    chk=True):
        """Agrega un texto a la pantalla

        Args:
            text (str): Texto a colocar
            sector (Literal[&quot;CENTER&quot;, &quot;UPPER&quot;, &quot;LOWER&quot;, &quot;CUSTOM&quot;]): Zona a colocar
            line (list[int, int], optional): coordenada a insertar el texto. Defaults to ....
            chk (bool, optional): Variable de control privada. Defaults to True.
        """

