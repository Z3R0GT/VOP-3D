"""
Nodo base para todo objeto que provee de tamaño e hijos

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
    BasisSquare: 0.0.0.1
        nodo base para la pantalla
    BasisTreeNode: 0.0.0.1
        nodo base todo objeto que necesite heredar y proveer hijos
"""
from .BasisSquare import *
from ..include.BasisTreeNode import *

class BasisRoot(BasisSquare, BasisTreeNode):
    """Nodo base para todo objeto que necesite hijo y tenga un tamaño
    """
    
    def __update_children__(self, father_update:bool=True):        
        """Metodo empleado para aquellos objetos que requiere refrescar
        sus pre_view por un nodo (puede ser propio o uno padre)
        
        Args:
            father_update (bool, optional): ¿puede actualizarse?. Defaults to True.
            
        Raises:
            HasNotChilds: lanzado en caso el nodo no tenga hijo disponibles
        """
    
    def __updater_father__(self):
        """Metodo empleado para aquellos objetos que requiere refrescar
        sus pre_view por un nodo hijo

        Raises:
            HasNotChilds: lanzado en caso el nodo no tenga hijo disponibles
        """
    