"""
Nodo base para cualquier objeto del tipo boton

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
    BasisUI: 0.0.0.1
        Nodo base para cualquier objeto que tenga interfaz
    ScreenTools: 0.0.0.1
        Nodo de utilidad
"""
from .BasisUI import *
from ..tools.ScreenTools import *

class BasisButtons(BasisUI):
    """Clase general para todo objeto que requiera usar funciones
    por acción propia o literal
    """
    def __func__(self, func) -> None:
        """Asigna una función a la variable action

        Args:
            func (_type_): función a guardar
        """
        self.action
        
    def _input_(self, msg:tuple[str]) -> None:
        """Ejecuta una seria de preguntas con base al mensaje dado,
        luego de ello llama a la función correspondiente bajo el concepto de::
            
            def my_función(entrada, variables_internas) -> None:
                #hace algo
                return
            
        Soporta que no tenga preguntas en cuyo caso solo sera::

            def my_función(list:[], variable_internas) -> None:
                #hace algo
                return
        
        Args:
            msg (tuple[str]): representación de las pregunta a hacer
        """
        self._in_:list
        
    def execute(self, *arg):
        """Ejecuta el 'action', puede mandarle argumentos opcionales
        puede ser más directo
        """