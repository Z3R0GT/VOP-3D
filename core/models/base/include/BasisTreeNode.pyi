"""
Nodo base para cualquier objeto que requiera heredar

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
        Nodo base para cualquier objeto
"""
from .BasisNode import *

class BasisTreeNode(BasisNode):
    """Nodo base para todo aquellos que esten horientados a tener o proveer de hijos a sus 
    pares
    """
    def __father_node__(self, components:list) -> None:
        """Constructor para nodos que puedan tener hijos

        Args:
            components (list): Abreviaturas de los nodos hijo
        """
        self.child_lst:list[BasisNode]
        self.child_tlt:int
        
        self.comp_ch:list[str]

    def __child_node__(self, components:list) -> None:
        """Constructor para nodos que puedan tener padre

        Args:
            components (list): Abreviaturas de los nodos padres
        """
        self.father:BasisNode
        self.in_id :int
        
        self.comp_fa:list[str]
        
    def add_child(self, node:BasisNode, is_new:bool=True) -> None:
        """Agrega un hijo al nodo (usa 'can_be_father') para
        verificar su el nodo puede o no ser usado

        Args:
            node (BasisNode): nodo a agregar
            is_new (bool, optional): ¿ya fue agregado antes?. Defaults to True.
        """
        
    def edit_child(self, child:BasisNode, *args) -> None:
        """Edita las propiedades un hijo

        Args:
            child (BasisNode): propiedades
        """
        
    def del_child(self, child:BasisNode,*, is_new:bool=True, kind:Literal["static", "dinamic"]="static") -> None:
        """Borra a un hijo de manera opcional/definitiva

        Args:
            child (BasisNode): 
                nodo a borrar
            is_new (bool, optional): 
                ¿ya fue agregado antes?. Defaults to True.
            kind (Literal[&quot;static&quot;, &quot;dinamic&quot;], optional): 
                static: Solo reemplaza la posición del nodo 
                dinamic: hace como si el nodo nunca hubiera existido. Defaults to "static".
        """
        
    def can_be_child(self, node:BasisNode,*,throw:bool=False) -> bool:
        """Indica si un nodo puede ser o no un hijo

        Args:
            node (BasisNode): nodo a consultar
            throw (bool, optional): ¿puede soltar una error?. Defaults to False.

        Returns:
            bool: representación de la pregunta
        """
        
    def can_be_father(self, node:BasisNode,*,throw:bool=False) -> bool:
        """Indica si un nodo puede ser o no un padre

        Args:
            node (BasisNode): nodo a consultar
            throw (bool, optional): ¿puede soltar una error?. Defaults to False.

        Returns:
            bool: representación de la pregunta
        """

    @deprecated("Requiere de un reemplanteamiento por IN_ID como list(int)", stacklevel=3)
    def move_child(self, child_from:BasisNode, child_to:BasisNode) -> None:
        """Mover un nodo a otra posición de otro hijo, siempre ambos
        sean hijos del mismo nodo

        Args:
            child_from (BasisNode): hijo desde
            child_to (BasisNode): hijo hasta
        """
        
    @deprecated("Requiere de un reemplanteamiento por IN_ID como list(int)", stacklevel=3)
    def move_father(self, father_to:BasisNode) -> None:
        """Reemplazar el actual padre a otro de un nodo hijo

        Args:
            father_to (BasisNode): padre a reemplazar
        """

    def __update_child__(self):
        """Actualiza el meta de un nodo hijo
        """

    def __update_father__(self):
        """Actualiza el meta de un nodo padre
        """

