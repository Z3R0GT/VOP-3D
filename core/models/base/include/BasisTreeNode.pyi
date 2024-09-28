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
    ################
    # Requiere documentación nueva
    # ###############    
    @deprecated("requiere de un plateamiento claro", stacklevel=3)
    def edit_child(self, node:BasisNode, **kwargs):
        """_summary_

        Args:
            node (BasisNode): _description_
        """
        
    def del_child(self, node:BasisNode, *, kind:Literal["static", "dinamic"]="static", is_new:bool=True):
        """_summary_

        Args:
            node (BasisNode): _description_
            kind (Literal[&quot;static&quot;, &quot;dinamic&quot;], optional): _description_. Defaults to "static".
            is_new (bool, optional): _description_. Defaults to True.
        """
        
    def find_child(self, node:BasisNode) -> int:
        """_summary_

        Args:
            node (BasisNode): _description_

        Returns:
            int: _description_
        """
        
    def can_be_added(self, node:BasisNode, *, kind:Literal["ch", "fa"]="ch", throw:bool=False) -> bool:
        """_summary_

        Args:
            node (BasisNode): _description_
            kind (Literal[&quot;ch&quot;, &quot;fa&quot;], optional): _description_. Defaults to "ch".
            throw (bool, optional): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
    
    @deprecated("No se recomienda usar 'node_f' como argumento AÚN, el basico de mover un nodo a otra parte del codigo sigue siendo 'funcional' ")
    @overload
    def move_to(self, node_f:BasisNode|list[BasisNode], node_t:BasisNode|list[BasisNode])->None:
        """_summary_

        Args:
            node_f (_type_): _description_
            node_t (_type_): _description_
        """
    @overload
    def move_to(self, node_f:BasisNode) -> None:
        """_summary_

        Args:
            node_f (BasisNode): _description_
        """
        
        
    